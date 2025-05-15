def make_pair_interval(lst: list) -> list:
    return [[lst[i], lst[i+1]] for i in range(0, len(lst), 2) if lst[i] < lst[i+1]]

def set_intervals_to_border(intervals: list, start_lesson: int, end_lesson: int) -> list:
    clipped = []
    for interval in intervals:
        start = max(interval[0], start_lesson)
        end = min(interval[1], end_lesson)
        if start < end:
            clipped.append([start, end])
    return clipped

def merge_intervals(intervals: list) -> list:
    if not intervals:
        return []

    intervals.sort()

    merged = [intervals[0]]

    for interval in intervals[1:]:
        prev = merged[-1]
        if interval[0] <= prev[1]:
            prev[1] = max(interval[1], prev[1])
        else:
            merged.append(interval)

    return merged

def merge_intervals_between(intervals1, intervals2):
    result = []
    i = j = 0
    while i < len(intervals1) and j < len(intervals2):
        a_start, a_end = intervals1[i]
        b_start, b_end = intervals2[j]

        start = max(a_start, b_start)
        end = min(a_end, b_end)
        if start < end:
            result.append([start, end])

        if a_end < b_end:
            i += 1
        else:
            j += 1
    return result

def total_time(intervals: list) -> int:
    return sum(end - start for start, end in intervals)

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_interval_raw = make_pair_interval(intervals['pupil'])
    tutor_interval_raw = make_pair_interval(intervals['tutor'])

    pupil_interval = set_intervals_to_border(pupil_interval_raw, lesson_start, lesson_end)
    tutor_interval = set_intervals_to_border(tutor_interval_raw, lesson_start, lesson_end)

    pupil_interval = merge_intervals(pupil_interval)
    tutor_interval = merge_intervals(tutor_interval)

    overlap = merge_intervals_between(pupil_interval, tutor_interval)

    return total_time(overlap)
