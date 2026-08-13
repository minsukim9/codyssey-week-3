import json

DATA_FILE = "data.json"


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

    filters = data.get("filters")
    patterns = data.get("patterns")

    if filters is None or patterns is None:
        print("스키마 오류: filters 또는 patterns가 존재하지 않습니다.")
        return None, None

    return filters, patterns
