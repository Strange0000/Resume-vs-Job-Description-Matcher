
import re

# Basic stopwords (you can expand this)
Basic_STOPWORDS = {
    "the", "is", "and", "in", "to", "of", "a", "for", "on", "with",
    "as", "by", "an", "be", "this", "that", "are", "it", "from"
}

def clean_txt(txt):
    txt = txt.lower()
    txt= re.sub(r'[^a-z0-9\s]', '', txt)  # remove punctuation
    words = txt.split()
    words = [word for word in words if word not in Basic_STOPWORDS]
    return words

def extract_keywords(txt):
    words = clean_txt(txt)
    return set(words)

def match_resume_to_job(resume, job_description):
    resume_keywords = extract_keywords(resume)
    job_keywords = extract_keywords(job_description)

    matched = resume_keywords.intersection(job_keywords)
    missing = job_keywords.difference(resume_keywords)

    if len(job_keywords) == 0:
        score = 0
    else:
        score = (len(matched) / len(job_keywords)) * 100

    return {
        "score": round(score, 2),
        "matched_keywords": list(matched),
        "missing_keywords": list(missing)
    }

# Example 
resume_text = """
Python developer with experience in machine learning, data analysis,
and building web applications using Flask and Django.
"""

job_description = """
Looking for a Python developer skilled in Django, REST APIs,
machine learning, and cloud deployment.
"""

result = match_resume_to_job(resume_text, job_description)

print("Matched Score:", result["score"])
print("Matched Keywords:", result["matched_keywords"])
print("Missing Keywords:", result["missing_keywords"])