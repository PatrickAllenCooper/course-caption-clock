def ends(cues, video_end):
    result = []
    for i, (start, end, text) in enumerate(cues):
        count = sum(not char.isspace() for char in text)
        required_duration = (count * 1000 + 16) // 17
        if required_duration <= end - start:
            result.append(end)
            continue

        boundary = cues[i + 1][0] - 80 if i + 1 < len(cues) else video_end
        latest = max(end, min(end + 900, boundary))
        result.append(min(start + required_duration, latest))
    return result
