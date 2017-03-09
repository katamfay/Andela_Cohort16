def find_missing(list1, list2):
  

  same = list1 + list2
  if same == 0 or list1 == list2:
    return 0
  
  for i in list1:
    if i in list2:
      continue
    else:
      return i
    
  for j in list2:
    if j in list1:
      continue
    else:
      return j
  