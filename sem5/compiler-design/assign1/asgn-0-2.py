import re


def find_input_statements(source_code):
    # Regular expression to find input statements
    input_pattern = r'\b(input|scanf)\s*\('
    input_statements = re.findall(input_pattern, source_code)
    return input_statements


def find_output_statements(source_code):
    # Regular expression to find output statements
    output_pattern = r'\b(print|printf)\s*\('
    output_statements = re.findall(output_pattern, source_code)
    return output_statements


if __name__ == "__main__":
    input_source_program = """
        # Input statement examples
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        
        # Output statement examples
        print("Hello, " + name + "! You are " + str(age) + " years old.")
        printf("Hello, %s! You are %d years old.", name, age);
    """

    input_statements = find_input_statements(input_source_program)
    output_statements = find_output_statements(input_source_program)

    print("Input statements found in the source program:")
    print(input_statements)

    print("\nOutput statements found in the source program:")
    print(output_statements)
