"""Canonical exceptions module for Sovereign Quantum
applications.
"""


class CanonicalException(Exception):
    """An exception class that renders to a ``CanonicalException``
    Data Transfer Object (DTO).
    """
    http_status = None
    code = None

    def __init__(self, code=None, message=None, detail=None, hint=None):
        self.code = code or self.code
        if self.code is None:
            raise TypeError("The `code` parameter is mandatory")
        self.message = message
        self.detail = detail
        self.hint = hint

    def as_dto(self):
        """Dumps the exception to a dictionary."""
        dto = {
            "code": self.code
        }
        if self.message:
            dto['message'] = self.message
        if self.detail:
            dto['detail'] = self.detail
        if self.hint:
            dto['hint'] = self.hint

        return dto


class ImplementationError(Exception):
    """Raised when the implementation of the Sovereign Quantum
    Framework is not according to the specification.
    """
    pass
