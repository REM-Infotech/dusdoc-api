# noqa: D104


from quart import Quart
from quart_socketio import SocketIO

from dusdoc_api.app.domain.admin.namespaces.funcionarios import FuncionariosNamespace

# from dusdoc_api.app.domain.admin.namespaces.docs import adminDocsNamespace
# from dusdoc_api.app.domain.admin.namespaces.forms import adminFormsNamespace
# from dusdoc_api.app.domain.admin.namespaces.system import DusdocNamespace


async def register_routes_admin(app: Quart) -> None:
    """Register all routes with the Quart application."""
    from .routes.auth import auth
    from .routes.forms import forms

    blueprints = [auth, forms]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # Add any additional routes or blueprints here as needed


async def register_api_admin(app: Quart) -> None:  # noqa: D103
    from dusdoc_api.models.users.admin import Users

    from .routes.forms import forms
    from .routes.funcionario import AdmissionalFormView, CadastroFuncionarioView

    form_admissional = AdmissionalFormView.as_view("AdmissionalForm", Users)
    forms.add_url_rule("/funcionario/admissional", view_func=form_admissional)

    form_cadastro_funcionario = CadastroFuncionarioView.as_view("CadastroFuncionarioView", Users)
    forms.add_url_rule("/funcionario/cadastro", view_func=form_cadastro_funcionario)


async def register_namespace_admin(io: SocketIO) -> None:  # noqa: D103
    """"""  # noqa: D419
    namespaces = [
        FuncionariosNamespace("/admin_funcionarios_informacoes", io),
    ]

    for namespace in namespaces:
        await io.register_namespace(namespace)


async def registry_admin(app: Quart, io: SocketIO) -> None:  # noqa: D103
    await register_api_admin(app)
    await register_routes_admin(app)
    await register_namespace_admin(io)
