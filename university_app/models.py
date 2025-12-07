from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database import Base

class Department(Base):
    __tablename__ = "departments"

    Department_ID = Column(Integer, primary_key=True, index=True)
    Department_Name = Column(String)
    Office_Location = Column(String)

    students = relationship("Student", back_populates="department")
    instructors = relationship("Instructor", back_populates="department")
    courses = relationship("Course", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    Student_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Email = Column(String)
    Phone = Column(String)
    Department_ID = Column(Integer, ForeignKey("departments.Department_ID"))

    department = relationship("Department", back_populates="students")
    registrations = relationship("Registration", back_populates="student")


class Instructor(Base):
    __tablename__ = "instructors"

    Instructor_ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Email = Column(String)
    Office_No = Column(String)
    Department_ID = Column(Integer, ForeignKey("departments.Department_ID"))

    department = relationship("Department", back_populates="instructors")
    courses = relationship("Course", back_populates="instructor")


class Course(Base):
    __tablename__ = "courses"

    Course_ID = Column(Integer, primary_key=True, index=True)
    Course_Name = Column(String)
    Credits = Column(Integer)
    Department_ID = Column(Integer, ForeignKey("departments.Department_ID"))
    Instructor_ID = Column(Integer, ForeignKey("instructors.Instructor_ID"))

    department = relationship("Department", back_populates="courses")
    instructor = relationship("Instructor", back_populates="courses")
    registrations = relationship("Registration", back_populates="course")


class Registration(Base):
    __tablename__ = "registrations"
    __table_args__ = (
        UniqueConstraint("Student_ID", "Course_ID", "Semester"),
    )

    Registration_ID = Column(Integer, primary_key=True, index=True)
    Student_ID = Column(Integer, ForeignKey("students.Student_ID"))
    Course_ID = Column(Integer, ForeignKey("courses.Course_ID"))
    Semester = Column(String)
    Registration_Date = Column(Date)

    student = relationship("Student", back_populates="registrations")
    course = relationship("Course", back_populates="registrations")
