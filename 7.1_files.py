###################################
# MODES:
# r open mode: read
#     the stream will be opened in read mode;
#     the file associated with the stream must exist and has to be readable, otherwise the open() function raises an exception.
#
# w open mode: write
#     the stream will be opened in write mode;
#     the file associated with the stream doesn't need to exist; if it doesn't exist it will be created;
#           if it exists, it will be truncated to the length of zero (erased);
#           if the creation isn't possible (e.g., due to system permissions) the open() function raises an exception.
#
# a open mode: append
#     the stream will be opened in append mode;
#     the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created;
#           if it exists the virtual recording head will be set at the end of the file
#           (the previous content of the file remains untouched.)
#
# r+ open mode: read and update
#     the stream will be opened in read and update mode;
#     the file associated with the stream must exist and has to be writeable, otherwise the open() function raises an exception;
#     both read and write operations are allowed for the stream.
#
# w+ open mode: write and update
#     the stream will be opened in write and update mode;
#     the file associated with the stream doesn't need to exist; if it doesn't exist, it will be created;
#           the previous content of the file remains untouched;
#     both read and write operations are allowed for the stream.
#####################################################
# Text mode 	Binary mode 	Description
# rt 	        rb 	            read
# wt 	        wb 	            write
# at 	        ab 	            append
# r+t 	        r+b 	        read and update
# w+t 	        w+b 	        write and update
#####################################################
# You can also open a file for its exclusive creation. You can do this using the x open mode.
#   If the file already exists, the open() function will raise an exception.
#
# Finally,
# the successful opening of the file will set the current file position (the virtual reading/writing head)
#   before the first byte of the file if the mode is not a
#   and after the last byte of file if the mode is set to a
####################################################################################
# PRE_OPENED STREAMS:
#   sys.stdin
#       - stdin(as standard input)
#       - the stdin stream is normally associated with the keyboard,
#           pre-open for reading and regarded as the primary data source for the running programs;
#       - the well - known input() function reads data from stdin by default.
# sys.stdout
#       - stdout(as standard output)
#       - the stdout stream is normally associated with the screen, pre-open for writing,
#           regarded as the primary target for outputting data by the running program;
#       - the well - known print() function outputs the data to the stdout stream.
# sys.stderr
#       - stderr(as standard error output)
#       - the stderr stream is normally associated with the screen, pre-open for writing,
#           regarded as the primary place where the running program should send information on the errors encountered during its work;
#       - we haven't presented any method to send the data to this stream (we will do it soon, we promise)
#       - the separation of stdout(useful results produced by the program) from the stderr
#           (error messages, undeniably useful but does not provide results)
#           gives the possibility of redirecting these two types of information to the different targets.
#           More extensive discussion of this issue is beyond the scope of our course.
#           The operation system handbook will provide more information on these issues.
####################################################################################

import errno

try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # processing goes here
    stream.close()
except IOError as exc:
    print(exc.errno)
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print(f"The error number is:{exc.errno}")


####################################################################################
# USEFUL DETECTING STREAMS ERRORS CONSTANTS
####################################################################################
# errno.EACCES → Permission denied
#       The error occurs when you try, for example, to open a file with the read only attribute for writing.
#
# errno.EBADF → Bad file number
#       The error occurs when you try, for example, to operate with an unopened stream.
#
# errno.EEXIST → File exists
#       The error occurs when you try, for example, to rename a file with its previous name.
#
# errno.EFBIG → File too large
#       The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.
#
# errno.EISDIR → Is a directory
#       The error occurs when you try to treat a directory name as the name of an ordinary file.
#
# errno.EMFILE → Too many open files
#       The error occurs when you try to simultaneously open more streams than acceptable for your operating system.
#
# errno.ENOENT → No such file or directory
#       The error occurs when you try to access a non-existent file/directory.
#
# errno.ENOSPC → No space left on device
#       The error occurs when there is no free space on the media.
####################################################################################


