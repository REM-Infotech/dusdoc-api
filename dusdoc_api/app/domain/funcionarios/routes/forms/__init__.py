# noqa: D104


from quart import Blueprint, Quart

forms = Blueprint("forms", __name__, url_prefix="/forms")


async def register_api_funcionario(app: Quart) -> None:  # noqa: D103
    from dusdoc_api.models.users.admin import Users

    from .admissional import AdmissionalFormView

    form_admissional = AdmissionalFormView.as_view("AdmissionalForm", Users)
    forms.add_url_rule("/admissional", view_func=form_admissional)
