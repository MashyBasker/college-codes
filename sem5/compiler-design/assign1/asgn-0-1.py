import re


def is_valid_identifier(identifier):
    # Regular expression to check if the identifier is valid
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return re.match(pattern, identifier)


def find_identifiers(source_code):
    # Split the source code into words (assuming identifiers are separated by whitespace)
    words = re.findall(r'\b\w+\b', source_code)

    # Filter out the valid identifiers
    valid_identifiers = [word for word in words if is_valid_identifier(word)]

    return valid_identifiers


if __name__ == "__main__":
    input_source_program = """
        int a = 10;
        double pi = 3.14159;
        string name = "John Doe";
        bool is_valid = True;
        for i in range(5):
            print(i)
    """

    identifiers = find_identifiers(input_source_program)
    print("Identifiers found in the source program:")
    print(identifiers)
