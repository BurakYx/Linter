def auto_fix(filename, errors):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for error in errors:
        if error["type"] == "IndentationError":
            lineno = error["line"] - 1
            lines[lineno] = " " * 4 + lines[lineno].lstrip()  

    with open(filename, 'w') as file:
        file.writelines(lines)
