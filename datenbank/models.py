import datetime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime, Date, Table

Base = declarative_base()


assocation_table = Table(
    "participant_course",
    Base.metadata,
    Column("participant_id",Integer,ForeignKey("participants.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer,primary_key=True,index=True,nullable=False)
    name = Column(String(40),nullable=False)
    surname = Column(String(20),nullable=False)
    email = Column(String(60), unique=True, index=True,nullable=False)
    date_of_birth = Column(Date,nullable=False)
    password = Column(String(100),nullable=False)
    number = Column(String(20),nullable=True)
    role = Column(String(20),nullable=False)
    created_at = Column(DateTime,default=datetime.UTC)
    courses = relationship("Course",secondary="participant_course",back_populates="participants")


class Teacher(Base):

    __tablename__ = "teachers"

    id = Column(Integer,primary_key=True,index=True,nullable=False)
    name = Column(String(40),nullable=False)
    surname = Column(String(20),nullable=False)
    email = Column(String(60), unique=True, index=True,nullable=False)
    date_of_birth = Column(Date,nullable=False)
    password = Column(String(100),nullable=False)
    number = Column(String(20),nullable=True)
    role = Column(String(20),nullable=False)
    created_at = Column(DateTime,default=datetime.UTC)
    course_id = Column(Integer,ForeignKey("courses.id"))
    course = relationship("Course",back_populates="teachers")

class Course(Base):

    __tablename__ = "courses"

    id = Column(Integer,primary_key=True,index=True)
    language = Column(String(20),nullable=False)
    start = Column(Date,nullable=False)
    end = Column(Date,nullable=False)
    created_at = Column(DateTime,nullable=False)
    participants = relationship("Participant",secondary="participant_course",back_populates="courses")
    teachers = relationship("Teacher",back_populates="course")









