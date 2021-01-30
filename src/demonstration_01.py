"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
# def two_sum(nums, target):
#     indecis = []
#     for num in nums:
#         for num2 in nums:
#             if num + num2 == target:
#                 indecis.append(nums.index(num))
#                 indecis.append(nums.index(num2))
#         break
#     return indecis


# QUADRATIC TIME, O(n^2)

# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             num1 = nums[i]
#             num2 = nums[j]
#             if num1 + num2 == target:
#                 return [i, j]
#     return None

    # Your code here


def two_sum(nums, target):
    num_dict = {}

    for i in range(len(nums)):
        num_dict[nums[i]] = i
    print(num_dict)
    
    for i in range(len(nums)):
        current_num = nums[i]
        #check if the compliment is in dict
        compliment = target - current_num

        if compliment in num_dict and i != num_dict[compliment]:
            return [i, num_dict[compliment]]



print(two_sum(nums = [2, 5, 9, 13], target = 7))
print(two_sum(nums = [4,3,5], target = 8))