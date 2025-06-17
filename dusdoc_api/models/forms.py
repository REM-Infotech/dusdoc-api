from sqlalchemy import BigInteger, Column, ForeignKey, LargeBinary, String

from dusdoc_api.app import db

files = db.Table(
    "files",
    db.Column("file_id", BigInteger, db.ForeignKey("file.id"), primary_key=True),
    db.Column(
        "cached_form_id", BigInteger, db.ForeignKey("cached_form.id"), primary_key=True
    ),
)


class FileModel(db.Model):
    __tablename__ = "file"
    id = Column(BigInteger, primary_key=True)
    filename = Column(String)
    blob = Column(LargeBinary)
    temporary_path = Column(String)


class CacheForms(db.Model):
    __tablename__ = "cached_form"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    files = bots = db.relationship(
        "FileMode",
        secondary="files",
        backref=db.backref("cached_form", lazy=True),
    )
