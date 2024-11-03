import json
import os
from rules import (
    indentation_rule,
    line_length_rule,
    naming_convention_rule,
    function_count_rule,
    variable_naming_rule
)
from fixer import fixer
from report import Report

class Linter:
    def __init__(self, filename, config_file='config/default_config.json'):
        self.filename = filename
        self.config = self.load_config(config_file)
        self.errors = []

    def load_config(self, config_file):
        """Load configuration from a JSON file."""
        with open(config_file, 'r') as f:
            return json.load(f)

    def lint(self):
        """Run all linting rules on the file."""
        with open(self.filename, 'r') as file:
            lines = file.readlines()

        self.errors.extend(indentation_rule.check(lines, self.config))
        self.errors.extend(line_length_rule.check(lines, self.config))
        self.errors.extend(naming_convention_rule.check(lines, self.config))
        self.errors.extend(function_count_rule.check(lines, self.config))
        self.errors.extend(variable_naming_rule.check(lines, self.config))

        if self.config.get("enable_auto_fix"):
            fixer.auto_fix(self.filename, self.errors)

    def report(self):
        """Generate and display the linting report."""
        report = Report(self.errors)
        report.display()
