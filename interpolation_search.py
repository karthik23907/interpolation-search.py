import random
import time


def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm

    Average Time Complexity: O(log log n)
    Worst Time Complexity: O(n)
    Space Complexity: O(1)

    Returns:
        (index, comparisons)
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        # Avoid division by zero
        if arr[high] == arr[low]:
            break

        # Estimate the probable position
        pos = low + (
            (target - arr[low]) * (high - low)
            // (arr[high] - arr[low])
        )

        comparisons += 1

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    """
    Binary Search Algorithm

    Time Complexity: O(log n)
    Space Complexity: O(1)

    Returns:
        (index, comparisons)
    """
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    """
    Compare the execution time and number of comparisons
    between Interpolation Search and Binary Search.
    """
    sizes = [1000, 5000, 10000, 50000, 100000]

    print(
        f"{'Size':>10} "
        f"{'IS Time(ms)':>14} "
        f"{'BS Time(ms)':>14} "
        f"{'IS Comparisons':>16} "
        f"{'BS Comparisons':>16}"
    )

    print("-" * 75)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        # Measure Interpolation Search
        start = time.perf_counter()

        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)

        is_time = (time.perf_counter() - start) / 100 * 1000

        # Measure Binary Search
        start = time.perf_counter()

        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)

        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(
            f"{size:>10} "
            f"{is_time:>14.4f} "
            f"{bs_time:>14.4f} "
            f"{comp_is:>16} "
            f"{comp_bs:>16}"
        )


def main():
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35

    index, comparisons = interpolation_search(arr, target)

    print("Interpolation Search Example")
    print("-" * 30)
    print(f"Array           : {arr}")
    print(f"Target          : {target}")
    print(f"Index Found     : {index}")
    print(f"Comparisons     : {comparisons}")

    print("\nPerformance Analysis")
    print("=" * 75)

    performance_analysis()


if __name__ == "__main__":
    main()