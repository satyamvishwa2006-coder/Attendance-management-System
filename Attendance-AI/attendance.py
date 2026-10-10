import json

FILE_NAME = "students.json"


def load_data():
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=2)


def find_student(data, roll_no):
    for student in data["students"]:
        if student["roll_no"] == roll_no:
            return student

    return None


def recalculate(student):
    student["present_days"] = sum(
        1 for status in student["attendance"].values()
        if status == "P"
    )

    student["total_days"] = len(student["attendance"])

    if student["total_days"] > 0:
        student["attendance_percentage"] = round(
            student["present_days"] /
            student["total_days"] * 100,
            2
        )
    else:
        student["attendance_percentage"] = 0


def check_attendance(roll_no, date):
    data = load_data()
    student = find_student(data, roll_no)

    if not student:
        return {"error": "Student not found"}

    status = student["attendance"].get(date)

    return {
        "action": "check_attendance",
        "roll_no": roll_no,
        "name": student["name"],
        "date": date,
        "status": status
    }


def mark_attendance(roll_no, date, status):
    data = load_data()
    student = find_student(data, roll_no)

    if not student:
        return {"error": "Student not found"}

    student["attendance"][date] = status

    recalculate(student)
    save_data(data)

    return {
        "action": "mark_attendance",
        "roll_no": roll_no,
        "name": student["name"],
        "date": date,
        "status": status,
        "present_days": student["present_days"],
        "attendance_percentage": student["attendance_percentage"]
    }


def remove_attendance(roll_no, date):
    data = load_data()
    student = find_student(data, roll_no)

    if not student:
        return {"error": "Student not found"}

    if date in student["attendance"]:
        del student["attendance"][date]

    recalculate(student)
    save_data(data)

    return {
        "action": "remove_attendance",
        "roll_no": roll_no,
        "name": student["name"],
        "date": date,
        "present_days": student["present_days"],
        "attendance_percentage": student["attendance_percentage"]
    }


def class_average():
    data = load_data()

    percentages = [
        student["attendance_percentage"]
        for student in data["students"]
    ]

    if not percentages:
        return 0

    return round(sum(percentages) / len(percentages), 2)