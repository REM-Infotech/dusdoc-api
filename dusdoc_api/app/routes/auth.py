from quart import Blueprint, jsonify, make_response
from quart_jwt_extended import create_access_token

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["GET", "POST"])
async def login():
    """
    Handle user login.
    """

    username = "user"

    return await make_response(
        jsonify(
            {
                "message": "Login successful",
                "token": create_access_token(identity=username),
            }
        ),
        200,
    )
