# WHILE LOOP - indefinite loop i.e. loops until a logical condition results in false
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Done!')

# BREAK STATEMENT - ends loop and jumps to the statement that immediately follows
while True:
    line = input('Type here:')
    if line == 'done':
        break  # exits to print('Done!')
    print(line)
print('Done!')


# CONTINUE STATEMENT - ends current iteration and skips to the next iteration of the loop
while True:
    line = input('Type here:')
    if line[0] == '#':
        print('Hashtagged')
        continue
    if line == 'done':
        break  # exits to print('Done!')
    print(line)
print('Done!')

