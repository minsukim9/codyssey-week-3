from input_mode import run_input_mode
from json_handler import load_filters_and_patterns


def run_menu():
    print("=== Mini NPU Simulator ===")
    print()
    print("[모드 선택]")
    print()
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")

    mode = input("선택: ")

    if mode == "1":
        run_input_mode()

    elif mode == "2":
        filters, patterns = load_filters_and_patterns()

        if filters is not None and patterns is not None:
            print("data.json 로드 완료")
            print(f"필터 크기 종류: {len(filters)}개")
            print(f"패턴: {len(patterns)}개")

    else:
        print("잘못된 입력입니다.")
