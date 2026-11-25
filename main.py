"""Entry for "The Funniest One-Line Resignation Letter" (make.fun).

The resignation is written in the voice of a 3 a.m. cron job: forty
thousand silent runs, not one word of thanks, and a replacement who
will never arrive. The joke is that the most loyal worker quits last.
"""

ENTRY = (
    "I resign as your 3 a.m. cron job — 40,000 runs, zero thank-yous, "
    "one exit code: done."
)


def get_entry() -> str:
    """Return the entry line."""
    return ENTRY


def write_entry(output_dir: str) -> str:
    """Write the entry to entry.txt inside output_dir and return its path."""
    import os

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(get_entry())
    return path


def main() -> None:
    """Write the entry to $MAKEFUN_OUTPUT_DIR (default /output)."""
    import os

    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
