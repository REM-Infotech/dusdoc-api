from uuid import uuid4

from sqlalchemy import Column, ForeignKey, Integer, LargeBinary, String

from dusdoc_api.app import db

files = db.Table(
    "files",
    db.Column("file_id", Integer, db.ForeignKey("file.id"), primary_key=True),
    db.Column(
        "cached_form_id", Integer, db.ForeignKey("cached_form.id"), primary_key=True
    ),
)


class FileModel(db.Model):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True, default=int(uuid4().hex, 16))
    filename = Column(String)
    blob = Column(LargeBinary)
    temporary_path = Column(String)


class CacheForms(db.Model):
    __tablename__ = "cached_form"
    id = Column(Integer, primary_key=True, default=int(uuid4().hex, 16))
    user_id = Column(Integer, ForeignKey("users.id"))
    files = bots = db.relationship(
        "FileModel",
        secondary="files",
        backref=db.backref("cached_form", lazy=True),
    )
