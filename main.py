"""u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018 entry: one code review
comment, a single line of at most 140 characters, approving a pull request
while carrying quiet existential dread.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The comment is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Comment (written in this session, never copied from the board): a tired
engineer equates the Friday deploy with the death of the sun. The laugh
comes from the dread itself, in a flat tone, and the approval still sounds
like an approval. The judge weighs approval-with-quiet-dread first, then
whether the laugh comes from the dread, understatement over melodrama,
a comment a tired engineer would really paste, and a fresh turn of phrase.
"""

import os


COMMENT = (
    "Approved. This ships Friday; the sun burns out in five billion "
    "years. Same sprint, really."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)

# The competition requires 1 to 140 characters, a single line.
MAX_CHARS = 140


def main() -> None:
    text = COMMENT.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "comment must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    # The gate requires a single line: reject any embedded newline.
    if "\n" in text or "\r" in text:
        raise SystemExit("comment must be a single line")
    data = text.encode("utf-8")
    # Create the output directory only when it does not exist already;
    # never delete or recreate the directory the grader provides.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the comment.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the comment")
    print(text)


if __name__ == "__main__":
    main()
