#!/usr/bin/env python3
"""Takes quick one-liner notes from the command line."""

#stand lib
import argparse as ap

#cutom
from constants import HOME

save_file = HOME+"Desktop/QuickNotes.txt"

if __name__ == "__main__":
    parser = ap.ArgumentParser(description="Take quick notes from command line.")
    parser.add_argument("note", nargs="+", help="Saves a note.")

    args = parser.parse_args()


    if args:
        with open(save_file, "a+") as f:
            f.write(" ".join(args.note))
            f.write("\n")
    else:
        print("No note was saved.")
    
    parser.exit(status=0, message="Note saved.\n")
