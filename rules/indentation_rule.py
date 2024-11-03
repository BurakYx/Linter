
def check(lines, config):
    errors = []
    for lineno, line in enumerate(lines, start=1):
        leading_spaces = len(line) - len(line.lstrip(' '))
        if leading_spaces % config['indentation'] != 0:
            errors.append({
                "line": lineno,
                "error": "Indentation is not a multiple of {0} spaces.".format(config['indentation']),
                "type": "IndentationError"
            })
    return errors
