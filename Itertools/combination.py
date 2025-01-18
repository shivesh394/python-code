from itertools import combinations
arr = [1, 2, 3, 4]
arr = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
r = 2
comb = list(combinations(arr, r))
print(comb, len(comb))   
# to deal with duplicate subsets use set(list(combinations(arr, r)))



from itertools import combinations_with_replacement
comb = list(combinations_with_replacement([1, 2, 3, 4], 3))
print(comb)
print(len(comb))
