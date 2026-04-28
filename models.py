from sqlalchemy import Column, Integer, String, Date
from database import Base
import datetime

class Job(Base):
    __tablename__ = "jobs"

    id           = Column(Integer, primary_key=True, index=True)
    company      = Column(String, nullable=False)
    role         = Column(String, nullable=False)
    status       = Column(String, default="applied")
    date_applied = Column(Date, default=datetime.date.today)
    notes        = Column(String, nullable=True)