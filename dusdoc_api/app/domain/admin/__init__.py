"""
Admin domain package for dusdoc_api.

Provides registration functions for admin routes, API endpoints, and SocketIO namespaces for the Quart application.
This module organizes the setup of admin-related features, including user and employee management,
and integrates them into the application instance.
"""

# noqa: D104

from quart import Quart
from quart_socketio import SocketIO

from dusdoc_api.app.domain.admin.namespaces.funcionarios import FuncionariosNamespace
from dusdoc_api.app.domain.admin.routes import registry_endpoint_admin

# from dusdoc_api.app.domain.admin.namespaces.docs import adminDocsNamespace
# from dusdoc_api.app.domain.admin.namespaces.forms import adminFormsNamespace
# from dusdoc_api.app.domain.admin.namespaces.system import DusdocNamespace


async def register_routes_admin(app: Quart) -> None:
    """
    Register all admin-related routes with the Quart application.

    Args:
        app (Quart): The Quart application instance.

    """
    from .routes import admin
    from .routes.auth import auth
    from .routes.forms import forms

    blueprints = [auth, forms, admin]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # Add any additional routes or blueprints here as needed


async def register_api_admin(app: Quart) -> None:
    """
    Register admin-related API endpoints with the Quart application.

    Set up URL routes for admin functionalities such as admission and employee registration forms.
    Bind view classes to specific endpoints and register them with the application's blueprint.

    Args:
        app (Quart): The Quart application instance.

    """
    from dusdoc_api.models.users.admin import Users

    from .routes.forms import forms
    from .routes.funcionario import AdmissionalFormView, CadastroFuncionarioView

    form_admissional = AdmissionalFormView.as_view("AdmissionalForm", Users)
    forms.add_url_rule("/funcionario/admissional", view_func=form_admissional)

    form_cadastro_funcionario = CadastroFuncionarioView.as_view("CadastroFuncionarioView", Users)
    forms.add_url_rule("/funcionario/cadastro", view_func=form_cadastro_funcionario)
    registry_endpoint_admin()


async def register_namespace_admin(io: SocketIO) -> None:
    """
    Register admin-related SocketIO namespaces.

    Args:
        io (SocketIO): The SocketIO instance.

    """
    namespaces = [
        FuncionariosNamespace("/admin_funcionarios_informacoes", io),
    ]

    for namespace in namespaces:
        await io.register_namespace(namespace)


async def registry_admin(app: Quart, io: SocketIO) -> None:
    """
    Register all admin-related routes, API endpoints, and namespaces with the application.

    Args:
        app (Quart): The Quart application instance.
        io (SocketIO): The SocketIO instance.

    """
    await register_api_admin(app)
    await register_routes_admin(app)
    await register_namespace_admin(io)
