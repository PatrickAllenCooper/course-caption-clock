# Caption Clock experiment record
> The chain from a prompt to a patch to an independent decision.
## What was fixed before the runs
Study start ff89e4996f5b. The same task, example, starting function, requested model and 100-second implementation limit applied to all six runs. One extra planning call supplied the same note to the three assisted runs. Plain then assisted ran in each pair. One candidate per fresh chat. The author specified the policy interface, scorer and budget and supplied no mid-run coaching.
## What the model saw
Only the public task, original function and output instruction were delivered to the model. The assisted arm also received its saved plan. The scorer and final inputs stayed outside every implementation prompt. These are bounded text-in/code-out calls with a deterministic harness. Our authenticated Codex CLI supplied gpt-6.1-sol at low reasoning effort. The recorded trials did not run in Cursor. The same prompts can be used in Cursor.
## Read every prompt and response
[Open the prompt archive](https://github.com/PatrickAllenCooper/course-caption-clock/tree/main/runs). Start at 00-plan. Open prompt.txt for the exact request, reply.txt for the public response, call.json for elapsed seconds and reported usage. Each of the six implementation directories also preserves the extracted candidate.py. No follow-up prompts were issued. All decisions used the same base function. No gold answers or final scores were fed back.
## What planning added
> - User constraint: Extend only initially fast cues, preserving starts and text and never shortening ends. Limit extensions to 900 ms and preserve an 80 ms gap before the next start, or the original gap if smaller. Use video_end as the last cue’s boundary. Leave readable cues unchanged. - Design hypothesis: Count non-whitespace Unicode code points. Compute the required duration by rounding up count × 1000 / 17 milliseconds. Extend fast cues to that duration when permitted; otherwise extend to their allowed limit. - Edge case: If the original gap is below 80 ms, the cue cannot extend. Empty or whitespace-only text remains unchanged. - Stopping check: Verify every constraint, the example’s [1000,1900], and recovery of at least 90% of initially fast, feasible cues; this design should recover all feasible cues.
The planning call took 7.3 seconds, shared across three assisted attempts. Its cost is separate from the implementation figures. Provider billing per call was unavailable. No student credentials are needed to rescore.
---
# What actually changed
## Starting policy
> def ends(cues, video_end): return [end for start, end, text in cues]
## Selected change
The selected function counts characters and uses integer ceiling division to compute the required duration. It leaves readable cues alone and clips an extension against the next cue or video end. Read the complete [selected source](https://github.com/PatrickAllenCooper/course-caption-clock/blob/main/candidate.py) and compare it to [the original policy](https://github.com/PatrickAllenCooper/course-caption-clock/blob/main/baseline.py). The harness copied the selected model output verbatim after stripping any Markdown fence. The application, evaluator, dataset generation and package version stayed fixed through candidate selection.
## Why this particular candidate
We selected the earliest assisted candidate that passed development, then would have tried the earliest plain pass. All six generated modules were frozen at 68be9fb150ca before the final panel ran. The selected run was 01-assisted. Among 379 reserved cues, 79 were initially too fast and had enough room to recover. The original recovered 0. The selected implementation recovered 79, violated 0 timing rules, and made 0 extensions past the needed duration.
## Every implementation trial
| Run | Seconds | Dev cues recovered | Final cues recovered | Verdict |
| --- | ---: | ---: | ---: | --- |
| 01-plain | 7.7 | 30 | 79 | PASS |
| 01-assisted | 6.9 | 30 | 79 | PASS |
| 02-plain | 6.8 | 30 | 79 | PASS |
| 02-assisted | 7.5 | 30 | 79 | PASS |
| 03-plain | 7.5 | 30 | 79 | PASS |
| 03-assisted | 8.2 | 30 | 79 | PASS |
## What the repetitions establish
The plain agent met the final target 3 times in three attempts. The assisted agent met it 3 times in three attempts. Input cases measure behavior; six calls are the units for comparing agents. The fixed order and single shared planning note limit any claim about planning in general. See [all scores and usage](https://github.com/PatrickAllenCooper/course-caption-clock/blob/main/research/results.json).
---
# Reproduce or extend the study
## Score a saved result
From the repo root, run `python3 verify.py`. This exercises a hand-checked example, compares the original and selected policies and replays all six development and final scores. To inspect one candidate independently run `python3 score.py runs/01-plain/candidate.py`. A failed target returns exit status 1 even when all checks ran as designed.
## Repeat one trial in Cursor
Make a new folder outside the published repository and open it in Cursor. Copy only baseline.py as candidate.py and the chosen run’s prompt.txt. Use a fresh chat and record the selected model, mode, date and time limit. Paste the full prompt. Save the returned module as candidate.py. Close the chat, copy that candidate back under a new name, and score it from the original repo. For a matched repeat, use identical settings and choose 01-plain or 01-assisted. Record provider differences. For a different model or native Cursor tools, label the result as a new condition.
## Use Plan and Goal for a larger project
In Plan mode ask for two designs and one cheap observation that would choose between them. Edit and save the plan. In Agent, or /goal in a Cursor CLI version that offers it, supply the measurable outcome, constraints, time and stop rule. Ask for a diff, development evidence and what remains unverified. Keep final evaluation under your control. These are instructions for extending this study. The six recorded implementation calls used a one-response budget.
## Reproduce the original runner
The optional `python3 research/trials.py NEW_RUN_DIR` uses the authenticated Codex CLI, the pinned model alias, and seven new calls; a provider subscription or access can be required. A free Cursor model is sufficient to study the method. All saved scoring works offline.
## A credible next claim
Use a rights-cleared talk and have editors rate a blinded sample of revised timings. Agree on an onset and overlap tolerance with an editor before asking the agent to optimize. Before a new campaign, freeze fresh cases and move the evaluator outside the editable workspace. The public evidence here is available for inspection by anyone. Prior exposure removes its value as a blind test.
