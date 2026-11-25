"""Copy the pre-written entry into the output directory."""

import os
import shutil


def main():
    # The clause itself lives in entry.txt, written before this runs;
    # this program only carries it into the output folder unchanged.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
