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

print('2','-'*20)
from os import strerror
test_bin_file = 'file.bin'
try:
    bf = open(test_bin_file, 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print('I/O error occured: ', strerror(e.errno))

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


# readlines() -


