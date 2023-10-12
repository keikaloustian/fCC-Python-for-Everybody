# ELSE IF STATEMENT
x = 2
if x < 2:
    print('...')
elif x == 2:
    print('...')


# TRY / EXCEPT STATEMENT
try:
    val = int('word')  # code that could result in an error
except:
    val = - 1  # "fallback" code in case of error
print('Result', val)  # -> -1



