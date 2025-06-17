from quart import Blueprint, Response, jsonify, make_response  # noqa: D100
from quart_jwt_extended import create_access_token

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])
async def login() -> Response:
    """Handle user login."""
    username = "user"

    return await make_response(
        jsonify({
            "message": "Login successful",
            "token": create_access_token(identity=username),
        }),
        200,
    )
