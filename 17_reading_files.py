# OPENING A FILE
open('filename', 'mode')  # -> function that takes in a file name and an optional mode such as 'r' for read and 'w' for write. Returns a file handle.

# If a file is not found, open() will result in a traceback.

handle = open('mbox.txt')


# NEWLINE CHARACTER
'\n'
# A newline character exists at the end of each line in a file.