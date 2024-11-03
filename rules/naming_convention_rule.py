
import re

def check(lines, config):
    errors = []
    naming_convention = config.get("naming_convention", "snake_case")
    
    function_pattern = re.compile(r'^\s*def\s+([a-zA-Z_]+)\s*\(.*\):')
    
    for lineno, line in enumerate(lines, start=1):
        match = function_pattern.match(line)
        if match:
            function_name = match.group(1)
            if naming_convention == "snake_case" and not re.match(r'^[a-z_][a-z0-9_]*$', function_name):
                errors.append({
                    "line": lineno,
                    "error": f"Function name '{function_name}' should be in snake_case.",
                    "type": "NamingConventionError"
                })
    return errors
