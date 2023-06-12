import numpy as np
import sys
sys.setrecursionlimit(10 ** 8)
from driver_code import perform_sorting_multiple, generate_excel


def PoissonDistribution(lam, range):
    """ For generating an array using given lambda value and range """
    s = np.random.poisson(lam, range)
    return_val = []

    for each in s:
        return_val.append(each)

    return return_val


def mean_fixedStdDeviation(mean, sd, size):
    """ For generating an array using given mean, standard deviation, array size"""
    return_val = []
    s = list(np.random.normal(mean, sd, size).astype(int))

    for each in s:
        return_val.append(each)
    return return_val


def run_input_data(input_array, cond_val, stat_type):
    """ For generating CSV from the given arrays """
    increasing_time_data = []
    decreasing_time_data = []
    random_time_data = []

    columns_data = ["Array Size", "Condition Value", "Self Tuning Sort", "Selection Sort", "Bubble Sort", "Insertion Sort",
                    "Shell Sort", "Quick Sort", "Merge Sort"]

    outfile_name = "time_stat_data_{0}.xlsx".format(stat_type)

    for input_line in range(len(input_array)):
        random_time, increasing_time, decreasing_time = perform_sorting_multiple(input_array[input_line], columns_data)

        random_time.insert(1, cond_val[input_line])
        increasing_time.insert(1, cond_val[input_line])
        decreasing_time.insert(1, cond_val[input_line])

        random_time_data.append(random_time)
        increasing_time_data.append(increasing_time)
        decreasing_time_data.append(decreasing_time)

    generate_excel(random_time_data, increasing_time_data, decreasing_time_data, columns_data, outfile_name)


def generate_csv(stat_type, repetitions, lambda_start, lambda_max, array_length_min, array_length_max,
                 array_size_increment):
    """ Generates the CSV with the given parameters """

    return_list = []
    cond_val = []

    lam = lambda_start

    # Poisson Distribution
    if stat_type == 'poisson':
        while lam <= lambda_max:
            array_size = array_length_min
            while array_size <= array_length_max:
                iteration_number = 1
                while iteration_number <= repetitions:

                    generated_array = PoissonDistribution(lam, array_size)
                    return_list.append(generated_array)
                    cond_val.append(lam)

                    iteration_number = iteration_number + 1

                array_size = array_size + array_size_increment

            lam = lam + 0.5

    # Fixed Mean
    elif stat_type == 'meanfixedsd':
        mean_val = 50
        sd_val = lambda_start
        while sd_val <= lambda_max:
            array_size = array_length_min
            while array_size <= array_length_max:
                iteration_number = 1
                while iteration_number <= repetitions:
                    generated_array = mean_fixedStdDeviation(mean_val, sd_val, array_size)
                    return_list.append(generated_array)
                    cond_val.append(sd_val)

                    iteration_number = iteration_number + 1
                array_size = array_size + array_size_increment

            sd_val = sd_val + 10

    # Fixed Standard Deviation
    elif stat_type == 'fixedsdmean':
            sd_val = 100
            mean_val = lambda_start
            while mean_val <= lambda_max:
                array_size = array_length_min
                while array_size <= array_length_max:
                    iteration_number = 1
                    while iteration_number <= repetitions:
                        generated_array = mean_fixedStdDeviation(mean_val, sd_val, array_size)
                        return_list.append(generated_array)
                        cond_val.append(mean_val)

                        iteration_number = iteration_number + 1
                    array_size = array_size + array_size_increment

                mean_val = mean_val + 500

    run_input_data(return_list, cond_val, stat_type)


if __name__ == "__main__":
    if int(sys.argv[1]) == 1:
        generate_csv('fixedsdmean', 5, 1000, 5000, 20000, 20000, 10)
    elif int(sys.argv[1]) == 2:
        generate_csv('meanfixedsd', 1, 10, 100, 20000, 20000, 10)
    elif int(sys.argv[1]) == 3:
        generate_csv('poisson', 10, 2, 6, 10, 100, 10)
