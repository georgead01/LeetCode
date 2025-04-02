def threeSumClosest(nums, target):
        
    n = len(nums)
    nums.sort()

    diff = float('inf')
    s = 0
    
    min_diff = diff
    answer = s

    for i in range(n-2):

        j = i+1
        k = n-1
        while j < k:
            s = nums[i]+nums[j]+nums[k]
            if s == target:
                return s

            diff = abs(s-target)

            if diff < min_diff:
                min_diff = diff
                answer = s

            if s < target:
                j += 1
            if s > target:
                k -= 1

    return answer