def keyword_match(resume, jd):

    resume_words = set(resume.split())
    jd_words = set(jd.split())

    match = resume_words.intersection(jd_words)
    score = len(match) / len(jd_words) * 100

    missing = jd_words - resume_words

    return score, missing