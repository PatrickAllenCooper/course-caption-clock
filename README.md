# Caption Clock

Borrow silence for a subtitle. Among 379 reserved cues, 79 were initially too fast and had enough room to recover. The original recovered 0. The selected implementation recovered 79, violated 0 timing rules, and made 0 extensions past the needed duration.

[Project guide (PDF)](docs/project-guide.pdf) · [Experiment record (PDF)](docs/experiment-record.pdf) · [Every actual prompt and reply](runs/) · [Complete scores](research/results.json)

## Try it in Cursor’s terminal

Use Python 3.11+. No network, model key or dependency installation is required.

```sh
python3 app.py sample.srt 2400
python3 verify.py
python3 score.py
```

The last command exits 1 if the selected implementation misses the frozen target. The verification command succeeds when the recorded measurements reproduce, including a recorded miss.

## Study design

Three fresh plain model requests and three with a shared planning note. The examples use a bounded implementation protocol and synthetic inputs. Plain successes 3/3, assisted successes 3/3. See [the frozen contract](brain/objective.md), [selection protocol](brain/protocol.md), [upstream source and license](vendor/) and [recorded model runner](research/trials.py). The `study-start` tag fixes the starting code and evaluator. A fresh Cursor replication is described in the experiment record. For a new graded study choose a harder objective and reserve fresh cases.

## Contribution

The course materials and evaluation were prepared with AI assistance. The selected implementation is a saved foundation-model response. This repository adds a teaching application to a pinned external library. Character count is a proxy for reading burden. Grapheme clusters, line breaks, learner proficiency and speech cadence can change the viewing experience. These fixtures contain generated text and gaps. Do not claim a measured improvement in comprehension.
