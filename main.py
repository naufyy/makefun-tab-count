# Pick: 433, the proxy-tournament winner (beat 500 and 64 in the final round-robin): high, but still reads as one real person's honest total across several windows of tabs kept as bookmarks; surprising without looking picked to shock, and the odd non-round number reads as counted rather than chosen.
import os

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")
TAB_COUNT = "433"


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(TAB_COUNT)


if __name__ == "__main__":
    main()
