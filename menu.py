from input_mode import run_input_mode
from json_mode import run_json_mode


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
        run_json_mode()

    else:
        print("잘못된 입력입니다.")
