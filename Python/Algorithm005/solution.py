def merge(interval):
  n=len(interval)
  merge=[]
  non_overlap=[]
  if interval==[]:
    print("Your interval is empty")
  else:
    interval.sort()
    for i in range(0,n+1):
      for j in range(i+1,n):
        if interval[i][1] > interval[j][0]:
          merge.extend(interval[i][1] > interval[j][1])
        else:
          non_overlap.extend([interval[i] > interval[j]])
    return non_overlap
