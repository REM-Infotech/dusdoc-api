from quart import jsonify, make_response  # noqa: D100
from quart.views import MethodView

from dusdoc_api.models.users.admin import Users


class AdmissionalForm(MethodView):  # noqa: D101
    def __init__(self, model: Users) -> None:  # noqa: D107
        self.model = model

    async def post(self):  # noqa: ANN201
        return await make_response(jsonify(ok="ok"))
