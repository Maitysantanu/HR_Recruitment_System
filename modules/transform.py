def clean_missing(df):
    df['email'] = df['email'].fillna("unknown@gmail.com")
    df['experience'] = df['experience'].fillna(0)
    return df