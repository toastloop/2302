def circular_shift(nums, k):
    output = []
    for i in range(k, len(nums)):
        output.append(nums[i])
    for i in range(k):
        output.append(nums[i])
    print(output)

circular_shift([1,2,3,4,5], 3)