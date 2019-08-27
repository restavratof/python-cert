# A specialized class name bytearray - is an array containing (amorphous) bytes.
#
# Bytearrays are:
#   - mutable
#   - a subject of the len() function
#   - you can access any of their elements using conventional indexing
#   - you mustn't set any byte array elements with a value which is not an integer (TypeError exception)
#   - you're not allowed to assign a value that doesn't come from the range 0 to 255 inclusive (ValueError exception)
#   - You can treat any byte array elements as integer values
#   -

# NOTE: such a constructor fills the whole array with zeros.
data = bytearray(10)

print('1','-'*20)
for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

#--------------------------------------------------------------
print('2','-'*20)
from os import strerror
test_bin_file = 'file.bin'
try:
    bf = open(test_bin_file, 'wb')
    result = bf.write(data)
    print('RESULT:', result)
    bf.close()
except IOError as e:
    print('I/O error occured: ', strerror(e.errno))

#--------------------------------------------------------------
# write() method returns number of successfully written bytes.
print('3','-'*20)
try:
    bf = open(test_bin_file, 'rb')
    bf.readinto(data)
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print('I/O error occured: ', strerror(e.errno))

#--------------------------------------------------------------
# read() - invoking without arguments, it tries to read all the contents of the file into the memory,
#       making them part of newly created object of bytes class.
#       Similar to bytearray, with significant exception - it is immutable.
# !!!! don't use this kind of read if you're not sure that the file's contents will fit the available memory. !!!!
print('\n4','-'*20)
try:
    bf = open(test_bin_file, 'rb')
    data = bytearray(bf.read())
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print('I/O error occured: ', strerror(e.errno))

# if read() is invoked with argument, it specifies the maximum number of bytes to be read.
print('\n5','-'*20)
try:
    bf = open(test_bin_file, 'rb')
    data = bytearray(bf.read(5))
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print('I/O error occured: ', strerror(e.errno))
# Note: the first five bytes of the file have been read by the code - the next five are still waiting to be processed.


# if read() is invoked with argument, it specifies the maximum number of bytes to be read.
print('\n6','-'*20)

srcname = input("Source file name?: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open source file: ", strerror(e.errno))
    exit(e.errno)
dstname = input("Destination file name?: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create destination file: ", strerr(e.errno))
    src.close()
    exit(e.errno)

buffer = bytearray(65536)
total = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create destination file: ", strerr(e.errno))
    exit(e.errno)

print(total, 'byte(s) succesfully written')
src.close()
dst.close()





