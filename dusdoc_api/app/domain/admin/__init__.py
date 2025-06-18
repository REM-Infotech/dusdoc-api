# noqa: D104


from quart import Quart, Response
from quart_socketio import SocketIO

from dusdoc_api.app.domain.admin.namespaces.docs import adminDocsNamespace
from dusdoc_api.app.domain.admin.namespaces.forms import adminFormsNamespace
from dusdoc_api.app.domain.admin.namespaces.system import DusdocNamespace


async def register_routes_admin(app: Quart) -> None:
    """Register all routes with the Quart application."""
    from .routes.auth import auth
    from .routes.forms import forms

    blueprints = [auth, forms]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # Add any additional routes or blueprints here as needed

    @app.after_request
    async def allow_origin(response: Response) -> Response:  # noqa: ANN202
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response


async def register_api_admin(app: Quart) -> None:  # noqa: D103
    from dusdoc_api.models.users.admin import Users

    from .routes.forms import forms
    from .routes.forms.admissional import AdmissionalFormView

    form_admissional = AdmissionalFormView.as_view("AdmissionalForm", Users)
    forms.add_url_rule("/admissional", view_func=form_admissional)


async def register_namespace_admin(io: SocketIO) -> None:  # noqa: D103
    namespaces = [
        DusdocNamespace("/", io),
        adminFormsNamespace("/admin_forms", io),
        adminDocsNamespace("/admin_informacoes", io),
    ]

    for namespace in namespaces:
        await io.register_namespace(namespace)


async def registry_admin(app: Quart, io: SocketIO) -> None:  # noqa: D103
    await register_api_admin(app)
    # await register_namespace_admin(io)
