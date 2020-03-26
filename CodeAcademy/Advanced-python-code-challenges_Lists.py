#1 Every Three Numbers
# Create a function called every_three_nums that has one parameter named 
# start. 
# The function should return a list of every third number between 
# start and 100 (inclusive). For example, every_three_nums(91) should 
# return the list [91, 94, 97, 100]. If start is greater than 100, the 
# function should return an empty list.
def every_three_nums(start):
  cool_lst = list(range(start, 101, 3))
  return cool_lst

print(every_three_nums(91)) #test


#2 Remove Middle
# Create a function named remove_middle which has three parameters named 
# lst, start, and end.
# The function should return a list where all elements in lst with an 
# index between start and end (inclusive) have been removed.
# For example, the following code: 
# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
# should return [4, 23, 42] because elements at indices 1, 2, and 3 
# have been removed.
remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
def remove_middle(lst, start, end):
  del lst[start:(end+1)]
  return lst

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


#3 More Frequent Item
# Create a function named more_frequent_item that has three parameters 
# named lst, item1, and item2.
# Return either item1 or item2 depending on which item appears more 
# often in lst.
# If the two items appear the same number of times, return item1.
def more_frequent_item(lst, item1, item2):
  num1 = lst.count(item1)
  num2 = lst.count(item2)
  if num2>num1:
    return item2
  else:
    return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


#4 Double Index
# Create a function named double_index that has two parameters: a list 
# named lst and a single number named index.
# The function should return a new list where all elements are the same 
# as in lst except for the element at index. The element at index should 
# be double the value of the element at index of the original lst.
# If index is not a valid index, the function should return the original 
# list.
def double_index(lst, index):
  length = len(lst)
  if index>=0 and index<length:
    lst[index] = 2*(lst[index])
    return lst
  else:
    return lst

#5 Middle Item
# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return 
# the middle element. If there are an even number of elements, the function 
# should return the average of the middle two elements.
def middle_element(lst):
  length = len(lst)
  odds = list(range(1,length+1, 2))
  evens = list(range(2, length+1, 2))
  if length==odds[-1]:
    middle_index = int((odds[-1]-1)/2)
    return lst[middle_index]
  else:
    num2 = lst[int((odds[-1]-1)/2)]
    num1 = lst[int((evens[-1])/2)]
    return (num1+num2)/2

print(middle_element([5, 2, -10, -4, 4, 5])) #test