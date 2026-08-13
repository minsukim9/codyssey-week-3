from judge import judge_scores
from mac import calculate_mac


def analyze_pattern(pattern_data, filters):
    size_key = pattern_data["size_key"]
    pattern = pattern_data["input"]
    expected = pattern_data["expected"]

    filter_group = filters.get(size_key)

    if filter_group is None:
        return {
            "cross_score": None,
            "x_score": None,
            "result": None,
            "expected": expected,
            "passed": False,
            "reason": f"{size_key} 필터가 존재하지 않습니다."
        }

    cross_filter = filter_group.get("Cross")
    x_filter = filter_group.get("X")

    if cross_filter is None or x_filter is None:
        return {
            "cross_score": None,
            "x_score": None,
            "result": None,
            "expected": expected,
            "passed": False,
            "reason": "Cross 또는 X 필터가 존재하지 않습니다."
        }

    cross_score = calculate_mac(pattern, cross_filter)
    x_score = calculate_mac(pattern, x_filter)

    result = judge_scores(
        cross_score,
        x_score,
        "Cross",
        "X"
    )

    passed = result == expected

    reason = None

    if not passed:
        if result == "UNDECIDED":
            reason = "동점(UNDECIDED) 처리 규칙"
        else:
            reason = "판정 결과와 expected 불일치"

    return {
        "cross_score": cross_score,
        "x_score": x_score,
        "result": result,
        "expected": expected,
        "passed": passed,
        "reason": reason
    }


def analyze_patterns(patterns, filters):
    results = {}

    for pattern_key, pattern_data in patterns.items():
        results[pattern_key] = analyze_pattern(
            pattern_data,
            filters
        )

    return results
