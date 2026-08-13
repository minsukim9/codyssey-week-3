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
