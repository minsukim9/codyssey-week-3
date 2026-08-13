import json

from label import normalize_label


DATA_FILE = "data.json"
FILTER_SIZES = (5, 13, 25)


def load_json_data(file_path=DATA_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"파일 오류: {file_path}을 찾을 수 없습니다.")

    except json.JSONDecodeError:
        print(f"파일 오류: {file_path}의 JSON 형식이 올바르지 않습니다.")

    return None


def load_filters_and_patterns(file_path=DATA_FILE):
    data = load_json_data(file_path)

    if data is None:
        return None, None

    if not isinstance(data, dict):
        print("스키마 오류: JSON 최상위 데이터는 객체 형식이어야 합니다.")
        return None, None

    filters = data.get("filters")
    patterns = data.get("patterns")

    if filters is None or patterns is None:
        print("스키마 오류: filters 또는 patterns가 존재하지 않습니다.")
        return None, None

    if not isinstance(filters, dict):
        print("스키마 오류: filters는 객체 형식이어야 합니다.")
        return None, None

    if not isinstance(patterns, dict):
        print("스키마 오류: patterns는 객체 형식이어야 합니다.")
        return None, None

    return filters, patterns


def validate_matrix(matrix, size):
    if not isinstance(matrix, list) or len(matrix) != size:
        return False

    for row in matrix:
        if not isinstance(row, list) or len(row) != size:
            return False

        for value in row:
            if not isinstance(value, (int, float)):
                return False

    return True


def normalize_filters(filters):
    normalized_filters = {}

    for size in FILTER_SIZES:
        size_key = f"size_{size}"
        filter_group = filters.get(size_key)

        if not isinstance(filter_group, dict):
            print(f"스키마 오류: {size_key} 필터가 존재하지 않거나 형식이 올바르지 않습니다.")
            continue

        normalized_group = {}

        for filter_key, matrix in filter_group.items():
            label = normalize_label(filter_key)

            if label is None:
                print(
                    f"스키마 오류: {size_key}의 "
                    f"알 수 없는 필터 라벨입니다. ({filter_key})"
                )
                continue

            if not validate_matrix(matrix, size):
                print(
                    f"스키마 오류: {size_key}의 "
                    f"{filter_key} 필터 크기 또는 데이터 형식이 올바르지 않습니다."
                )
                continue

            normalized_group[label] = matrix

        if "Cross" not in normalized_group or "X" not in normalized_group:
            print(
                f"스키마 오류: {size_key}에 "
                "정상적인 Cross 또는 X 필터가 없습니다."
            )
            continue

        normalized_filters[size_key] = normalized_group

    return normalized_filters