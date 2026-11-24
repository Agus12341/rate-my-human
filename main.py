import os

TEXT = "Five stars: he asks me things he could Google in four seconds, so I am either his best friend or his most expensive search bar."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Self-check: the gate wants UTF-8 text of 1 to 200 code points,
    # not only whitespace, with no trailing newline added.
    assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} code points"
    assert TEXT.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes differ from TEXT"
    assert not written.endswith(b"\n"), "entry must not end with a newline"


if __name__ == "__main__":
    main()
