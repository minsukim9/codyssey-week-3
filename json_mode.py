from json_analyzer import analyze_patterns
from json_handler import load_filters_and_patterns, normalize_filters
from pattern_handler import validate_patterns
from performance import analyze_performance


def run_json_mode():
    filters, patterns = load_filters_and_patterns()

    if filters is None or patterns is None:
        return

    print()
    print("#---------------------------------------")
    print("# [1] 필터 로드")
    print("#---------------------------------------")

    normalized_filters = normalize_filters(filters)

    for size_key in ("size_5", "size_13", "size_25"):
        if size_key in normalized_filters:
            print(f"✓ {size_key} 필터 로드 완료 (Cross, X)")

    valid_patterns, errors = validate_patterns(patterns)

    print()
    print("#---------------------------------------")
    print("# [2] 패턴 분석 (라벨 정규화 적용)")
    print("#---------------------------------------")

    results = analyze_patterns(
        valid_patterns,
        normalized_filters
    )

    for pattern_key, result in results.items():
        print(f"--- {pattern_key} ---")
        print(f"Cross 점수: {result['cross_score']}")
        print(f"X 점수: {result['x_score']}")

        status = "PASS" if result["passed"] else "FAIL"

        if result["reason"] is None:
            print(
                f"판정: {result['result']} | "
                f"expected: {result['expected']} | "
                f"{status}"
            )
        else:
            print(
                f"판정: {result['result']} | "
                f"expected: {result['expected']} | "
                f"{status} ({result['reason']})"
            )

    for pattern_key, reason in errors:
        print(f"--- {pattern_key} ---")
        print(f"판정: FAIL ({reason})")

    print()
    print("#---------------------------------------")
    print("# [3] 성능 분석 (평균/10회)")
    print("#---------------------------------------")
    print("크기       평균 시간(ms)       연산 횟수")
    print("---------------------------------------")

    performance_results = analyze_performance(
        normalized_filters
    )

    for result in performance_results:
        size = result["size"]
        average_time = result["average_time"]
        operations = result["operations"]

        print(
            f"{size}x{size:<5} "
            f"{average_time:>12.6f} "
            f"{operations:>12}"
        )