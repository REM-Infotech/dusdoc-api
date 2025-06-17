from sqlalchemy import ForeignKey, Integer, LargeBinary, String

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
    id = db.Column(Integer, primary_key=True)
    filename = db.Column(String)
    blob = db.Column(LargeBinary)
    temporary_path = db.Column(String)


class CacheForms(db.Model):
    __tablename__ = "cached_form"
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey("users.id"))
    files = db.relationship(
        "FileModel",
        secondary="files",
        backref=db.backref("cached_form", lazy=True),
    )
