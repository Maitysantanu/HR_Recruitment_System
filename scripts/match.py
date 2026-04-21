import pandas as pd
from modules.db import get_connection
from modules.matcher import match_candidates

job_desc = input("Enter Job Description:\n")

conn = get_connection()

query = "SELECT name, skills, resume_text FROM candidates"
df = pd.read_sql(query, conn)

top = match_candidates(job_desc, df)

print("\nTop 3 Candidates:\n")
print(top[['name', 'score']])

conn.close()