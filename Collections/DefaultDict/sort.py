from collections import Counter
nums = [-1,1,-6,4,5,-6,1,4,1]

# Count the frequency of each number in the list using Counter
num_frequency = Counter(nums)

# Sort the numbers based on the frequency (ascending order)
# sorted_nums = sorted(nums, key=lambda x: (num_frequency[x],))


# When frequencies are the same, sort by the number itself (descending order)
sorted_nums = sorted(nums, key=lambda x: (num_frequency[x], -x))

print(sorted_nums)