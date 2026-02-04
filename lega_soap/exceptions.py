class LegaError(RuntimeError):
    pass


class AuthError(LegaError):
    pass


class ServiceError(LegaError):
    pass