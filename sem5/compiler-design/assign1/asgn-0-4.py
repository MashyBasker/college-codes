import re


def remove_comments(source_code):
    # Regular expression to remove single-line comments
    cleaned_code = re.sub(r'#.*', '', source_code)

    # Regular expression to remove multi-line comments
    cleaned_code = re.sub(r'/\*.*?\*/', '', cleaned_code, flags=re.DOTALL)

    return cleaned_code


if __name__ == "__main__":
    input_source_program = """
        # This is a single-line comment
        def factorial(n):
            # Calculate factorial using recursion
            if n == 0:
                return 1
            else:
                return n * factorial(n-1)

        /*
        This is a multi-line comment.
        It spans multiple lines and will be removed.
        */

        print(factorial(5))  # Output: 120
    """

    cleaned_code = remove_comments(input_source_program)
    print("Code without comments:")
    print(cleaned_code)
