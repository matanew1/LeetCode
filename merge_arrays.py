def merge(nums1, m, nums2, n):
    # if one of them is empty, returns the non-emtpy result
    if not nums1:
        return nums2
    if not nums2:
        return nums1

    # find occurances of each list
    occ_nums1 = {num1: nums1.count(num1) for num1 in nums1 if num1 > 0}
    occ_nums2 = {num2: nums2.count(num2) for num2 in nums2 if num2 > 0}

    # merge dicts to one dicts
    merged_dict = {key: occ_nums1.get(key, 0) + occ_nums2.get(key, 0)
                   for key in set(occ_nums1.keys()) | set(occ_nums2.keys())}

    # convert dict occurances to list spread
    nums1 = [key for key, value in merged_dict.items() for _ in range(value)]
    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))