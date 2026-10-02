"""Copy a locally obtained licensed CSV into data/raw."""
import argparse
from pathlib import Path
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("--source-path", type=Path)
args = parser.parse_args()
target = Path(__file__).resolve().parents[1] / "data/raw"
target.mkdir(parents=True, exist_ok=True)
if args.source_path:
    shutil.copy2(args.source_path, target / args.source_path.name)
    print(f"Copied licensed local source to {target / args.source_path.name}")
else:
    print("No download performed. See data/README.md for the licensed source workflow.")
