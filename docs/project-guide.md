# Caption Clock
> Borrow silence for a subtitle.
## Shop for the project
A caption editor can change a timestamp in seconds. Deciding which timestamps to change takes judgment. Try playing two lines back to back and then two with a pause. Only the second pair offers free reading time. I chose this over automatic transcription because the text and onset times already give us small, inspectable inputs and an independent timing check.
## Start with something people already use
srt 3.5.3 parses the SubRip file and writes it back. The starting integration respects the source timings. The new policy changes only cue ends. It requires no speech model, audio upload or transcript rewriting. The distribution URL, exact version, digest and upstream license live in vendor/. The course application and its starting policy are new.
## Turn the tradeoff into a number
Recovery is the number of feasible fast cues made readable divided by the number of feasible fast cues. Report that denominator. Guard the original onset and wording in the integration, and bound each output end in the timing evaluator.
A line with 17 visible characters displayed for 500 ms needs 500 ms more. If the next line starts at 1,300 ms, its 80 ms gap leaves room. Move the end to 1,000 ms. With a next start at 510 ms, leave the end at 500 ms.
## Try it locally
Open the repository in Cursor. Use Python 3.11 or newer from its terminal. No package install, dataset download or model account is needed to run the example.
`python3 app.py sample.srt 2400`
The first cue lasts about one second instead of half a second. Its start and words survive the round trip. The second cue keeps its original interval.
## Cues recovered
Original 0 · Selected 79
---
# From objective to portfolio claim
## Write the contract first
A lecture caption editor wants to give viewers enough time to read without moving the start of a spoken line. Implement ends(cues, video_end) returning a list of integer end times in milliseconds. Each cue is (start_ms, end_ms, text), ordered, positive-duration, in-video, nonoverlapping. Count non-whitespace Unicode code points. Target at most 17 per second. You may extend an end by at most 900 ms, leaving at least 80 ms before the next start (for the last cue use video_end with no gap). If the original already has less gap, preserve it. Never shorten, move or change text. Recover at least 90% of initially fast cues that can reach the target under these limits. Keep already readable cues unchanged. Development example: [(0,500,'a'*17),(1300,1900,'ok')], video_end=2400 should produce [1000,1900].
## Plan with the model
A short silence can supply the missing reading time. Count the non-whitespace characters, compute the required integer duration, and clip the extension at the earliest of the three limits. Rewriting the text could alter meaning, and moving a start could break speech synchronization. A second design you could investigate follows.
Leave timing fixed and simplify long captions instead. You would need human checks for preserved meaning. Our score could never settle that question.
## Hand off one decision
In a clean copy of the starting policy, use Cursor Plan to name the edge case that could make a plausible patch fail. Save its reasoning as a short plan. Give a fresh Agent chat the objective, approved plan, editable function and a stopping budget. The experiment record links the exact inputs used here.
## Inspect the evidence
Among 379 reserved cues, 79 were initially too fast and had enough room to recover. The original recovered 0. The selected implementation recovered 79, violated 0 timing rules, and made 0 extensions past the needed duration. Plain runs passed 3/3, and plan-assisted runs passed 3/3. The unchanged application policy and the plain model are two different baselines.
`python3 verify.py` reproduces the saved outcomes. `python3 score.py` evaluates the selected candidate and exits 1 if it misses the target.
## Where the claim ends
Character count is a proxy for reading burden. Grapheme clusters, line breaks, learner proficiency and speech cadence can change the viewing experience. These fixtures contain generated text and gaps. Do not claim a measured improvement in comprehension. Use a rights-cleared talk and have editors rate a blinded sample of revised timings. Agree on an onset and overlap tolerance with an editor before asking the agent to optimize.
~ [Repository, source code and second PDF](https://github.com/PatrickAllenCooper/course-caption-clock)   |   [Machine-readable results](https://github.com/PatrickAllenCooper/course-caption-clock/blob/main/research/results.json)
