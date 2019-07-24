import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_object):
    print(json.dumps(json_object, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            cmd_arg = sys.argv[1]
            pretty_print_json(load_data(cmd_arg))
        except FileNotFoundError:
            print('File "', cmd_arg, '" not found.', sep='')
    else:
        print(
            '''
            File not found.
            To print the json-file in readable form, pass it as a parameter.
            For example:
            > pprint_json.py example.json
            '''
        )
