from pydantic import BaseModel
from datetime import date

class DepartmentBase(BaseModel):
    Department_Name: str
    Office_Location: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    Department_ID: int
    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    Name: str
    Email: str
    Phone: str
    Department_ID: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    Student_ID: int
    class Config:
        orm_mode = True


class InstructorBase(BaseModel):
    Name: str
    Email: str
    Office_No: str
    Department_ID: int

class InstructorCreate(InstructorBase):
    pass

class Instructor(InstructorBase):
    Instructor_ID: int
    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    Course_Name: str
    Credits: int
    Department_ID: int
    Instructor_ID: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    Course_ID: int
    class Config:
        orm_mode = True


class RegistrationBase(BaseModel):
    Student_ID: int
    Course_ID: int
    Semester: str
    Registration_Date: date

class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    Registration_ID: int
    class Config:
        orm_mode = True
