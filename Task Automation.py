import re

def extract_emails(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
    with open(output_file, "w", encoding="utf-8") as out:
        for email in emails:
            out.write(email + "\n")
    print(f"Extracted {len(emails)} emails from source.txt to {output_file}")

extract_emails("source.txt", "collected_emails.txt")