class Report:
    def __init__(self, errors):
        self.errors = errors

    def display(self):
        if not self.errors:
            print("No linting errors found!")
            return

        print("Linting errors found:")
        for error in self.errors:
            print(f"Line {error['line']}: {error['error']} ({error['type']})")
