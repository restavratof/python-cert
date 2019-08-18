from os import  strerror
test_file = '7.1_test_file.txt'

#---------------------------------------------------
# 1 - Read the whole file at once
stream = open(test_file, 'rt', encoding='utf-8')
print(stream.read()) # printing the content of the file

#---------------------------------------------------
# 2 - Read file char by char
print('1','-'*20)
try:
    cnt = 0
    s = open(test_file, 'rt')
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print('I/O error occured: ', strerror(e.errno))

#---------------------------------------------------
# 3 - Read file line by line
print('2','-'*20)
try:
    ccnt = lcnt = 0
    s = open(test_file, 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:       ", lcnt)
except IOError as e:
    print("I/O error occured:", strerror(e.errno))


#---------------------------------------------------
# readlines()
#   read all the file contents, and returns a list of strings, one element per file line.
#   The maximum accepted input buffer size is passed to the method as its argument.
print('3','-'*20)
try:
    ccnt = lcnt = 0
    s = open(test_file, 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

#---------------------------------------------------
# Iteration
#   The object returned by the open() is an instance of the iterable class.
#   Its __next__ method just returns the next line read in from the file
#   You can expect that the object automatically invokes close() when any of the file reads reaches the end of the file.
print('4','-'*20)
try:
    ccnt = lcnt = 0
    for line in open(test_file, 'rt'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:       ", lcnt)
except IOError as e:
    print("I/O error occured: ", strerror(e.errno))




