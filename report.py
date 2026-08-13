def summarize_results(results, errors):
    total_count = len(results) + len(errors)

    pass_count = 0
    failure_cases = []

    for pattern_key, result in results.items():
        if result["passed"]:
            pass_count += 1
        else:
            failure_cases.append(
                (pattern_key, result["reason"])
            )

    for pattern_key, reason in errors:
        failure_cases.append(
            (pattern_key, reason)
        )

    fail_count = len(failure_cases)

    return {
        "total": total_count,
        "passed": pass_count,
        "failed": fail_count,
        "failure_cases": failure_cases
    }


def print_summary(summary):
    print()
    print("#---------------------------------------")
    print("# [4] 결과 요약")
    print("#---------------------------------------")
    print(f"총 테스트: {summary['total']}개")
    print(f"통과: {summary['passed']}개")
    print(f"실패: {summary['failed']}개")

    if summary["failure_cases"]:
        print()
        print("실패 케이스:")

        for pattern_key, reason in summary["failure_cases"]:
            print(f"- {pattern_key}: {reason}")
