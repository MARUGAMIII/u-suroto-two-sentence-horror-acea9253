"""Two-sentence horror entry.

Writes one horror story of exactly two sentences to /output/entry.txt.
The gate: UTF-8 text, 1-400 characters, not only whitespace.
"""

STORY = (
    "Every morning I find one of my shoes untied, and I always assumed "
    "I was forgetting to tie it. Last night I tied both shoes in a double "
    "knot before bed, and this morning one of them was tied in a neat "
    "little bow I never learned to make."
)


def main():
    text = STORY.strip()
    # Gate self-check: mirror the sealed scorer (1-400 chars, not only
    # whitespace, plain ASCII, exactly two sentences) so we never write
    # an invalid entry.
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert text.count(".") == 2, "entry must be exactly two sentences"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
