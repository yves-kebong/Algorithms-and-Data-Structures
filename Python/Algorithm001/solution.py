def iincide_target(array , target):
  n=len(array)
  for i in range(n):
    for j in range (i+1, n):
      if array[i]+array[j] == target:
        return [i,j]
      else :
        print("indices don't exist")
  return []