from pathlib import Path

html = Path("index.html").read_text(encoding="utf-8")
css = Path("style.css").read_text(encoding="utf-8")

required_fields = [
    'id="registrationForm"',
    'name="studentName"',
    'name="rollNumber"',
    'name="email"',
    'name="course"',
    'type="submit"'
]

for field in required_fields:
    assert field in html, f"FAIL: Missing {field}"

assert "style.css" in html, "FAIL: CSS file not linked"
assert ".card" in css, "FAIL: Card styling missing"

print("PASS: Registration form and all required fields exist.")
print("PASS: CSS is linked and styling is present.")