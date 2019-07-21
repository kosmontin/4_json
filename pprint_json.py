import json
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_handler:
        return json.loads(file_handler.read())


def pretty_print_json(raw_json):
    print(json.dumps(raw_json, indent=4, ensure_ascii=False))
    pass


if __name__ == '__main__':
    cmd_arg = sys.argv[1] if len(sys.argv) > 1 else 'example.json'
    try:
        pretty_print_json(load_data(cmd_arg))
    except FileNotFoundError:
        print('File "', cmd_arg, '" not found.', sep='')
    pass
