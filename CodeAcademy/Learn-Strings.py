def get_length(string):
  i = 0
  for let in string:
    i+=1
  return i

def letter_check(word, letter):
  for let in word:
    if let == letter:
      return True
    elif word[-1]==let:
      return False

def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False

def common_letters(string_one, string_two):
  common_lets = []
  for let in string_one:
    if let in common_lets:
      continue
    if let in string_two:
      common_lets.append(let)
  return common_lets

  def username_generator(first_name, last_name):
  f = 0
  l = 0
  if len(first_name)<3:
    f = len(first_name)
  if len(first_name)>=3:
    f = 3
  if len(last_name)<4:
    l = len(last_name)
  if len(last_name)>=4:
    l = 4
  user = first_name[:f] + last_name[:l]  
  return user
print(username_generator('yo', 'dawg'))

# Creates password out of username such that each letter is shifted to the
# right one spot (end letter is first letter)
def password_generator(username):
  password = ""
  i = -1
  for let in username:
    password += username[i]
    i += 1
  return password