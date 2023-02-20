"""
Given a list of integers *nums* consisting of 2n elements 
in the form $[x_1,x_2,...,x_n,y_1,y_2,...,y_n]$, return a 
list that contains the same values as *nums* but in the 
form $[x_1,y_1,x_2,y_2,...,x_n,y_n]$.

Example: nums=[2,5,1,3,4,7], n=3 -> [2,3,5,4,1,7] 
"""
def shuffle(nums: list, n: int) -> list:
  return [x for pair in zip(nums[:n], nums[n:]) for x in pair]

assert shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7] 

"""
Given an integer list nums and an integer k (where k >= 1), 
count how many numbers in the list are divisible by k.

Example: nums=[1,2,3,4,5,6,7,8,9,10], k=2 -> 5
"""
def count_divisible(nums: list[int], k: int) -> int:
    return len([x for x in nums if x % k == 0])

assert count_divisible([1,2,3,4,5,6,7,8,9,10], 2) == 5


"""
Given an integer list nums and a non-negative integer k, 
circularly shift the array to the left by k spaces. Elements 
at the beginning of the list are to be shifted to the end of 
the list.

Examples: nums=[1,2,3,4,5], k = 1 -> [2,3,4,5,1]
          nums=[1,2,3,4,5], k = 3 -> [4,5,1,2,3]
"""
def circular_shift(nums: list, k: int) -> list:
  return nums[k:] + nums[:k]

assert circular_shift([1,2,3,4,5], 3) == [4,5,1,2,3]
assert circular_shift([1,2,3,4,5], 4) == [5,1,2,3,4]
assert circular_shift([1,2,3,4,5], 5) == [1,2,3,4,5]

"""
Given two lists of integers, return a new list that contains 
the common elements between them in ascending order. Feel free 
to assume that neither list contains duplicates.

Examples: nums1=[1,2,3], nums2=[2,5,1] -> [1,2] 
          nums1=[2,3,1], nums2=[5,0,7] -> []

Optional Extension: Assume either list could contain duplicates 
(feel free to decide how the output should look like when 
duplicates are found).
"""
def list_intersection(nums1: list, nums2: list) -> list:
    output: list[int] = [x for x in nums1 if x in nums2]
    output.sort()
    return output

assert list_intersection([1,2,3], [2,5,1]) == [1,2]
assert list_intersection([3,2,1], [2,5,1]) == [1,2]