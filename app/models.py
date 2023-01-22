from configuration.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class User(Base):
    __tablename__ = "users"
    email: Column(String, unique=True, index=True)
    first_name: Column(String)
    last_name: Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return self.email
