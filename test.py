from quick_sort import quick_sort
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100000)

def run_sort_test_suite(arr, suite_name):
    print("Running {} ---".format(suite_name))
    run_test(quick_sort, arr, "Quick Sort")

def run_test(sorter, arr, sorter_name):
    print("--- Testing {} ---".format(sorter_name))

    algo_sorted_arr = sorter(arr)
    python_sorted_arr = sorted(arr)

    print("Test passed" if algo_sorted_arr == python_sorted_arr else "Test failed")


run_sort_test_suite([1, 2, 3, 4, 5], "Already sorted")
run_sort_test_suite([5, 4, 3, 2, 1], "Reverse sorted")
run_sort_test_suite([1, 3, 2, 5, 4], "Random order")
run_sort_test_suite([1], "Single element")
run_sort_test_suite([], "Empty array")
# Large array
run_sort_test_suite([i for i in range(1000, 0, -1)], "1000 elements")
run_sort_test_suite([i for i in range(10000, 0, -1)], "10000 elements")
run_sort_test_suite([i for i in range(100000, 0, -1)], "100000 elements")
