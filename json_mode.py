from json_handler import load_filters_and_patterns, normalize_filters
from pattern_handler import validate_patterns


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

    print()
    print("#---------------------------------------")
    print("# [2] 패턴 검증")
    print("#---------------------------------------")

    valid_patterns, errors = validate_patterns(patterns)

    for pattern_key, pattern_data in valid_patterns.items():
        print(
            f"✓ {pattern_key} 검증 완료 "
            f"(expected: {pattern_data['expected']})"
        )

    for pattern_key, reason in errors:
        print(f"✗ {pattern_key}: {reason}")