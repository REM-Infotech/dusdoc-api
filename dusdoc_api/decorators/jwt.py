from functools import wraps


def jwt_socketio_required(func):
    """
    Decorator to require JWT authentication for Socket.IO events.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        from quart_jwt_extended.utils import verify_token_claims

        arg = args
        env = arg[0].server.environ
        # Verify the JWT in the request
        jwt_data = kwargs.get("token")
        verify_token_claims(jwt_data)

        # Call the original function
        return await func(*args, **kwargs)

    return wrapper
