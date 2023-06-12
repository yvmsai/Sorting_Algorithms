import random
import time
import sys
sys.setrecursionlimit(10 ** 8)
from Self_Tuning_Sort import split_array
from sorting_algorithms import Algorithm
import pandas as pd


def random_array_generation(input_size):
    """ For generating random array of elements with given length """

    population = range(input_size * -1, input_size)
    random_list = random.sample(population, input_size)

    return random_list

def run_algorithms(input_array, input_size):
    """ For triggering all algorithms and for returning the elapsed time taken by each algorithm """

    current_size_time = []
    current_size_time.append(input_size)

    # 1 - Self Tuning Sort
    start_time = time.time()
    split_elements = split_array(input_array)
    self_sort_array = sort_split_arrays(split_elements, input_array)
    end_time = time.time()
    current_size_time.append(end_time - start_time)

    # 2 - Selection Sort
    start_time = time.time()
    selection_sort_array = Algorithm.selection_sort(input_array.copy())
    end_time = time.time()
    current_size_time.append(end_time - start_time)

    # 3 - Bubble Sort
    start_time = time.time()
    bubble_sort_array = Algorithm.bubble_sort(input_array.copy())
    end_time = time.time()
    current_size_time.append(end_time - start_time)

    # 4 - Insertion Sort
    start_time = time.time()
    insertion_sort_array = Algorithm.insertion_sort(input_array.copy())
    end_time = time.time()
    current_size_time.append(end_time - start_time)

    # 5 - Shell Sort
    start_time = time.time()
    shell_sort_array = Algorithm.shell_sort(input_array.copy())
    end_time = time.time()
    current_size_time.append(end_time - start_time)

    # 6 - Quick Sort
    start_time = time.time()
    quick_sort_array = Algorithm.quick_sort_algorithm(input_array.copy(), 0, len(input_array) - 1, 0)
    end_time = time.time()
    current_size_time.append(end_time - start_time)

    # 7 - Merge Sort
    start_time = time.time()
    merge_sort_array = Algorithm.merge_sort_algo(input_array.copy())
    end_time = time.time()
    current_size_time.append(end_time - start_time)

    return current_size_time, self_sort_array


def generate_excel(random_sort_times, increasing_sort_times, decreasing_sort_times, file_columns, excel_name):
    """ For generating an Excel sheet with the elapsed time details """

    random_df = pd.DataFrame(random_sort_times, columns=file_columns)
    increasing_df = pd.DataFrame(increasing_sort_times, columns=file_columns)
    decreasing_df = pd.DataFrame(decreasing_sort_times, columns=file_columns)

    with pd.ExcelWriter(excel_name) as writer:
        random_df.to_excel(writer, sheet_name='Random Data', index=None)
        increasing_df.to_excel(writer, sheet_name='Increasing Data', index=None)
        decreasing_df.to_excel(writer, sheet_name='Decreasing Data', index=None)


def generate_and_sort(array_min_size, array_max_size, array_increment, maximum_repetitions):
    """ For generating a random array from the given min range to max range and for performing sorting """

    random_all_times = []
    increasing_all_times = []
    decreasing_all_times = []

    file_columns = ["Array Size", "Self Tuning Sort", "Selection Sort", "Bubble Sort", "Insertion Sort",
                    "Shell Sort", "Quick Sort", "Merge Sort"]
    outfile_name = "time_data_input_{0}_to_{1}.xlsx".format(array_min_size, array_max_size)

    array_size = array_min_size
    while array_size <= array_max_size:
        iteration_num = 1
        while iteration_num <= maximum_repetitions:
            random_array = random_array_generation(array_size)
            random_time, increasing_time, decreasing_time = perform_sorting_multiple(random_array, file_columns)

            random_all_times.append(random_time)
            increasing_all_times.append(increasing_time)
            decreasing_all_times.append(decreasing_time)

            iteration_num = iteration_num + 1
        array_size = array_size + array_increment

    generate_excel(random_all_times, increasing_all_times, decreasing_all_times, file_columns, outfile_name)


def perform_sorting_multiple(input_array, columns_data):
    """ For performing sorting multiple times on a given array, sorted array, and decreasing array """

    array_size = len(input_array)
    if len(set(input_array)) != 1:

        # Random Array Sorting
        random_time, sorted_array = run_algorithms(input_array, array_size)

        # Increasing Array Sorting
        increasing_time, already_sorted = run_algorithms(sorted_array, array_size)

        # Decreasing Array Sorting
        decreasing_time, decrease_sorted = run_algorithms(sorted_array[::-1], array_size)

    else:
        default_data = [array_size] + [0] * (len(columns_data) - 1)
        increasing_time = default_data.copy()
        decreasing_time = default_data.copy()
        random_time = default_data.copy()
        sorted_array, already_sorted, decrease_sorted = default_data.copy(), default_data.copy(), default_data.copy()

    return random_time, increasing_time, decreasing_time


def sort_split_arrays(input_list, user_input):
    """ For clubbing the arrays and for calling the merge result of the Merge Sort algorithm """
    """
    * Merge Sort's merge result algorithm requires 2 arrays and an input array for comparison. This function is used for
    calling the merge result algorithm, where first the function takes the 0th array as the sorted array.
    * Then, for creating a combined array, script will iterate arrays from index 1 till the last array and combines both
    the arrays for creating an unsorted array
    * Then the unsorted(clubbed) array, along with the other 2 arrays will be sent to the merge result algorithm. And, 
    the returned sorted array along with the next iteration array and the current clubbed array will be sent to the
    merge result algorithm repeatedly till the last array is sorted. 
    """

    sorted_array = input_list[0]
    for each in range(1, len(input_list)):
        current_list = input_list[each]

        combined_list = sorted_array + current_list

        sorted_array = Algorithm.merge_result(sorted_array, current_list, combined_list)
    return sorted_array


if __name__=="__main__":
    generate_and_sort(array_min_size=900, array_max_size=1000, array_increment=10, maximum_repetitions=10)
