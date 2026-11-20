"""Retiming for a sorted, non-overlapping UTF-8 SRT subtitle track."""
from datetime import timedelta
from pathlib import Path
import argparse
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "vendor"))
import srt
from candidate import ends


def retime(text, video_end):
    track = list(srt.parse(text))
    zero = timedelta()
    unit = timedelta(milliseconds=1)
    cues = [(c.start // unit, c.end // unit, c.content) for c in track]
    if video_end < 0 or any(a < 0 or a >= b or b > video_end or
                            (i and a < cues[i - 1][1])
                            for i, (a, b, _) in enumerate(cues)):
        raise ValueError("Expected an ordered, nonoverlapping track within video duration")
    for caption, end in zip(track, ends(cues, video_end), strict=True):
        caption.end = zero + end * unit
    return srt.compose(track, reindex=False, strict=False)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("file", type=Path)
    cli.add_argument("video_end_ms", type=int)
    args = cli.parse_args()
    print(retime(args.file.read_text(encoding="utf8"), args.video_end_ms), end="")
