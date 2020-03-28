# Divisble by Ten
# Create a function named divisible_by_ten() that takes a list of numbers 
# named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num%10==0:
      count += 1
    else:
      continue
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))


# Greetings
# Create a function named add_greetings() which takes a list of strings 
# named names as a parameter.
# In the function, create an empty list that will contain each greeting. 
# Add the string "Hello, " in front of each name in names and append the 
# greeting to the list.
# Return the new list containing the greetings.
def add_greetings(names):
  greeted = []
  for name in names:
    greeting = "Hello, " + name
    greeted.append(greeting)
  return greeted


# Delete Starting Even Numbers
# Write a function called delete_starting_evens() that has a parameter 
# named lst.
# The function should remove elements from the front of lst until the 
# front of the list is not even. The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], 
# then delete_starting_evens(lst) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!
def delete_starting_evens(lst):
  for num in lst:
    if num%2==0:
      lst = lst[1:]
    else:
      break
  return lst

def delete_starting_evens1(lst):
  while len(lst)>=1:
    if (lst[0])%2==0:
      lst = lst[1:]
    else:
      break
  return lst

print(delete_starting_evens1([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens1([4, 8, 10]))


# Odd Indices
# Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from 
# lst that has an odd index. The function should then return this new list.
def odd_indices(lst):
  oddities = []
  for num in lst:
    if (lst.index(num))%2!=0:
      oddities.append(num)
  return oddities

print(odd_indices([4, 3, 7, 10, 11, -2]))


# Exponents
# Create a function named exponents() that takes two lists as parameters 
# named bases and powers. Return a new list containing every number in 
# bases raised to every number in powers.
def exponents(bases, powers):
  superpowers = []
  for base in bases:
    for power in powers:
      superpowers.append(base**power)
  return superpowers

print(exponents([2, 3, 4], [1, 2, 3]))


# Larger Sum
# Create a function named larger_sum() that takes two lists of numbers as 
# parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater 
# number. If the sum of the elements of each list are equal, return lst1.
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num in lst1:
    sum1+=num
  for num in lst2:
    sum2+=num
  if sum2>sum1:
    return lst2
  else:
    return lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))


# Over 9000
# Create a function named over_nine_thousand() that takes a list of 
# numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is 
# greater than 9000. When this happens, the function should return the 
# sum. If the sum of all of the elements is never greater than 9000, the 
# function should return total sum of all the elements. If the list is 
# empty, the function should return 0.
def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
  if sum>0:
    sum = 0
    for num in lst:
      sum += num
      if sum>9000:
        return sum
    return sum  
  if sum<=0:
    return sum
  if len(lst)==0:
    return 0
print(over_nine_thousand([1]))

# What I wrote originally (that's actually way cooler, b/c it keeps adding
# the next value in the list continuously going through the list until it
# hits 9001 and then stops)
def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
  if sum>0:
    sum = 0
    while sum<=9000:
      for num in lst:
        sum += num
        if sum>9000:
          break
    return sum
  if sum<=0:
    return sum
  if len(lst)==0:
    return 0
print(over_nine_thousand([1]))


# Max Number
# (This one was deceptively a bitch)
# Create a function named max_num() that takes a list of numbers named nums 
# as a parameter. The function should return the largest number in nums
def max_num(nums):
  for num in nums:
    i = 0
    while i<len(nums):
      if num>=(nums[i]):
        i+=1
        if i==len(nums):
          return num
      else:
        break

print(max_num([50, -10, 0, 75, 20]))


# Same Values
# Write a function named same_values() that takes two lists of numbers of 
# equal size as parameters.
# The function should return a list of the indices where the values were 
# equal in lst1 and lst2.
def same_values(lst1, lst2):
  indexes = []
  i = 0
  while i<len(lst1):
    if lst1[i] == lst2[i]:
      indexes.append(i)
      i += 1
    else:
      i += 1
  return indexes

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# Reversed List
# Create a function named reversed_list() that takes two lists of the same 
# size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The 
# function should return False otherwise.
def reversed_list(lst1, lst2):
  lst1r = []
  i = 1
  while i<=len(lst1):
    lst1r.append(lst1[0-i])
    i+=1
  print(lst1r)
  print(lst2)
  if lst1r==lst2:
    return True
  else:
    return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))