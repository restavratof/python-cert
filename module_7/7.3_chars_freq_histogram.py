from os import strerror

# srcname = input("Source file name?: ")
srcname = '7.1_test_file.txt'
outname = f"{srcname}.hist"

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

# chars_freq_sort = sorted((key, value) for (key,value) in chars_freq.items())
chars_freq_sort = print(sorted(chars_freq.items(), key=lambda kv: (kv[1], kv[0])))

for key, val in chars_freq_sort.items():
    print(key,' -> ', val, sep='')

try:
    fo = open(outname, 'wt')
    for key, val in chars_freq_sort.items():
        # print('"', key, '" -> ', val, sep='')
        fo.write(f"{key} -> {val}\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))