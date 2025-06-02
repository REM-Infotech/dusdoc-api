from quart import Blueprint, request


auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])
async def login():
    """
    Handle user login.
    """
    request
    return "Login Page"
