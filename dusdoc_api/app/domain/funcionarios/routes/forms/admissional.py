from quart import Response, jsonify, make_response  # noqa: D100
from quart.views import MethodView

from dusdoc_api.models.users.admin import Users


class AdmissionalFormView(MethodView):  # noqa: D101
    init_every_request = False
    methods = ["GET", "POST"]

    def __init__(self, model: Users) -> None:  # noqa: D107
        self.model = model

    async def get(self) -> Response:  # noqa: ANN003, ANN201
        return await make_response(jsonify(ok="ok"))

    async def post(self) -> Response:  # noqa: ANN003, ANN201
        return await make_response(jsonify(ok="ok"))
