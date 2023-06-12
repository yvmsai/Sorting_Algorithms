"""
All sorting algorithms
"""

import math
class Algorithm:

    def selection_sort(input_array):
        """
        For sorting the given array using Selection Sort algorithm
        Time Complexity: O(n^2) (Best, Average, and Worst Case(s))
        """

        for i in range(0, len(input_array)-1):
            min_val = i
            for j in range(i+1, len(input_array)):
                if input_array[j] < input_array[min_val]:
                    min_val = j
            input_array[i], input_array[min_val] = input_array[min_val], input_array[i]

        return input_array


    def bubble_sort(input_array):
        """
        For sorting the given array using Bubble Sort algorithm
        Time Complexity: O(n) - Best Case, O(n^2) - Average and Worst Case
        """

        for i in range(0, len(input_array)-1):
            for j in range(0, len(input_array)-1-i):
                if input_array[j + 1] < input_array[j]:
                    input_array[j], input_array[j + 1] = input_array[j + 1], input_array[j]

        return input_array


    def insertion_sort(input_array):
        """
        For sorting the given array using Insertion Sort algorithm
        Time Complexity: n - Best Case, n^2 - Average and Worst Case
        """

        for i in range(1, len(input_array)):
            v = input_array[i]
            j = i - 1
            while j >= 0 and input_array[j] > v:
                input_array[j+1] = input_array[j]
                j = j-1
            input_array[j+1] = v

        return input_array


    def shell_sort(input_array):
        """
        For solving the array using Shell Sort algorithm
        Time Complexity: O(n) - Best, O(n log^2 n) - Average and Worst Case
        """
        reverse_val_1 = None

        array_length = len(input_array)
        shell_gap = array_length//2

        """
        1. Algorithm will calculate the gap or h value for iterating first.
        2. Generates the indexes that needs to be compared using th calculated h value
        3. When the index 1 value is greater than index 2, elements will be swapped and reverse_condition will be flagged
           as TRUE
           3.1. When the reverse_condition is flagged as TRUE, comparison will go in the reverse direction and the loop
                will iterate until there is a small value in reverse_val_2.
                When the value is small, reverse_condition will be flagged as False and while loop will stop iterating
        4. Reduce the h by 2 more and take the floor value
        """

        while shell_gap > 0:
            for index_1 in range(0, array_length):
                index_2 = index_1 + shell_gap
                reverse_condition = False
                if index_2 < array_length:
                    if input_array[index_1] > input_array[index_2]:
                        input_array[index_1], input_array[index_2] = input_array[index_2], input_array[index_1]
                        reverse_condition = True
                        reverse_val_1 = index_1

                # Point - 3.1
                    while reverse_condition:
                        reverse_val_2 = reverse_val_1 - shell_gap
                        if reverse_val_2 >= 0 and input_array[reverse_val_1] < input_array[reverse_val_2]:
                            input_array[reverse_val_1], input_array[reverse_val_2] = input_array[reverse_val_2], \
                                                                                 input_array[reverse_val_1]
                            reverse_val_1 = reverse_val_1 - shell_gap
                        else:
                            reverse_condition = False

            shell_gap = shell_gap//2

        return input_array


    def quick_sort_algorithm(input_array, start_index, end_index, pivot_pos):
        """ A simple quick sort algorithm """
        """
        Partitions the array and recursively runs the algorithm
        After partition, start position of the array is considered as the pivot position of the array
        Left Partition Array - Pivot Index will be the start of the array before partition (i.e., start_index)
        Right Partition Array - Pivot Index will be the next index of the sorted element's index
        
        Time Complexity: O(n log n) - Best and Average Cases, O(n^2) - Worst Case
        """

        if start_index < end_index:
            sorted_index = Algorithm.quick_sort_partition(input_array, start_index, end_index, pivot_pos)

            Algorithm.quick_sort_algorithm(input_array, start_index, sorted_index-1, pivot_pos=start_index)
            Algorithm.quick_sort_algorithm(input_array, sorted_index+1, end_index, pivot_pos=sorted_index+1)

        return input_array

    def quick_sort_partition(sort_array, start_pos, end_pos, pivot_index):
        """ For partitioning the array """
        """
        Uses the start position, end position and pivot index and values to partition the array
        *   Start position will be increased everytime by 1 if the value at the start position is lesser than or equal to
            pivot value.
        *   End position will be decreased everytime by 1 if the value at the end position is greater than pivot value
        *   If start position is lesser than end position, swaps the values at start position and end position
        *   If start position becomes greater than end position, swaps the values at the pivot index and end position and 
            returns the end position which will help in partitioning the input array.
        """
        pivot_val = sort_array[pivot_index]
        while start_pos < end_pos:
            while start_pos < len(sort_array) and sort_array[start_pos] <= pivot_val:
                start_pos = start_pos + 1

            while sort_array[end_pos] > pivot_val and end_pos >= 0:
                end_pos = end_pos - 1

            if start_pos < end_pos:
                sort_array[start_pos], sort_array[end_pos] = sort_array[end_pos], sort_array[start_pos]

        sort_array[pivot_index], sort_array[end_pos] = sort_array[end_pos], sort_array[pivot_index]

        return end_pos


    def merge_sort_algo(input_array):
        """
        For performing Merge Sort Algorithm
        Time Complexity: O(n log n) (includes the time complexity of merging the results)
        """

        if len(input_array) > 1:
            divide_index = math.floor(len(input_array) / 2)
            array_1, array_2 = input_array[0:divide_index], input_array[divide_index:]

            Algorithm.merge_sort_algo(array_1)
            Algorithm.merge_sort_algo(array_2)
            Algorithm.merge_result(array_1, array_2, input_array)
        return input_array


    def merge_result(first_array, second_array, original_array):
        i, j, k = 0, 0, 0
        while i < len(first_array) and j < len(second_array):
            if first_array[i] <= second_array[j]:
                original_array[k] = first_array[i]
                i = i + 1
            else:
                original_array[k] = second_array[j]
                j = j + 1
            k = k + 1

        if i == len(first_array):
            original_array[k:len(original_array)] = second_array[j: len(second_array)+1]
        else:
            original_array[k:len(original_array)] = first_array[i: len(first_array)+1]

        return original_array
