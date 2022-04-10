def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())
        file_copy("print.py", "for.py")
        with open('for.py', 'r') as filehandle:
            for line in filehandle:
                print(line, end = '')
