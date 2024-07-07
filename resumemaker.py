import openai

def parse_resume_to_json(resume_content):
    openai.api_key = 'your-api-key'

    prompt = f"""
    You are an AI designed to parse resumes. Please take the following resume content and convert it into JSON format with the following structure:

    {{
      "name": "Name",
      "contact_information": {{
        "email": "Email",
        "phone": "Phone",
        "address": "Address"
      }},
      "professional_summary": "Summary",
      "work_experience": [
        {{
          "job_title": "Job Title",
          "company": "Company",
          "location": "Location",
          "start_date": "Start Date",
          "end_date": "End Date",
          "responsibilities": [
            "Responsibility 1",
            "Responsibility 2",
            ...
          ]
        }},
        ...
      ],
      "education": [
        {{
          "degree": "Degree",
          "institution": "Institution",
          "location": "Location",
          "graduation_date": "Graduation Date"
        }},
        ...
      ],
      "skills": [
        "Skill 1",
        "Skill 2",
        ...
      ],
      "certifications": [
        {{
          "certification": "Certification",
          "issuing_organization": "Issuing Organization",
          "date": "Date"
        }},
        ...
      ],
      "projects": [
        {{
          "project_name": "Project Name",
          "description": "Description",
          "technologies_used": [
            "Technology 1",
            "Technology 2",
            ...
          ]
        }},
        ...
      ],
      "languages": [
        "Language 1",
        "Language 2",
        ...
      ],
      "hobbies": [
        "Hobby 1",
        "Hobby 2",
        ...
      ]
    }}

    Here is the resume content:
    {resume_content}
    """

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1500
    )

    return response.choices[0].text.strip()

# Example usage:
resume_content = """John Doe
Email: john.doe@example.com
Phone: 123-456-7890
Address: 123 Main St, Anytown, USA

Professional Summary:
Experienced software developer with expertise in AI and machine learning.

Work Experience:
Software Engineer at XYZ Corp
Location: Anytown, USA
Start Date: January 2020
End Date: Present
Responsibilities:
- Developed machine learning models
- Improved algorithm efficiency

Education:
Bachelor of Science in Computer Science
Anytown University
Location: Anytown, USA
Graduation Date: May 2019

Skills:
- Python
- Machine Learning

Certifications:
- Certified Machine Learning Specialist, AI Institute, June 2020

Projects:
- AI Chatbot
  Description: Developed an AI chatbot for customer service
  Technologies Used: Python, NLP

Languages:
- English
- Spanish

Hobbies:
- Hiking
- Reading
"""

parsed_json = parse_resume_to_json(resume_content)
print(parsed_json)
