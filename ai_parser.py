import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def parse_request(user_request, student_data):

    prompt = f"""
You are an attendance management AI.

Convert the user's request into JSON.

Student data:
{json.dumps(student_data, indent=2)}

User request:
{user_request}

Return ONLY valid JSON.

Allowed actions:

1. check_attendance
2. mark_attendance
3. remove_attendance
4. get_percentage

JSON formats:

check_attendance:
{{
  "action": "check_attendance",
  "roll_no": "101",
  "date": "2026-10-10"
}}

mark_attendance:
{{
  "action": "mark_attendance",
  "roll_no": "101",
  "date": "2026-10-10",
  "status": "P"
}}

remove_attendance:
{{
  "action": "remove_attendance",
  "roll_no": "101",
  "date": "2026-10-10"
}}

get_percentage:
{{
  "action": "get_percentage",
  "roll_no": "101"
}}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return json.loads(response.output_text)