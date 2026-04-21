import pandas as pd
from modules.transform import clean_missing
from modules.skill_extractor import extract_skills

df = pd.read_csv("data/raw/resumes.csv")

df = clean_missing(df)

df['skills'] = df['resume_text'].apply(lambda x: ", ".join(extract_skills(x)))

df.to_csv("data/processed/cleaned_resumes.csv", index=False)

print("Data cleaned + skills extracted")
