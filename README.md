# AI Attendance Management System

A terminal-based attendance management system built with Python, JSON, and AI-powered natural-language processing. The system allows users to check student attendance, calculate attendance percentages, mark or remove attendance, and calculate the overall class attendance average without a frontend.

## 🚀 Features

- **JSON-Based Storage:** Stores student details and daily attendance records in `students.json`.
- **AI-Powered Commands:** Converts natural-language requests into structured JSON actions.
- **Check Attendance:** Check whether a student was present or absent on a particular date.
- **Mark Attendance:** Mark a student as Present (`P`) or Absent (`A`).
- **Remove Attendance:** Remove or reset an attendance record.
- **Automatic Percentage Calculation:** Recalculates attendance percentages after updates.
- **Class Attendance Average:** Calculates the average attendance percentage across all students.
- **Terminal Interface:** Interact with the system directly through the command line.
- **No Frontend Required:** The entire application runs in the terminal.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Storage:** JSON
- **AI Integration:** OpenAI API or a compatible AI provider
- **Libraries:** `openai`, `python-dotenv`

## 📁 Project Structure

```text
Attendance-AI/
├── main.py
├── attendance.py
├── ai_parser.py
├── students.json
├── requirements.txt
├── .env
└── README.md
```

### File Descriptions

| File | Purpose |
|---|---|
| `main.py` | Runs the terminal interface and processes user requests. |
| `attendance.py` | Handles attendance operations, percentage calculations, and JSON updates. |
| `ai_parser.py` | Converts natural-language requests into structured JSON actions using an AI API. |
| `students.json` | Stores student information and daily attendance records. |
| `requirements.txt` | Lists the Python dependencies. |
| `.env` | Stores API credentials securely. |

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Attendance-AI.git
cd Attendance-AI
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` has not been created yet, add:

```text
openai
python-dotenv
```

Then run the installation command again.

### 4. Configure the API Key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace the placeholder with your own valid OpenAI API key.

**Security:** Never commit your actual API key to GitHub. If you use Hugging Face instead, configure the appropriate token and update `ai_parser.py` for that provider.

### 5. Run the Application

```bash
python main.py
```

The system will start in the terminal and prompt you to enter an attendance-related request.

## 💻 Example Usage

### Check Attendance

**Input:**

```text
Was Rahul Kumar present on 10 October 2026?
```

**Structured AI Action:**

```json
{
  "action": "check_attendance",
  "roll_no": "101",
  "date": "2026-10-10"
}
```

**Example Output:**

```json
{
  "action": "check_attendance",
  "roll_no": "101",
  "name": "Rahul Kumar",
  "date": "2026-10-10",
  "status": "P"
}
```

Here, `P` means Present and `A` means Absent.

### Get Attendance Percentage

**Input:**

```text
What is Rahul Kumar's attendance percentage?
```

**Example Output:**

```json
{
  "action": "get_percentage",
  "roll_no": "101",
  "name": "Rahul Kumar",
  "attendance_percentage": 85.71
}
```

### Mark Attendance

**Input:**

```text
Mark Rahul Kumar present on 10 October 2026.
```

The AI converts the request into a structured action, and Python updates `students.json` and recalculates the student's attendance percentage.

### Remove Attendance

**Input:**

```text
Remove Rahul Kumar's attendance for 10 October 2026.
```

The application processes the request and updates the student's attendance record.

### Calculate Class Average

The application calculates the average of the attendance percentages of all students in the dataset.

The calculation is performed by Python rather than the AI model to improve numerical accuracy and consistency.

## 📊 Attendance Calculation

Individual attendance percentage:

```text
Attendance Percentage =
(Present Days / Total Attendance Days) × 100
```

Class average attendance percentage:

```text
Class Average =
Sum of Individual Attendance Percentages
/ Number of Students
```

For example, if five students have attendance percentages of 80%, 70%, 90%, 60%, and 100%, the class average is 80%.

**Note:** This is the arithmetic mean of individual student percentages. It may differ from the overall attendance rate calculated using total student-days present divided by total possible student-days.

## 📅 Attendance Data Format

The application uses JSON to store student data.

Example:

```json
{
  "name": "Rahul Kumar",
  "roll_no": "101",
  "total_days": 7,
  "present_days": 6,
  "attendance_percentage": 85.71,
  "attendance": {
    "2026-10-08": "P",
    "2026-10-09": "P",
    "2026-10-10": "A",
    "2026-10-11": "P",
    "2026-10-12": "P",
    "2026-10-13": "P",
    "2026-10-14": "P"
  }
}
```

The sample attendance period is **8 October 2026 to 14 October 2026**.

## 🔐 Security and Data Integrity

- Keep API keys in `.env`.
- Add `.env` and `venv/` to `.gitignore`.
- Validate AI-generated actions before executing them.
- Verify student roll numbers and dates before changing attendance.
- Recalculate percentages in Python instead of trusting AI-generated numbers.
- Back up `students.json` before important changes.
- Do not use real student personal information in a public repository.

Example `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

## ⚠️ Current Limitations

- The application uses a local JSON file rather than a database.
- AI functionality requires a correctly configured, supported API provider.
- The application is designed for terminal interaction only.
- The sample student records are demonstration data.
- Validation and error handling should be strengthened before production use.
- The current design is intended for a small prototype, not concurrent multi-user attendance management.

## 🔮 Future Enhancements

- Support for multiple classes and semesters.
- Attendance reports in CSV and Excel formats.
- Database integration using SQLite or PostgreSQL.
- Student-wise attendance history.
- Low-attendance alerts.
- Date-range reports and attendance summaries.
- Improved validation and audit logs.
- Support for additional AI providers.

## 🎯 Project Objective

The goal of this project is to demonstrate how Python, JSON-based storage, and AI can work together to create a simple attendance management system that understands natural-language commands and converts them into structured operations.

The project also demonstrates the separation of responsibilities between AI-based request interpretation and deterministic Python calculations.

## 👨‍💻 Author

SATYAM VISHWAKARMA

## 📄 License

This project is available for educational and learning purposes. Add a suitable open-source license, such as the MIT License, if you intend to permit reuse and redistribution.
