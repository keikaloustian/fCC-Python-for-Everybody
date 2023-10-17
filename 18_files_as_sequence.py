# READING FILE ONE LINE AT A TIME

# A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence.

# That means a for loop can be used to iterate through the file.

file_handle = open('mbox.txt')
for line in file_handle:
    print(line)


# .read() - READING WHOLE FILE AT ONCE (INTO ONE STRING)
input = file_handle.read()


# USING TRY/EXCEPT TO HANDLE BAD FILE NAMES
fname = input('Enter file name:')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened.')
    quit()  # the quit() function terminates the execution of the program
