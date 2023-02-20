"""
Given an array of integers, return the indexes (as a Python set) of the two numbers that add up to a specific target.
You may assume that each input would have **exactly one solution**, and you may **not use the same element twice**.

Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""

def two_sum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] + nums[j] == target: return {i, j}


def two_sum(nums, target): return {i for i in range(len(nums)) for j in range(len(nums)) if nums[i] + nums[j] == target and i != j}

assert two_sum([2, 7, 11, 15], 9) == set((0, 1))
assert two_sum([2, 20, 1, -5, 3], 4) == set((2, 4))
assert two_sum([3, 1, 1, 1, 1, 3], 6) == set((0, 5))

""""
You are given an array of integers called nums. The numbers stored in the array appear twice except for one number, 
which only appears once. Write a method that finds this number. 

Example:
    nums = [1,4, 1, 3, 5, 5, 4] return 3
"""
# def find_unique(nums):
#   for i in range(len(nums)):
#     found = False
#     for j in range(len(nums)):
#       if i == j: pass
#       elif nums[i] == nums[j]: 
#         found = True
#         break
#       else: pass
#     if found == False:
#       return nums[i]

def find_unique(nums):
  for i in range(len(nums)):
    if nums.count(nums[i]) == 1: 
      return nums[i]

def find_unique(nums): return {s for s in nums if nums.count(s) == 1}.pop()

assert find_unique([1, 4, 1, 3, 5, 5, 4]) == 3

### [25 points] Problem 3

"""
Given a string of words separated by spaces, find the word that appears the most in the string. Feel free to assume that there will be no ties.

    Example:

    Given "hello world hello hello world hi"

    Return hello
"""

# def most_common_word(string):
#   words = {word: 0 for word in string.split()}
#   for word in string.split():
#     words[word] += 1
#   return max(words, key=words.get)

def most_common_word(string):
    words = {(word.lower()): 0 for word in string.split()}
    for word in string.split(): words[(word.lower())] += 1 
    return max(words, key=words.get)
#def most_common_word(string): return max(string.split(), key=string.split().count)

assert most_common_word("Hello world hello hello world hi") == "hello"
assert most_common_word("this is is a test just a just a test") == "a"

"""
Given a list of words, return the words that can be typed using letters of the alphabet that appear on only one row 
of the American keyboard (see image below).

Example:
    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: {"Alaska", "Dad"}
"""
# def keyboard_row(words_lst):
#   output = set()
#   rows = (set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm"))
#   for word in words_lst:
#     wordset = set(word.lower())
#     if wordset.issubset(rows[0]) or wordset.issubset(rows[1]) or wordset.issubset(rows[2]):
#       output.add(word)
#   return output

# def keyboard_row(words_lst):
#   rows = (set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm"))
#   return {word for word in words_lst if set(word.lower()).issubset(rows[0]) or set(word.lower()).issubset(rows[1]) or set(word.lower()).issubset(rows[2])}

def keyboard_row(word_lst): return {word for word in word_lst if set(word.lower()).issubset(set("qwertyuiop")) or set(word.lower()).issubset(set("asdfghjkl")) or set(word.lower()).issubset(set("zxcvbnm"))}

def keyboard_row(word_lst): return {word for word in word_lst if set(word.lower()) <= set("qwertyuiop") or set(word.lower()) <= set("asdfghjkl") or set(word.lower()) <= set("zxcvbnm")}


# def keyboard_row(words_lst): 
#   rows = (
#       {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"},
#       {"a", "s", "d", "f", "g", "h", "j", "k", "l"},
#       {"z", "x", "c", "v", "b", "n", "m"}
#   )
#   return {word for word in words_lst if set(word.lower()).issubset(rows[0]) or set(word.lower()).issubset(rows[1]) or set(word.lower()).issubset(rows[2])}

assert keyboard_row(["Hello", "Alaska", "Dad", "Peace"]) == set(("Alaska", "Dad"))
assert keyboard_row(["Typewriter", "Fads", "Dads", "Peace"]) == set(("Typewriter", "Fads", "Dads"))