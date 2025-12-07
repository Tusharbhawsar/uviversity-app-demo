# seed.py

from datetime import date
import random
from database import engine, SessionLocal
import models

# ----------------------------------------
# Reset DB
# ----------------------------------------
models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    # ----------------------------------------
    # Departments (REAL DATA)
    # ----------------------------------------
    dept_data = [
        ("Computer Science", "Building A"),
        ("Information Technology", "Building B"),
        ("Electrical Engineering", "Building C"),
        ("Mechanical Engineering", "Building D"),
        ("Civil Engineering", "Building E"),
        ("Business Administration", "Building F"),
        ("Economics", "Building G"),
        ("Physics", "Building H"),
        ("Mathematics", "Building I"),
        ("Biotechnology", "Building J"),
    ]

    departments = [
        models.Department(Department_Name=name, Office_Location=loc)
        for name, loc in dept_data
    ]
    db.add_all(departments)
    db.commit()

    # ----------------------------------------
    # Students (REAL NAMES)
    # ----------------------------------------
    student_data = [
        ("Aarav Sharma", "aarav.sharma@example.com", "9876543210"),
        ("Riya Patel", "riya.patel@example.com", "9876543201"),
        ("Kabir Mehta", "kabir.mehta@example.com", "9845123789"),
        ("Sara Khan", "sara.khan@example.com", "9823412378"),
        ("Arjun Verma", "arjun.verma@example.com", "9898989898"),
        ("Meera Joshi", "meera.joshi@example.com", "9812312345"),
        ("Dev Malhotra", "dev.malhotra@example.com", "9876501234"),
        ("Ananya Gupta", "ananya.gupta@example.com", "9812298765"),
        ("Ishaan Bhatia", "ishaan.bhatia@example.com", "9890123456"),
        ("Tara Nair", "tara.nair@example.com", "9823123456"),
    ]

    students = [
        models.Student(
            Name=name,
            Email=email,
            Phone=phone,
            Department_ID=random.randint(1, 10),
        )
        for name, email, phone in student_data
    ]
    db.add_all(students)
    db.commit()

    # ----------------------------------------
    # Instructors (REAL TEACHER NAMES)
    # ----------------------------------------
    instructor_data = [
        ("Dr. Neha Kapoor", "neha.kapoor@university.com", "A-101"),
        ("Prof. Raghav Iyer", "raghav.iyer@university.com", "B-214"),
        ("Dr. Sunita Rao", "sunita.rao@university.com", "C-305"),
        ("Dr. Vikram Sinha", "vikram.sinha@university.com", "D-112"),
        ("Prof. Leena Joseph", "leena.joseph@university.com", "E-220"),
        ("Dr. Arvind Menon", "arvind.menon@university.com", "F-330"),
        ("Prof. Pooja Desai", "pooja.desai@university.com", "G-120"),
        ("Dr. Amit Kulkarni", "amit.kulkarni@university.com", "H-145"),
        ("Prof. Mohan Rao", "mohan.rao@university.com", "I-132"),
        ("Dr. Shalini Mehta", "shalini.mehta@university.com", "J-201"),
    ]

    instructors = [
        models.Instructor(
            Name=name,
            Email=email,
            Office_No=office,
            Department_ID=random.randint(1, 10),
        )
        for name, email, office in instructor_data
    ]
    db.add_all(instructors)
    db.commit()

    # ----------------------------------------
    # Courses (REAL COURSE NAMES)
    # ----------------------------------------
    course_data = [
        ("Data Structures & Algorithms", 4),
        ("Database Management Systems", 3),
        ("Operating Systems", 4),
        ("Software Engineering", 3),
        ("Computer Networks", 3),
        ("Machine Learning", 4),
        ("Artificial Intelligence", 4),
        ("Thermodynamics", 3),
        ("Business Analytics", 3),
        ("Microbiology Basics", 4),
    ]

    courses = [
        models.Course(
            Course_Name=name,
            Credits=credits,
            Department_ID=random.randint(1, 10),
            Instructor_ID=random.randint(1, 10),
        )
        for name, credits in course_data
    ]
    db.add_all(courses)
    db.commit()

    # ----------------------------------------
    # Registrations (Unique & Valid)
    # ----------------------------------------
    semester = "Fall 2025"
    used_pairs = set()
    registrations = []

    while len(registrations) < 10:
        sid = random.randint(1, 10)
        cid = random.randint(1, 10)
        key = (sid, cid, semester)

        if key in used_pairs:
            continue

        used_pairs.add(key)
        registrations.append(
            models.Registration(
                Student_ID=sid,
                Course_ID=cid,
                Semester=semester,
                Registration_Date=date.today(),
            )
        )

    db.add_all(registrations)
    db.commit()

    print("REAL DATA SEEDING COMPLETED!")

finally:
    db.close()
