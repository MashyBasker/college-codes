import re


def find_keywords(source_code, keywords):
    # Regular expression to find keywords
    keyword_pattern = r'\b(' + '|'.join(keywords) + r')\b'
    found_keywords = re.findall(keyword_pattern, source_code)
    return found_keywords


if __name__ == "__main__":
    # List of Python keywords
    python_keywords = [
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
        'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
        'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
    ]

    input_source_program = """
        # This is a sample Python program
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)
    """

    keywords_found = find_keywords(input_source_program, python_keywords)
    print("Keywords found in the source program:")
    print(keywords_found)
