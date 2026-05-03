from database.conn import Base
from sqlalchemy import Boolean, Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func





class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    attendance_date=Column(Date)
    coaching=Column(Boolean)
    school=Column(Boolean)
    marked_at = Column(
        DateTime,
        server_default=func.now()
    )
