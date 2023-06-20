def removeDuplicates(nums):
    # create dict occurrences
    my_dict = {num: nums.count(num) for num in nums}

    # find max value
    max_val = max(my_dict.values())

    # find wanted index of max_value
    wanted_index = list(my_dict.keys())[list(my_dict.values()).index(max_val)]

    # number of duplicate to remove
    remove = max_val - 2

    # remove
    my_dict[wanted_index] -= remove

    # spread dict to list
    nums = [key for key, value in my_dict.items() for _ in range(value)]

    # k = length of the list returned
    k = len(nums)

    return k


print(removeDuplicates([1,1,1,2,2,3]))