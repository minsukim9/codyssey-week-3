def main():
    print("=== Mini NPU Simulator ===")
    print()
    print("[모드 선택]")
    print()
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")

    mode = input("선택: ")

    if mode == "1":
        print("사용자 입력 모드를 선택했습니다.")
    elif mode == "2":
        print("data.json 분석 모드를 선택했습니다.")
    else:
        print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()
