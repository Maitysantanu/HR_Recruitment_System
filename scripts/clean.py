import pandas as pd
from modules.transform import clean_missing
from modules.skill_extractor import extract_skills

df = pd.read_csv("data/raw/resumes.csv")

# Clean missing
df = clean_missing(df)

# Extract skills automatically
df['skills'] = df['resume_text'].apply(lambda x: ", ".join(extract_skills(x)))

# Save processed file
df.to_csv("data/processed/cleaned_resumes.csv", index=False)

print("Data cleaned + skills extracted")