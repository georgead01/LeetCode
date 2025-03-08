def permute(nums):
    n = len(nums)

    # base case
    if n <= 1:
        return [nums]
    # recursive case
    else:
        result = []

        for i in range(n):
            elt = nums[i]
            rest = nums[:i]+nums[i+1:]
            
            for perm in permute(rest):
                result.append([elt]+perm)

        return result