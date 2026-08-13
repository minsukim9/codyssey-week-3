import time

from mac import calculate_mac


DEFAULT_REPEAT = 10


def measure_mac(pattern, filter_data, repeat=DEFAULT_REPEAT):
    total_time = 0.0

    for _ in range(repeat):
        start = time.perf_counter()

        calculate_mac(pattern, filter_data)

        end = time.perf_counter()

        total_time += end - start

    average_time = total_time / repeat

    return average_time * 1000


def analyze_performance(filters):
    results = []

    cross_3 = [
        [0.0, 1.0, 0.0],
        [1.0, 1.0, 1.0],
        [0.0, 1.0, 0.0]
    ]

    average_time = measure_mac(cross_3, cross_3)

    results.append({
        "size": 3,
        "average_time": average_time,
        "operations": 3 * 3
    })

    for size in (5, 13, 25):
        size_key = f"size_{size}"

        if size_key not in filters:
            continue

        cross_filter = filters[size_key]["Cross"]

        average_time = measure_mac(
            cross_filter,
            cross_filter
        )

        results.append({
            "size": size,
            "average_time": average_time,
            "operations": size * size
        })

    return results