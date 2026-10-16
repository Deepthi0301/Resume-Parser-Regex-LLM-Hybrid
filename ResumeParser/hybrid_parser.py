
import json
import sys
from pathlib import Path

from regex_parser import extract_text, extract_information as regex_extract
from llm_parser import extract_information as llm_extract


def parse_resume(file_path):
    try:
        # Read the resume once
        resume_text = extract_text(file_path)

        if not resume_text.strip():
            print("Error: No text found in this resume.")
            return

        # Approach 1: Extract information using regex
        regex_data = regex_extract(resume_text)

        # Approach 2: Extract information using the LLM
        llm_data = llm_extract(resume_text)

        # Approach 3: Combine both results
        hybrid_data = {}

        # Regex is generally more reliable for email and phone patterns
        for field in ["email_address", "phone_number"]:
            hybrid_data[field] = (
                regex_data.get(field) or llm_data.get(field)
            )

        # Use AI for fields that need more understanding.
        # If AI has no result, fall back to regex.
        fields = [
            "full_name",
            "technical_skills",
            "educational_qualifications",
            "work_experience",
            "projects",
            "certifications"
        ]

        for field in fields:
            ai_value = llm_data.get(field)
            regex_value = regex_data.get(field)

            if ai_value:
                hybrid_data[field] = ai_value
            else:
                hybrid_data[field] = regex_value

        # Save the combined result
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        output_file = (
            output_dir / (Path(file_path).stem + "_hybrid_parsed.json")
        )

        output_file.write_text(
            json.dumps(hybrid_data, indent=4, ensure_ascii=False),
            encoding="utf-8"
        )

        print(json.dumps(hybrid_data, indent=4, ensure_ascii=False))
        print(f"\nJSON saved to: {output_file.resolve()}")

    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Could not parse resume: {error}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hybrid_parser.py <resume_file>")
    else:
        parse_resume(sys.argv[1])
