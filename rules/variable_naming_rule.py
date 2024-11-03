
import re

def check(lines, config):
    errors = []
    naming_convention = config.get("naming_convention", "snake_case")
    
    assignment_pattern = re.compile(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=')
    
    for lineno, line in enumerate(lines, start=1):
        match = assignment_pattern.match(line)
        if match:
            variable_name = match.group(1)
            if naming_convention == "snake_case" and not re.match(r'^[a-z_][a-z0-9_]*$', variable_name):
                errors.append({
                    "line": lineno,
                    "error": f"Variable name '{variable_name}' should be in snake_case.",
                    "type": "VariableNamingError"
                })
    return errors
