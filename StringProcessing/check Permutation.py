#is_permutation_1 = "google"
# is_permutation_2 = "ooggle"
# is_permutation_1 is a permutation of is_permutation_2 bcus:
# same length of string,
# equal amount of characters.

# The code from line 5 to line 9 is the same as in Solution 1.
#  On line 11, d is initialized to a Python dictionary.
#   Using a for loop on line 13 where i equals a character in str_1, i is stored as a key in d with 1 as a value if it’s not present in d.
#    If it’s present, its value is incremented by 1. After this for loop, d will have the entire count of all the characters present in str_1.
#     We’ll make use of this in the for loop on line 18 where str_2 is traversed.
#     If any character in str_2 is present as a key in d, its value is decremented by 1.
#    If it’s not already present in d, it is inserted into d as a key with value equal to 1.

# Now, if str_1 and str_2 are permutations of each other, the two for loops will counterbalance each other and the values of all the keys in d should be 0.
#  We find this out on line 24 where we evaluate value == 0 for all the keys in d.
#   Using the all function, we combine the evaluation results from all the iterations and return it from the function.
#   The all() function returns True if all items in an iterable are True. Otherwise, it returns False.

# Approach 2: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    d = dict()

    for i in str_1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in str_2:
        if i in d:
            d[i] -= 1
        else:
            return False

    return all(value == 0 for value in d.values())


is_permutation_1 = "google"
is_permutation_2 = "ooggle"

print(is_perm_2(is_permutation_1, is_permutation_2))
