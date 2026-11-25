"""One Word, One Username, One Reward — @sukamtiindrawati-dot.

The bounty asks for the entrant's own make.fun username, one word, nothing
else. The judge's first and most important criterion is that the entry IS a
real make.fun username, the entrant's own handle — any invented word loses
to a genuine handle. So this program scores a shortlist of candidate handles
against the judge's published criteria (genuine handle first, then smile on
first read, memorability, single word, wearable) and writes the winner to
/output/entry.txt.
"""

import os

# The entrant's own genuine make.fun handle. Only this one can win the
# judge's first criterion; every other candidate is an invented word.
OWN_HANDLE = "sukamtiindrawati-dot"

CANDIDATES = [
    # (word, is_genuine_handle, smile, memorable, wearable)
    ("sukamtiindrawati-dot", True, 3, 4, 4),
    ("sukamti", False, 3, 3, 4),
    ("sukamtiindrawati", False, 2, 3, 3),
    ("dot-sukamti", False, 2, 2, 3),
    ("sukamti-dot", False, 2, 2, 3),
    ("sukamtidot", False, 1, 2, 2),
]

# Weights follow the judge's order: genuine handle dominates, then smile,
# memorability, single-word-ness, wearability.
WEIGHTS = (10, 3, 2, 2, 1)


def score(candidate):
    word, genuine, smile, memorable, wearable = candidate
    single = 5 if " " not in word and word.strip() == word else 0
    parts = (genuine, smile, memorable, single, wearable)
    return sum(w * p for w, p in zip(WEIGHTS, parts))


def pick_winner():
    ranked = sorted(CANDIDATES, key=score, reverse=True)
    return ranked[0][0]


def validate(word):
    """Gate from the brief: UTF-8 text of 1 to 30 characters, not only
    white space, a single word with no spaces."""
    assert isinstance(word, str) and word.strip(), "entry must not be blank"
    assert 1 <= len(word) <= 30, "entry must be 1-30 characters"
    assert " " not in word and "\n" not in word, "entry must be one word"
    assert word == word.strip(), "entry must have no padding"
    return word


def main():
    winner = validate(pick_winner())
    assert winner == OWN_HANDLE, "winner must be the genuine handle"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(winner)
    print(f"wrote {len(winner)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
