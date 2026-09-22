nums = [2,7,11,15]
target = 9

#num[0] + num [1] = target

hash_set = {}

for i, n in enumerate(nums):
  diff = target - n
  if diff in hash_set:
    print((hash_set[diff], i))
    break
  hash_set[n] = i
