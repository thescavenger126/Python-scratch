# Strings INTRODUCTION
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

# String METHODS
# .split() auto does " ", but can do any other string (as seen with comma)
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"
author_names = authors.split(',')
author_last_names = []
for name in author_names:
  first_last = name.split()
  author_last_names.append(first_last[-1])
print(author_last_names)

data_set = """1 2 3 4
5 6 7 8 9
10  11  12"""
data_set_lines = data_set.split('\n')
print(data_set_lines)

# .join() is the exact opposite of split - takes a list and joins them with
# string you provide
data_set_reborn = '\n'.join(data_set_lines)
print(data_set_reborn)

# .strip() removes a specific string (or character(s)) from your string
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

# .replace(argument1, argument2) finds all of argument1's in the string and
# replaces it with argument2
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. 
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

# .find() finds the index of the first character of the argument provided in
# the string
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

# .format() takes variables as an argument and includes them in
# the string that it is run on. You include {} marks as 
# placeholders for where those variables will be imported
def poem_title_card(poet, title):
  card = 'The poem "{}" is written by {}.'.format(title, poet)
  return card
print(poem_title_card('Max', 'Johny Rocket'))

def poem_description(publishing_date, author, title, original_work):
  poem_desc = """
  The poem {title} by {author} was originally published in {original_work} 
  in {publishing_date}.""".format(title=title, author=author, original_work=original_work, publishing_date=publishing_date)
  return poem_desc
print(poem_description('Dec 23rd, 1999', 'T-Prehl', 'The Awesome-est', 'Origin Story'))

# Review of String METHODS
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
highlighted_poems_list = highlighted_poems.split(',')
highlighted_poems_stripped = []
for info in highlighted_poems_list:
  stripped = info.strip()
  highlighted_poems_stripped.append(stripped)
highlighted_poems_details = []
for info in highlighted_poems_stripped:
  stripped = info.split(':')
  highlighted_poems_details.append(stripped)
titles = []
poets = []
dates = []
for info in highlighted_poems_details:
  title = info[0]
  poet = info[1]
  date = info[2]    
  titles.append(title)
  poets.append(poet)
  dates.append(date)
i = 0
for title in titles:
  poem_desc = """
  The poem {} was published by {} in {}
  """.format(title, poets[i], dates[i])
  print(poem_desc)
  i += 1