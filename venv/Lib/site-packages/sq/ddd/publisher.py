import contextlib
import os
import uuid

from sq.datastructures import ImmutableDTO
from sq.datastructures import DTO
from sq.exc import ImplementationError
from sq.ddd.exc import InconsistentAggregateState
import sq.timezone


class EventPublisher:
    """Publishes events produced in an event-sourced
    aggregate.
    """

    @property
    def version(self):
        return self.__version

    @property
    def namespace(self):
        return type(self.__instance).__name__.lower()

    def __init__(self, instance):
        self.__instance = instance
        self.__events = []
        self.__streaming = False
        self.__version = 1
        self.__handlers = {}

    def count(self):
        return len(self.__events)

    def publish(self, name, **params):
        """Publish a new domain event. Note that this method can
        not be invoked in domain event handler functions to preserve
        the consistency of the event stream.
        """
        if self.__streaming:
            raise ImplementationError("Cannot publish event during stream.")
        with self.stream() as publish:
            event = DTO(
                urn="%s:%s" % (self.namespace, name.lower()),
                name=name,
                params=ImmutableDTO(params).as_dto(),
                version=self.__version,
                timestamp=sq.timezone.now()
            )
            publish(event)

    def _publish(self, event, replay=False):
        if not replay:
            self.__events.append(event)
        self.handle(event)

    @contextlib.contextmanager
    def stream(self, replay=False):
        """Context-manager that prevents domain events being
        published within the context block.
        """
        self.__streaming = True
        try:
            yield (lambda e: self._publish(e, replay=replay))
        finally:
            self.__streaming = False

    def consume(self):
        """Return a generator consuming all pending domain events.
        Set a correlation identifier to group events together.
        """
        if not self.__events:
            raise StopIteration

        if self.__instance.id is None:
            raise ImplementationError(
                "Can not consume event stream before aggregate has"
                "been assigned an identifier.")

        cid = str(uuid.UUID(bytes=os.urandom(16)))
        while self.__events:
            event = self.__events.pop(0)
            event.aggregate_id = self.__instance.id
            event.correlation_id = cid
            event.timestamp = sq.timezone.now()
            yield ImmutableDTO(event).as_dto()

    def handle(self, event):
        """Invoke the domain event handler for an event.

        Args:
            event: a Data Transfer Object (DTO) identifying
                the event and containing the parameters.

        Returns:
            None

        Raises:
            InconsistentAggregateState: the event version did
                not match the aggregate version.
            ImplementationError: no event handler method was
                declared on the aggregate class.
        """
        instance = self.__instance
        if event.version != self.__version:
            raise InconsistentAggregateState(
                "Aggregate version mismatches with event.")

        fn = self.__handlers.get(event.name)
        if fn is None:
            attname = "on_%s" % (event.name.lower())
            try:
                fn = self.__handlers[event.name] = getattr(self.__instance, attname)
            except AttributeError:
                raise ImplementationError("%s must declare method `%s` to handle "
                                          "event %s" % (type(instance).__name__,
                                            attname, event.name))

        fn(event.params)
        self.__version += 1

    def __iter__(self):
        return iter(self.__events)
