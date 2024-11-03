

def check(lines, config):
    errors = []
    max_length = config.get("max_line_length", 80)
    
    for lineno, line in enumerate(lines, start=1):
        if len(line) > max_length:
            errors.append({
                "line": lineno,
                "error": f"Line exceeds {max_length} characters.",
                "type": "LineLengthError"
            })
    return errors
A
