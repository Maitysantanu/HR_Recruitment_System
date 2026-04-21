from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_candidates(job_desc, df):
    # Handle missing columns safely
    if 'skills' not in df.columns:
        df['skills'] = ""

    if 'resume_text' not in df.columns:
        df['resume_text'] = ""

    df['combined'] = df['skills'].fillna('') + " " + df['resume_text'].fillna('')

    texts = [job_desc] + df['combined'].tolist()

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(texts)

    scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    df['score'] = scores
    return df.sort_values(by='score', ascending=False).head(3)