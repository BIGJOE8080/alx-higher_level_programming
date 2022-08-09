Executable File  9 lines (7 sloc)  231 Bytes
#!/usr/bin/python3
'''Module for read_file method.'''


def read_file(filename=""):
    '''Method for reading from a file.'''
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
