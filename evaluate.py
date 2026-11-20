"""Fixed fixture generator and independent, integer-arithmetic reading-time oracle."""
import random


def score(policy, seed, batches):
    rng = random.Random(seed)
    feasible = recovered = violations = excessive = total = 0
    for _ in range(batches):
        cues = []
        start = 0
        for _ in range(rng.randint(3, 16)):
            end = start + rng.randint(250, 1700)
            text = ("é " * rng.randrange(1, 36)).strip()
            cues.append((start, end, text))
            start = end + rng.randrange(0, 1200)
        result = policy(cues.copy(), start)
        if len(result) != len(cues):
            raise ValueError("One end required per cue")
        for i, ((a, b, text), value) in enumerate(zip(cues, result)):
            total += 1
            cap = min(b + 900, start if i+1 == len(cues) else max(b, cues[i+1][0]-80))
            chars = len("".join(text.split()))
            needs = chars*1000 > 17*(b-a)
            can_recover = needs and chars*1000 <= 17*(cap-a)
            feasible += can_recover
            recovered += can_recover and chars*1000 <= 17*(value-a)
            violations += type(value) is not int or not b <= value <= cap or (not needs and value != b)
            excessive += value > max(b, a + (chars*1000 + 16)//17)
    return dict(total=total, feasible=feasible, recovered=recovered, violations=violations,
                excess_extensions=excessive, passed=feasible>0 and recovered>=0.9*feasible and violations==0)
