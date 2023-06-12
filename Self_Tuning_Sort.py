

def split_array(input_array):
    """ For splitting given input array into arrays of Increasing and Random Arrays """
    """
    This function compares the current iterating value with the previous value, and if already a flag exists, checks the
    condition as per the flag. Else, as per the comparison script puts a value to the flag variable.
    
    When the flag is equal to 1, function checks whether the current value is greater than a previous value or not.
    If True, appends the value to the existing array. Else, appends the existing values to the split_eles and
    continues the comparison.
    Same case with the flag 2. If flag already exists and if the comparison is True, inserts the value at the 0th index.
    Else, appends the existing array to the split_eles, and continues the comparison.
    
    Time Complexity: O(n)
    """

    split_eles = []
    current_cond_eles = []
    flag = ''

    current_cond_eles.append(input_array[0])

    for element_index in range(1, len(input_array)):
        current_element = input_array[element_index]

        # 1 - Equal Element Condition
        if input_array[element_index] == input_array[element_index - 1] and not flag:
            current_cond_eles.append(current_element)

        # 2 - Increasing Element Condition
        elif input_array[element_index] >= input_array[element_index - 1] and (not flag or flag == 1):
            flag = 1
            current_cond_eles.append(current_element)

        # 3 - Decreasing Element Condition
        elif input_array[element_index] <= input_array[element_index - 1] and (not flag or flag == 2):
            flag = 2
            current_cond_eles.insert(0, current_element)

        # Breaking Logic
        else:
            split_eles.append(current_cond_eles)

            current_cond_eles = []
            flag = ''
            current_cond_eles.append(current_element)

    if current_cond_eles:
        split_eles.append(current_cond_eles)

    return split_eles


if __name__ == "__main__":
    print(split_array([22, 31, 34, 89, 89, 44, 52, 38, 42, 10]))
