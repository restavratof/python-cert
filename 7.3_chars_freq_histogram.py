from os import strerror

# srcname = input("Source file name?: ")
srcname = '7.1_test_file.txt'

chars_freq = {}

try:
    src = open(srcname, 'rt')
    ch = src.read(1).lower()
    while ch != '':
        # print(ch, end='')
        if ch in chars_freq:
            chars_freq[ch] = chars_freq[ch] + 1
        else:
            chars_freq[ch] = 1
        ch = src.read(1).lower()
    src.close()
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)

for key, val in chars_freq.items():
    print('"',key,'" -> ', val, sep='')

