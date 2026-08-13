import re

from json_handler import validate_matrix
from label import normalize_label

PATTERN_KEY = re.compile(r"^size_(\d+)_(\d+)$")


def extract_pattern_size(pattern_key):
    match = PATTERN_KEY.match(pattern_key)

    if match is None:
        return None

    return int(match.group(1))


def validate_patterns(patterns):
    valid_patterns = {}
    errors = []

    for pattern_key, pattern_data in patterns.items():
        size = extract_pattern_size(pattern_key)

        if size is None:
            errors.append(
                (pattern_key, "패턴 키 형식이 올바르지 않습니다.")
            )
            continue

        if not isinstance(pattern_data, dict):
            errors.append(
                (pattern_key, "패턴 데이터 형식이 올바르지 않습니다.")
            )
            continue

        pattern = pattern_data.get("input")
        expected = pattern_data.get("expected")

        if pattern is None:
            errors.append(
                (pattern_key, "input 데이터가 존재하지 않습니다.")
            )
            continue

        if expected is None:
            errors.append(
                (pattern_key, "expected 값이 존재하지 않습니다.")
            )
            continue

        if not validate_matrix(pattern, size):
            errors.append(
                (
                    pattern_key,
                    f"패턴 크기가 {size}x{size} 형식과 일치하지 않습니다."
                )
            )
            continue

        normalized_expected = normalize_label(expected)

        if normalized_expected is None:
            errors.append(
                (
                    pattern_key,
                    f"알 수 없는 expected 라벨입니다. ({expected})"
                )
            )
            continue

        valid_patterns[pattern_key] = {
            "size": size,
            "size_key": f"size_{size}",
            "input": pattern,
            "expected": normalized_expected
        }

    return valid_patterns, errors
