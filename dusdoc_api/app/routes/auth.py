from quart import Blueprint



auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/login", methods=["GET", "POST"])
async def login():
    """
    Handle user login.
    """
    return "Login Page"