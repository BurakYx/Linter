import argparse
from linter import Linter

def main():
    parser = argparse.ArgumentParser(description="Run a linter on your Python code.")
    parser.add_argument("file", help="Python file to lint")
    parser.add_argument("-c", "--config", help="Path to configuration file", default="config/default_config.json")
    args = parser.parse_args()

    linter = Linter(args.file, args.config)
    linter.lint()
    linter.report()

if __name__ == "__main__":
    main()
