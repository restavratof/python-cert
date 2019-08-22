from os import strerror

test_file = '7.1_test_file.txt'
#------------------------------------------------------
# Write into file char by char
try:
    fo = open(test_file, 'wt')
    for i in range(3):
        s = "test line #"+ str(i+1) + "\n"
        for ch in s:
            fo.write(ch)
    fo.close()
except IOError as e:
    print("I/O error occured: ", strerror(e.errno))

#------------------------------------------------------
# Write into file line by line
print('1','-'*20)
try:
    fo = open(test_file, 'wt')
    for i in range(3):
        fo.write("test line #"+ str(i+1) +"\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))



