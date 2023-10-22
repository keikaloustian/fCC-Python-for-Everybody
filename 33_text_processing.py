# ASCII - AMERICAN STANDARD CODE FOR INFORMATION INTERCHANGE

# 256 characters, digits, symbols, non-printing characters, each represented by a number from zero to 256.
# Represents simple (mainly English) strings.
# 8 bits (0 or 1) or one byte per character.

# ord() function tells us the numeric value of a simple ASCII character
ord('H')  # -> 72
ord('\n')  # -> 10


# UNICODE
# Computers needed to understand more characters, therefore came along much more complex character sets such as Unicode.
# To send it over the internet, Unicode would be UTF-32, which is four bytes per character, which would be too big.
# There is also UTF-16 (two bytes), used by in some countries.


# UTF-8
# Recommended practice for encoding data to be exchanged between computers.
# UTF-8 is dynamic, one to four bytes.
# The first byte corresponds to ASCII, thus it's backwards compatible.


# In Python 3 all strings are Unicode
# There's also a <class 'bytes'> which is basically an array of bytes.
# Most of the time when working with external resources, the encoding is UTF-8 (but can be others)
# Python strings need to be encoded into bytes (usually UTF-8) before being sent and received data needs to be decoded
# encode() and decode() are for Unicode <-> UTF-8 by default; other encoding can be specified as argument
