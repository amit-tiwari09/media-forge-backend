class AppException(Exception):

    def __init__(
        self,
        message: str,
        statusCode: int = 400,
        errors: dict[str, list[str]] | None = None,
    ):
        self.message = message
        self.statusCode = statusCode
        self.errors = errors

        super().__init__(message)
