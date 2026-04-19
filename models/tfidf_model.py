from sklearn.feature_extraction.text import TfidfVectorizer

def compute_similarity(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume,jd])

    similarity = (vectors * vectors.T).toarray()[0,1]
    return similarity * 100