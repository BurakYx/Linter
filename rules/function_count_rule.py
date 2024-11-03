
import re

def check(lines, config):
    errors = []
    max_functions = config.get("max_functions_per_file", 10)
    
    function_pattern = re.compile(r'^\s*def\s+[a-zA-Z_]+\s*\(.*\):')
    function_count = sum(1 for line in lines if function_pattern.match(line))
    
    if function_count > max_functions:
        errors.append({
            "line": 0,  
            "error": f"File contains {function_count} functions, exceeding the limit of {max_functions}.",
            "type": "FunctionCountError"
        })
    
    return errors
