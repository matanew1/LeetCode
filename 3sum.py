def threeSum(nums):
    start, end = 0, len(nums) - 1
    zeros = []
    res = []

    nums.sort()
    while end - start > 1:
        for i in range(start + 1, len(nums) - 1):
            base = nums[start] + nums[end]
            sum = base + nums[i]
            if sum == 0:
                zeros.append([nums[start], nums[i], nums[end]])
            res.append(base + nums[i])
        max_val = max(res)
        res = []
        if max_val <= 0:
            start += 1
        else:
            end -= 1

    merged_list=[]
    for sublist in zeros:
        if sublist not in merged_list:
            print(sublist, merged_list)
            merged_list.append(sublist)
    print(merged_list)

threeSum([-1,0,1,2,-1,-4])