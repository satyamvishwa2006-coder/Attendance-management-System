import json

from attendance import (
    check_attendance,
    mark_attendance,
    remove_attendance,
    class_average,
    load_data,
    find_student
)

from ai_parser import parse_request


def execute_action(action):

    data = load_data()

    action_type = action["action"]
    roll_no = action.get("roll_no")

    if action_type == "check_attendance":

        return check_attendance(
            roll_no,
            action["date"]
        )

    elif action_type == "mark_attendance":

        return mark_attendance(
            roll_no,
            action["date"],
            action["status"]
        )

    elif action_type == "remove_attendance":

        return remove_attendance(
            roll_no,
            action["date"]
        )

    elif action_type == "get_percentage":

        student = find_student(
            data,
            roll_no
        )

        if not student:
            return {
                "error": "Student not found"
            }

        return {
            "action": "get_percentage",
            "roll_no": roll_no,
            "name": student["name"],
            "attendance_percentage":
                student["attendance_percentage"]
        }

    return {
        "error": "Unknown action"
    }


def main():

    print("=" * 50)
    print("      AI ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 50)

    while True:

        user_request = input("\nEnter request: ")

        if user_request.lower() in ["exit", "quit"]:
            print("Exiting...")
            break

        try:

            data = load_data()

            action = parse_request(
                user_request,
                data
            )

            print("\nAI JSON:")
            print(
                json.dumps(
                    action,
                    indent=2
                )
            )

            result = execute_action(action)

            print("\nRESULT:")
            print(
                json.dumps(
                    result,
                    indent=2
                )
            )

            print(
                "\nCLASS ATTENDANCE AVERAGE:",
                class_average(),
                "%"
            )

        except Exception as e:

            print("\nERROR:")
            print(str(e))


if __name__ == "__main__":
    main()