"""The 3AM Fridge Text - entry writer.

Reads entry.txt next to this file and writes it, byte for byte, to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is not set). One direct write, no temporary file, mode 0644.

The write is wrapped so a failure to create the output directory or
to write the file raises a clear error instead of failing silently.
"""

import os
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    data = (here / "entry.txt").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_path = out_dir / "entry.txt"
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        raise RuntimeError(f"failed to write {out_path}: {exc}") from exc


if __name__ == "__main__":
    main()
