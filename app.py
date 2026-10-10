import re
import string
from collections import Counter

STOP_WORDS = {
    "the", "and", "for", "with", "this", "that", "from", "into", "your", "have", "will",
    "about", "through", "across", "using", "within", "their", "there", "been", "were", "over",
    "under", "more", "most", "such", "same", "also", "years", "year", "role", "team", "teams",
    "job", "support", "responsible", "including", "key", "work", "based", "related", "required",
    "experience", "knowledge", "strong", "proven", "ability", "able", "enable", "delivery",
    "focus", "skills", "demonstrated", "business", "process", "processes", "critical", "production",
    "enterprise", "platforms", "solutions", "systems"
}


def normalize_text(text: str) -> str:
    text = text.lower()
    text = text.replace("&", " and ")
    text = text.replace("/", " ")
    text = text.translate(str.maketrans(string.punctuation, " " * len(string.punctuation)))
    return " ".join(text.split())


def extract_keywords(text: str, min_len: int = 3, max_words: int = 40):
    tokens = normalize_text(text).split()
    filtered = []
    for token in tokens:
        if len(token) >= min_len and token not in STOP_WORDS:
            filtered.append(token)

    counts = Counter(filtered)
    ranked = [word for word, _ in counts.most_common(max_words)]
    return ranked


def compute_match_score(cv_text: str, jd_text: str):
    cv_keywords = set(extract_keywords(cv_text))
    jd_keywords = set(extract_keywords(jd_text))

    if not jd_keywords:
        return 0, [], []

    overlap = sorted(jd_keywords.intersection(cv_keywords))
    missing = sorted(jd_keywords - cv_keywords)

    percent = round((len(overlap) / len(jd_keywords)) * 100)
    return percent, overlap, missing


def build_tailored_summary(cv_text: str, jd_text: str):
    cv_keywords = set(extract_keywords(cv_text))
    jd_keywords = set(extract_keywords(jd_text))
    matches = sorted(jd_keywords.intersection(cv_keywords))

    if not matches:
        return (
            "Results from the CV and job description are not yet aligned. "
            "Consider adding more role-relevant experience, technologies, and achievements."
        )

    priority_terms = matches[:12]
    summary = (
        "Results-driven engineering leader with deep experience in "
        + ", ".join(priority_terms[:5])
        + ". Proven track record in leading high-availability environments, improving observability, reducing MTTR, and driving operational excellence across mission-critical platforms."
    )
    return summary


def build_skill_recommendations(cv_text: str, jd_text: str):
    cv_keywords = set(extract_keywords(cv_text))
    jd_keywords = set(extract_keywords(jd_text))
    overlap = sorted(jd_keywords.intersection(cv_keywords))
    missing = sorted(jd_keywords - cv_keywords)

    return {
        "matched": overlap[:20],
        "missing": missing[:20],
        "match_score": round((len(overlap) / len(jd_keywords)) * 100) if jd_keywords else 0,
    }
