from json_handler import load_filters_and_patterns, normalize_filters


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
