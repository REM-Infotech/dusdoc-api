# noqa: D100
import json

from quart import Response, jsonify, make_response, request
from quart.views import MethodView
from werkzeug.datastructures import CombinedMultiDict  # noqa: F401

from dusdoc_api.models.users.admin import Users


class AdmissionalFormView(MethodView):  # noqa: D101
    init_every_request = False
    methods = ["GET", "POST"]

    def __init__(self, model: Users) -> None:  # noqa: D107
        self.model = model

    async def get(self) -> Response:  # noqa: ANN003, ANN201
        return await make_response(jsonify(ok="ok"))

    async def post(self) -> Response:  # noqa: ANN003, ANN201
        files = await request.files  # noqa: F841
        data = await request.data or await request.form or await request.json

        if isinstance(data, bytes):
            data = data.decode()
            if isinstance(data, str):
                data = json.loads(data)

        for k, v in list(data.items()):
            print(f"{k}: {v}")

        return await make_response(jsonify(ok="ok"))
