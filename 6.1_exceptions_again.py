def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print(reciprocal(0))


# BaseException
#    +---Exception
#    |   +---TypeError
#    |   +---StopAsyncIteration
#    |   +---StopIteration
#    |   +---ImportError
#    |   |   +---ModuleNotFoundError
#    |   |   +---ZipImportError
#    |   +---OSError
#    |   |   +---ConnectionError
#    |   |   |   +---BrokenPipeError
#    |   |   |   +---ConnectionAbortedError
#    |   |   |   +---ConnectionRefusedError
#    |   |   |   +---ConnectionResetError
#    |   |   +---BlockingIOError
#    |   |   +---ChildProcessError
#    |   |   +---FileExistsError
#    |   |   +---FileNotFoundError
#    |   |   +---IsADirectoryError
#    |   |   +---NotADirectoryError
#    |   |   +---InterruptedError
#    |   |   +---PermissionError
#    |   |   +---ProcessLookupError
#    |   |   +---TimeoutError
#    |   |   +---UnsupportedOperation
#    |   |   +---herror
#    |   |   +---gaierror
#    |   |   +---timeout
#    |   |   +---Error
#    |   |   |   +---SameFileError
#    |   |   +---SpecialFileError
#    |   |   +---ExecError
#    |   |   +---ReadError
#    |   +---EOFError
#    |   +---RuntimeError
#    |   |   +---RecursionError
#    |   |   +---NotImplementedError
#    |   |   +---_DeadlockError
#    |   |   +---BrokenBarrierError
#    |   +---NameError
#    |   |   +---UnboundLocalError
#    |   +---AttributeError
#    |   +---SyntaxError
#    |   |   +---IndentationError
#    |   |   |   +---TabError
#    |   +---LookupError
#    |   |   +---IndexError
#    |   |   +---KeyError
#    |   |   +---CodecRegistryError
#    |   +---ValueError
#    |   |   +---UnicodeError
#    |   |   |   +---UnicodeEncodeError
#    |   |   |   +---UnicodeDecodeError
#    |   |   |   +---UnicodeTranslateError
#    |   |   +---UnsupportedOperation
#    |   +---AssertionError
#    |   +---ArithmeticError
#    |   |   +---FloatingPointError
#    |   |   +---OverflowError
#    |   |   +---ZeroDivisionError
#    |   +---SystemError
#    |   |   +---CodecRegistryError
#    |   +---ReferenceError
#    |   +---BufferError
#    |   +---MemoryError
#    |   +---Warning
#    |   |   +---UserWarning
#    |   |   +---DeprecationWarning
#    |   |   +---PendingDeprecationWarning
#    |   |   +---SyntaxWarning
#    |   |   +---RuntimeWarning
#    |   |   +---FutureWarning
#    |   |   +---ImportWarning
#    |   |   +---UnicodeWarning
#    |   |   +---BytesWarning
#    |   |   +---ResourceWarning
#    |   +---error
#    |   +---Verbose
#    |   +---Error
#    |   +---TokenError
#    |   +---StopTokenizing
#    |   +---Empty
#    |   +---Full
#    |   +---_OptionError
#    |   +---TclError
#    |   +---SubprocessError
#    |   |   +---CalledProcessError
#    |   |   +---TimeoutExpired
#    |   +---Error
#    |   |   +---NoSectionError
#    |   |   +---DuplicateSectionError
#    |   |   +---DuplicateOptionError
#    |   |   +---NoOptionError
#    |   |   +---InterpolationError
#    |   |   |   +---InterpolationMissingOptionError
#    |   |   |   +---InterpolationSyntaxError
#    |   |   |   +---InterpolationDepthError
#    |   |   +---ParsingError
#    |   |   |   +---MissingSectionHeaderError
#    |   +---InvalidConfigType
#    |   +---InvalidConfigSet
#    |   +---InvalidFgBg
#    |   +---InvalidTheme
#    |   +---EndOfBlock
#    |   +---BdbQuit
#    |   +---error
#    |   +---_Stop
#    |   +---PickleError
#    |   |   +---PicklingError
#    |   |   +---UnpicklingError
#    |   +---_GiveupOnSendfile
#    |   +---error
#    |   +---LZMAError
#    |   +---RegistryError
#    |   +---ErrorDuringImport
#    +---GeneratorExit
#    +---SystemExit
#    +---KeyboardInterrupt

def printExcTree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)

printExcTree(BaseException)



