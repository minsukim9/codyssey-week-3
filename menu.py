from mac import calculate_mac


def run_menu():
    print("=== Mini NPU Simulator ===")
    print()
    print("[모드 선택]")
    print()
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")

    mode = input("선택: ")

    if mode == "1":
        cross_filter = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]

        x_filter = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]

        pattern = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]

        cross_score = calculate_mac(pattern, cross_filter)
        x_score = calculate_mac(pattern, x_filter)

        print(f"Cross 점수: {cross_score}")
        print(f"X 점수: {x_score}")

    elif mode == "2":
        print("data.json 분석 모드를 선택했습니다.")

    else:
        print("잘못된 입력입니다.")
