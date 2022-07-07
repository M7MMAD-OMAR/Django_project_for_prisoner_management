from sq.ddd.publisher import EventPublisher
from sq.ddd.base import DomainObject


class EventSourcedAggregate(DomainObject):
    """The base class for all event-sourced aggegrates.

    This class provides a conveniant building block for designing
    event-sourced aggegrates. It collects all events published
    within the aggregate and makes them available to the repositories
    for persistence.
    """
    __abstract__ = True

    @property
    def events(self):
        return self.__publisher__

    def __new__(cls, *args, **kwargs):
        instance = super(EventSourcedAggregate, cls).__new__(cls)
        instance.id = None
        instance.__publisher__ = EventPublisher(instance)
        return instance

