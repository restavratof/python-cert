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

# Finally,
# the successful opening of the file will set the current file position (the virtual reading/writing head)
#   before the first byte of the file if the mode is not a
#   and after the last byte of file if the mode is set to a



