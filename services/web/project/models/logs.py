from __future__ import annotations
from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy

from .base import Base
from .. import db

class Log(Base):
    """
    Logs Table will logging every things that happens in the system
    """
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    table_name = db.Column(db.String(128))
    operation = db.Column(db.String(128))
    content = db.Column(db.String(256))
    target_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self,
                 table_name: str,
                 target_id: int,
                 created_at: datetime = datetime.now(),
                 updated_at: datetime = datetime.now(),
                 **kwargs):
        super().__init__(created_at, updated_at)
        self.table_name = table_name
        self.target_id = target_id