import pandas as pd
from modules.db import get_connection, create_table

# Create table automatically
create_table()

conn = get_connection()
cursor = conn.cursor()

df = pd.read_csv("data/processed/cleaned_resumes.csv")

for _, row in df.iterrows():
    query = """
    INSERT INTO candidates (name, email, skills, experience, education, resume_text)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        row['name'],
        row['email'],
        row['skills'],
        row['experience'],
        row['education'],
        row['resume_text']
    )
    cursor.execute(query, values)

conn.commit()
cursor.close()
conn.close()

print("Data loaded into MySQL")