# Regular Expressions
import re

patterns = ["term1", "term2"]

text = "This is a string with pattern term1, but not the other"

for pattern in patterns:
    print("I'm searching for {}".format(pattern))

    if re.search(pattern, text):
        print("MATCH FOR {}".format(pattern))
    else:
        print("NO MATCH")


# find a match : re.search(term_to_search, text)
match = re.search("term1", text)
print(type(match))  # <class 're.Match'>

# match = re.search("term2", text)
# print(type(match))  # <class 'NoneType'>

# find the index of match : match.start()
# returns the index in string, from where the match found
start_index = match.start()
print(start_index)  # 30

# split the text: just like split() method in string
split_term = "@"
email = "user@email.com"

print(re.split(split_term, email)) # ['user', 'email.com']


# get the number of how many times a pattern appears in a string
find_all_matches = re.findall("match", "test phrase match in match middle")
print(find_all_matches) # ['match', 'match']
print("'match' appears in string {} times".format(len(find_all_matches))) # 'match' appears in string 2 times


def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("\nSearching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")

test_phrase = "sdsd..sssddd..sdddsddd..dsds..dssssss..sddddd"


test_pattern = ["sd*"] # returns 's' followed by 0 or more 'd'

multi_re_find(test_pattern, test_phrase)
# ['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sddddd']


test_pattern = ["sd+"] # returns 's' followed by 1 or more 'd'

multi_re_find(test_pattern, test_phrase)
# ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddddd']


test_pattern = ["sd?"] # returns 's' followed by 0 or 1 'd'

multi_re_find(test_pattern, test_phrase)
# ['sd', 'sd', 's', 's', 'sd', 'sd', 'sd', 'sd', 's', 's', 's', 's', 's', 's', 's', 'sd']


test_pattern = ["sd{3}"] # returns 's' followed by exactly 3 'd'

multi_re_find(test_pattern, test_phrase)
# ['sddd', 'sddd', 'sddd', 'sddd']


test_pattern = ["sd{2,3}"] # returns 's' followed by 2 or 3 'd'

multi_re_find(test_pattern, test_phrase)
# ['sddd', 'sddd', 'sddd', 'sddd']


test_pattern = ["sd{1,3}"] # returns 's' followed by 1 or 3 'd'

multi_re_find(test_pattern, test_phrase)
# ['sd', 'sd', 'sddd', 'sddd', 'sddd', 'sd', 'sddd']


test_pattern = ["s[sd]+"] # returns 's' followed by 1 or more 's' or 'd'

multi_re_find(test_pattern, test_phrase)
# ['sdsd', 'sssddd', 'sdddsddd', 'sds', 'ssssss', 'sddddd']


## exclusion

test_phrase = "This is a string! But it has punctuation. How can we remove it?"


test_pattern = ["[^!.?]+"] # exclude 1 or more instances of '!.?'

multi_re_find(test_pattern, test_phrase)
# ['This is a string', ' But it has punctuation', ' How can we remove it']


test_pattern = ["[a-z]+"] # returns all lower case letters

multi_re_find(test_pattern, test_phrase)
# ['his', 'is', 'a', 'string', 'ut', 'it', 'has', 'punctuation', 'ow', 'can', 'we', 'remove', 'it']


test_pattern = ["[A-Z]+"] # returns all upper case letters

multi_re_find(test_pattern, test_phrase)
# ['T', 'B', 'H']


test_phrase = "This is a string with numbers 1223231 and symbols #hashtag"


test_pattern = [r"\d+"] # returns all the digits

multi_re_find(test_pattern, test_phrase)
# ['1223231']


test_pattern = [r"\D+"] # returns all the non-digits

multi_re_find(test_pattern, test_phrase)
# ['This is a string with numbers ', ' and symbols #hashtag']


test_pattern = [r"\s+"] # returns all the white-spaces. useful when counting the spaces

multi_re_find(test_pattern, test_phrase)
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


test_pattern = [r"\S+"] # returns all the non-white-spaces. useful to extract all the words

multi_re_find(test_pattern, test_phrase)
# ['This', 'is', 'a', 'string', 'with', 'numbers', '1223231', 'and', 'symbols', '#hashtag']


test_pattern = [r"\w+"] # returns all the alpha-numerics: letters and numbers

multi_re_find(test_pattern, test_phrase)
# ['This', 'is', 'a', 'string', 'with', 'numbers', '1223231', 'and', 'symbols', 'hashtag']


test_pattern = [r"\W+"] # returns all the non-alpha-numerics

multi_re_find(test_pattern, test_phrase)
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' #']