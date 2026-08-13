from judge import judge_scores
from mac import calculate_mac
from performance import measure_mac


SIZE = 3


def input_matrix(name):
    while True:
        matrix = []

        print(f"{name} ({SIZE}줄 입력, 공백 구분)")

        try:
            for _ in range(SIZE):
                row = list(map(float, input().split()))

                if len(row) != SIZE:
                    raise ValueError

                matrix.append(row)

            return matrix

        except ValueError:
            print(
                "입력 형식 오류: "
                "각 줄에 3개의 숫자를 공백으로 구분해 입력하세요."
            )
            print()


def run_input_mode():
    print()
    print("#---------------------------------------")
    print("# [1] 필터 입력")
    print("#---------------------------------------")

    filter_a = input_matrix("필터 A")
    print("필터 A 저장 완료")
    print()

    filter_b = input_matrix("필터 B")
    print("필터 B 저장 완료")
    print()

    print("#---------------------------------------")
    print("# [2] 패턴 입력")
    print("#---------------------------------------")

    pattern = input_matrix("패턴")
    print("패턴 저장 완료")
    print()

    score_a = calculate_mac(pattern, filter_a)
    score_b = calculate_mac(pattern, filter_b)

    result = judge_scores(score_a, score_b)

    time_a = measure_mac(pattern, filter_a)
    time_b = measure_mac(pattern, filter_b)
    average_time = (time_a + time_b) / 2

    print("#---------------------------------------")
    print("# [3] MAC 결과")
    print("#---------------------------------------")
    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(f"연산 시간(평균/10회): {average_time:.6f} ms")

    if result == "UNDECIDED":
        print("판정: 판정 불가 (|A-B| < 1e-9)")
    else:
        print(f"판정: {result}")