# CHARACTER-BASED EXPRESSIONS FOR MATCHING AND PARSING STRINGS
import re  # -> library required

fh = open('mailbox.txt')
for line in fh:
    line = line.rstrip()
    if re.search('^From:', line):  # -> search From: in the beginning of lines
        print(line)


# SOME EXAMPLES
# ^ matches start of line
# . any character
# * signifies "any number of times"
# \S any non-whitespace character
# + one or more times