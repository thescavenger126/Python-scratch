#for examples, name of list is "lst"
lst = [value1, value2, ...]
len(lst) # provides length of list **if there are 4 values, len(lst)=4** 
lst[num] # num is a +/- index of lst, and will provide value at that index
range(start, end, increment) # creates a range of #'s as specified, but DOES NOT MAKE ACTUAL LISt (must use list(...) to make list)
lst.count(value) # counts number of times the value occurs in the list
zip(lst1, lst2) # combines two lists such that value1 of list 1 and value 1 of list 2 are paired, etc (must use list(...) to make list)
del lst[index1:index2] # deletes section of list **deletes values UP TO BUT NOT INCLUDING index2** 
def middle_element(lst):
  length = len(lst)
  print(length)
  odds = list(range(1,length+1, 2))
  evens = list(range(2, length+1, 2))
  if length==odds[-1]:
    return lst[]
  
  
  print(odds)
  print(evens)

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))