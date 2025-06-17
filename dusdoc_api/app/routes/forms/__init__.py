# noqa: D104


from quart import Blueprint, Quart

from dusdoc_api.models.users.admin import Users

forms = Blueprint("forms", __name__, "/forms")


async def register_api(app: Quart) -> None:  # noqa: D103
    from .admissional import AdmissionalForm

    form_admissional = AdmissionalForm.as_view("form-admissional", Users)
    forms.add_url_rule("/admissional", view_func=form_admissional)
