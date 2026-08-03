import re

# Sample Resume Text
resume = """
Name: Ash Kumar
Email: ashkumar123@gmail.com
Phone: +91-9876543210

Skills:
Python, Java, SQL, HTML, CSS, Machine Learning

Education:
B.Tech in Computer Science

Experience:
Software Intern at ABC Technologies (2025-2026)
"""

# Extract Name
name = re.search(r"Name:\s*(.*)", resume)

# Extract Email
email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resume)

# Extract Phone Number
phone = re.search(r"(\+91[-\s]?)?[6-9]\d{9}", resume)

# Extract Skills
skills = re.search(r"Skills:\s*([\s\S]*?)Education:", resume)

# Extract Education
education = re.search(r"Education:\s*([\s\S]*?)Experience:", resume)

# Extract Experience
experience = re.search(r"Experience:\s*([\s\S]*)", resume)

# Print Results
print("----- Resume Information Extraction -----")

print("Name       :", name.group(1).strip() if name else "Not Found")
print("Email      :", email.group() if email else "Not Found")
print("Phone      :", phone.group() if phone else "Not Found")

print("\nSkills:")
if skills:
    print(skills.group(1).strip())

print("\nEducation:")
if education:
    print(education.group(1).strip())

print("\nExperience:")
if experience:
    print(experience.group(1).strip())
