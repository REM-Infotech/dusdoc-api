from pathlib import Path  # noqa: D100, F401

from quart import request  # noqa: F401
from quart.datastructures import FileStorage  # noqa: F401
from quart_socketio import Namespace  # noqa: F401


# class FuncionarioFormsNamespace(Namespace):  # noqa: D101
#     async def on_admissional_form(self) -> bool | None:  # noqa: D102
#         try:
#             data = await request.socket_data
#             for _k, v in list(data.items()):
#                 v: FileStorage
#                 print(v.stream.read())

#             return True

#         except Exception as e:
#             print(e)
#             return False

#     async def on_admissional_files(self) -> bool:
#         try:
#             data = request.socket_data
#             for _k, v in list(data.items()):
#                 if isinstance(v, FileStorage):
#                     print(v.stream.read())

#                     parent = Path(__file__).parent.resolve()
#                     v.save(parent.joinpath(v.filename))
#             return True

#         except Exception as e:
#             print(e)
#             return False

#         return True
