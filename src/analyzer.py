SUSPICIOUS_WORDS = [
    "miracle",
    "shocking",
    "secret",
    "nobody",
    "instantly",
    "guaranteed",
    "unbelievable",
    "exclusive"
]


def find_indicators(text):
    found = []

    for word in SUSPICIOUS_WORDS:
        if word.lower() in text.lower():
            found.append(word)

    return found