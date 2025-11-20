from typing import *
import yaml
import pickle
import sys

def to_ron_pretty(obj: Any, indent=0) -> str:
    spaces = '  ' * indent
    if obj is None:
        return "None"
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        s = obj.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        return f'"{s}"'
    elif isinstance(obj, list):
        if not obj:
            return "[]"
        items = []
        for item in obj:
            item_str = to_ron_pretty(item, indent + 1)
            items.append(f'\n{spaces}  {item_str}')
        return f'[{",".join(items)}\n{spaces}]'

    elif isinstance(obj, dict):
        if not obj:
            return "{}"

        pairs = []
        for k, v in obj.items():
            if not isinstance(k, str):
                raise ValueError("Ключи в RON должны быть строками")
            if k.replace('_', '').replace('-', '').isalnum() and k[0].isalpha():
                key_ron = k
            else:
                key_ron = to_ron_pretty(k, indent)
            value_str = to_ron_pretty(v, indent + 1)
            pairs.append(f'\n{spaces}  {key_ron}: {value_str}')
        return f'{{{",".join(pairs)}\n{spaces}}}'

    else:
        raise TypeError(f"Неподдерживаемый тип: {type(obj)}")

def yaml_to_binary(yaml_text: str) -> bytes:
    data = yaml.load(yaml_text, Loader=yaml.SafeLoader)
    return pickle.dumps(data)

def binary_to_ron(binary_data: bytes) -> str:
    data = pickle.loads(binary_data)
    return to_ron_pretty(data)

def yaml_to_ron_via_binary(yaml_text: str) -> str:
    binary_data = yaml_to_binary(yaml_text)
    return binary_to_ron(binary_data)


if __name__ == "__main__":
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            yaml_content = f.read()

        binary_data = yaml_to_binary(yaml_content)
        print("Результат бинарного перевода:")
        print(binary_data)
        bin_file = sys.argv[1].replace('.yaml', '.bin').replace("in", "out")
        with open(bin_file, 'wb') as f:
            f.write(binary_data)
        print(f"Бинарный объект сохранен в {bin_file}")

        result = yaml_to_ron_via_binary(yaml_content)
        print("Результат RON:")
        print(result)
        output_file = sys.argv[1].replace('.yaml', '.ron').replace("in", "out")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\nРезультат сохранен в {output_file}")

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)