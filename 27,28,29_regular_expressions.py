# CHARACTER-BASED EXPRESSIONS FOR MATCHING AND PARSING STRINGS

import re  # -> library required
fh = open('mailbox.txt')
for line in fh:
    line = line.rstrip()
    if re.search('^From:', line):
        # re.search returns True if reg expression is found in string, otherwise False
        print(line)


# SOME REGEX EXAMPLES
# ^ matches start of line
# . any character
# * signifies "any number of times"
# \S any non-whitespace character
# + one or more times


# re.findall() - finds and returns list of all matches ([] if none found)
x = 'My 2 favourite numbers are 11 and 100'
y = re.findall('[0-9]+', x)  # -> ['2', '11', '100']


# GREEDY MATCHING
# The repeat characters (* and +) will look for the largest possible match by pushing outward in both directions

# To disable greedy matching and match the shortest possible string, follow the * or + with a ?

# The string extraction can be fine-tuned by surrounding the portion of interest with ()
z = re.findall('^From (\S+@\S+)')  # -> Matching lines need to start with 'From ', but only \S+@\S+ will be returned and assigned to z

# ESCAPING CHARACTERS
# $ matches the expression to its left at the end of a string
# If we want to match the dollar sign character and not the special definition above, it needs to be escaped with a backslash:
z = re.findall('\$', x)