import os
import re


def camel_to_snake(name):
    """Converts CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def convert_to_snake_case(text):
    """Converts __to__snake__case imports to correct imports."""
    pattern = r'__to__snake__case\(([a-zA-Z0-9]+)\)'

    def replacer(match):
        class_name = match.group(1)
        snake_case_name = camel_to_snake(class_name)
        return snake_case_name

    return re.sub(pattern, replacer, text)


def convert_type_annotations(text):
    """Replaces dict(str, object) with dict[str, object] in function annotations."""
    result = text
    replacement_pairs = [
        (r'-> dict\((\w+), (\w+)\):', r'-> Dict[\1, \2]:'),
        (r'-> Optional\[dict\((\w+), (\w+)\)\]:', r'-> Optional[Dict[\1, \2]]:'),
        (r': dict\((\w+), (\w+)\)', r': Dict[\1, \2]'),
        (r': Optional\[dict\((\w+), (\w+)\)\]', r': Optional[Dict[\1, \2]]'),
        (r'-> list\[(\w+)\]:', r'-> List[\1]:'),
        (r'-> Optional\[list\[(\w+)\]\]:', r'-> Optional[List[\1]]:'),
        (r': list\[(\w+)\]', r': List[\1]'),
        (r': Optional\[list\[(\w+)\]\]', r': Optional[List[\1]]')
    ]
    for pattern, replacement in replacement_pairs:
        result = re.sub(pattern, replacement, result)
    return result


def process_file(file_path: str):
    """Reads file, performs conversion and writes back."""
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()

    content = convert_to_snake_case(content)
    content = convert_type_annotations(content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def process_models():
    """Run through all models."""
    directory = './fingerprint_server_sdk/models'
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                process_file(file_path)


if __name__ == "__main__":
    process_models()

