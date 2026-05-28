import time
import random
import csv
import platform
import os


# ─────────────────────────────────────────────
# TASK 1: ALGORITHM IMPLEMENTATIONS
# ─────────────────────────────────────────────

# --- Search Algorithms ---

def linear_search(arr, target):
    """O(n) - checks each element one by one"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    """O(log n) - requires sorted array, divides search space in half"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# --- Sorting Algorithms ---

def bubble_sort(arr):
    """O(n²) - repeatedly swaps adjacent elements if out of order"""
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr):
    """O(n²) - finds minimum element and places it at beginning"""
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr):
    """O(n²) worst, O(n) best - inserts each element into correct position"""
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    """O(n log n) - divides array, sorts halves, then merges"""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]);
            i += 1
        else:
            result.append(right[j]);
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """O(n log n) average, O(n²) worst - partitions around pivot"""
    a = arr[:]
    _quick_sort_helper(a, 0, len(a) - 1)
    return a


def _quick_sort_helper(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)


def _partition(arr, low, high):
    # Median-of-three pivot to reduce worst-case probability
    mid = (low + high) // 2
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] < arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ─────────────────────────────────────────────
# TASK 3: MEASUREMENT PROTOCOL
# ─────────────────────────────────────────────

def measure(func, *args, runs=5):
    """Run function 'runs' times and return mean execution time in milliseconds"""
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        times.append(end - start)
    return (sum(times) / len(times)) * 1000  # convert to milliseconds


# ─────────────────────────────────────────────
# TASK 2: INPUT DESIGN
# ─────────────────────────────────────────────

SIZES = [100, 500, 1000, 2000, 5000, 10000]
RUNS = 5


def generate_inputs(n):
    random_list = random.sample(range(n * 10), n)
    sorted_list = list(range(n))
    reverse_list = list(range(n, 0, -1))
    return random_list, sorted_list, reverse_list


# ─────────────────────────────────────────────
# TASK 4 / TASK 5: RUN BENCHMARK & RECORD DATA
# ─────────────────────────────────────────────

def run_benchmark():
    results = []

    print("=" * 60)
    print("  ALGORITHM BENCHMARK - Assignment 1")
    print("=" * 60)

    for n in SIZES:
        print(f"\n[n = {n}]")
        rand_list, sorted_list, rev_list = generate_inputs(n)
        target = rand_list[n // 2]  # search target (guaranteed to exist)
        sorted_target = sorted_list[n // 2]

        # ── Search ──
        t = measure(linear_search, rand_list, target, runs=RUNS)
        print(f"  Linear Search (random):     {t:.6f} ms")
        results.append({"algorithm": "Linear Search", "condition": "random", "n": n, "time_ms": round(t, 6)})

        t = measure(linear_search, sorted_list, sorted_target, runs=RUNS)
        results.append({"algorithm": "Linear Search", "condition": "sorted", "n": n, "time_ms": round(t, 6)})

        t = measure(binary_search, sorted_list, sorted_target, runs=RUNS)
        print(f"  Binary Search (sorted):     {t:.6f} ms")
        results.append({"algorithm": "Binary Search", "condition": "sorted", "n": n, "time_ms": round(t, 6)})

        # ── O(n²) Sorts ──
        t = measure(bubble_sort, rand_list, runs=RUNS)
        print(f"  Bubble Sort   (random):     {t:.6f} ms")
        results.append({"algorithm": "Bubble Sort", "condition": "random", "n": n, "time_ms": round(t, 6)})

        t = measure(bubble_sort, rev_list, runs=RUNS)
        results.append({"algorithm": "Bubble Sort", "condition": "reverse", "n": n, "time_ms": round(t, 6)})

        t = measure(selection_sort, rand_list, runs=RUNS)
        print(f"  Selection Sort(random):     {t:.6f} ms")
        results.append({"algorithm": "Selection Sort", "condition": "random", "n": n, "time_ms": round(t, 6)})

        t = measure(insertion_sort, rand_list, runs=RUNS)
        print(f"  Insertion Sort(random):     {t:.6f} ms")
        results.append({"algorithm": "Insertion Sort", "condition": "random", "n": n, "time_ms": round(t, 6)})

        t = measure(insertion_sort, sorted_list, runs=RUNS)
        print(f"  Insertion Sort(sorted):     {t:.6f} ms")
        results.append({"algorithm": "Insertion Sort", "condition": "sorted", "n": n, "time_ms": round(t, 6)})

        t = measure(insertion_sort, rev_list, runs=RUNS)
        print(f"  Insertion Sort(reverse):    {t:.6f} ms")
        results.append({"algorithm": "Insertion Sort", "condition": "reverse", "n": n, "time_ms": round(t, 6)})

        # ── O(n log n) Sorts ──
        t = measure(merge_sort, rand_list, runs=RUNS)
        print(f"  Merge Sort    (random):     {t:.6f} ms")
        results.append({"algorithm": "Merge Sort", "condition": "random", "n": n, "time_ms": round(t, 6)})

        t = measure(merge_sort, rev_list, runs=RUNS)
        results.append({"algorithm": "Merge Sort", "condition": "reverse", "n": n, "time_ms": round(t, 6)})

        t = measure(quick_sort, rand_list, runs=RUNS)
        print(f"  Quick Sort    (random):     {t:.6f} ms")
        results.append({"algorithm": "Quick Sort", "condition": "random", "n": n, "time_ms": round(t, 6)})

        t = measure(quick_sort, rev_list, runs=RUNS)
        results.append({"algorithm": "Quick Sort", "condition": "reverse", "n": n, "time_ms": round(t, 6)})

    return results


def save_results(results, filename="results_MachineA.csv"):
    keys = ["algorithm", "condition", "n", "time_ms"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)
    print(f"\n✅ Results saved to: {filename}")


# ─────────────────────────────────────────────
# TASK 4: HARDWARE SPECS (auto-detect)
# ─────────────────────────────────────────────

def save_hardware_specs(filename="hardware_specs.txt"):
    import sys
    lines = [
        "=" * 50,
        "  MACHINE HARDWARE SPECIFICATIONS",
        "=" * 50,
        f"Machine Label  : Machine A  (change to B on second computer)",
        f"OS             : {platform.system()} {platform.release()} ({platform.version()})",
        f"Python Version : {sys.version}",
        f"Processor      : {platform.processor()}",
        f"Architecture   : {platform.machine()}",
        "",
        "--- Fill in manually ---",
        "CPU Model      : ",
        "Clock Speed    : GHz",
        "Number of Cores: ",
        "RAM Size       : GB",
        "Storage Type   : SSD / HDD",
        "=" * 50,
    ]
    with open(filename, "w") as f:
        f.write("\n".join(lines))
    print(f"✅ Hardware specs template saved to: {filename}")
    print("   → Please fill in CPU model, clock speed, cores, RAM, storage manually.")


if __name__ == "__main__":
    save_hardware_specs()
    results = run_benchmark()
    save_results(results)
    print("\nDone! Now copy both files to your report folder.")
    print("On Machine B, rename the CSV to: results_MachineB.csv")
