numbers = [2,7,11,15]
target = 9

first = 0
last = len(numbers) - 1

while first < last:
  sum = numbers[first] + numbers[last]
  if target < sum:
    last -=1
  elif target > sum:
    first +=1
  else:
    print((first+1, last+1))
    break
print([])
    
