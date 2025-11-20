from typing import *
import sys
import struct


class Token:
    def __init__(self, type_: str, value: Any, line: int, col: int):
        self.type = type_
        self.value = value
        self.line = line
        self.col = col

def tokenize(text: str) -> List[Token]:
    tokens = []
    lines = text.split('\n')

    for line_index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        indent_level = len(line) - len(line.lstrip())
        tokens.append(Token("INDENT", indent_level, line_index, 0))

        if stripped.startswith('-'):
            tokens.append(Token("DASH", "-", line_index, indent_level))
            rest = stripped[1:].strip()
            if rest and ':' in rest:
                key_part, value_part = rest.split(':', 1)
                tokens.append(Token("KEY", key_part.strip(), line_index, indent_level + 2))
                tokens.append(Token("COLON", ":", line_index, indent_level + 2 + len(key_part)))
                if value_part.strip():
                    tokens.append(Token("STRING", value_part.strip(), line_index, indent_level + 2 + len(key_part) + 1))
        elif ':' in stripped:
            key_part, value_part = stripped.split(':', 1)
            key_part = key_part.strip()
            value_part = value_part.strip()

            tokens.append(Token("KEY", key_part, line_index, indent_level))
            tokens.append(Token("COLON", ":", line_index, indent_level + len(key_part)))

            if value_part:
                tokens.append(Token("STRING", value_part, line_index, indent_level + len(key_part) + 1))

        tokens.append(Token('NEWLINE', '\\n', line_index, len(line)))

    return tokens


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def peek(self, offset=0) -> Optional[Token]:
        if self.pos + offset < len(self.tokens):
            return self.tokens[self.pos + offset]
        return None

    def consume(self, expected_type: str = None) -> Token:
        token = self.peek()
        if not token:
            raise SyntaxError("Неожиданный конец файла")
        if expected_type and token.type != expected_type:
            raise SyntaxError(f"Ожидался {expected_type}, но получен {token.type} в строке {token.line}")
        self.pos += 1
        return token

    def skip_newlines(self):
        while self.peek() and self.peek().type == "NEWLINE":
            self.consume()

    def parse_document(self):
        self.skip_newlines()
        result = {}

        while self.peek():
            if self.peek().type == "INDENT":
                indent = self.consume("INDENT")
                if indent.value != 0:
                    while self.peek() and self.peek().type != "NEWLINE":
                        self.consume()
                    if self.peek() and self.peek().type == "NEWLINE":
                        self.consume("NEWLINE")
                    continue

            if self.peek().type == "KEY":
                key = self.consume("KEY").value
                self.consume("COLON")

                if self.peek() and self.peek().type == "STRING":
                    value = self.consume("STRING").value
                    result[key] = value
                elif self.peek() and self.peek().type == "NEWLINE":
                    self.consume("NEWLINE")
                    value = self.parse_block(2)
                    result[key] = value if value is not None else []
                else:
                    result[key] = None

                if self.peek() and self.peek().type == "NEWLINE":
                    self.consume("NEWLINE")
            else:
                self.consume()

        return result

    def parse_block(self, expected_indent: int):
        start_pos = self.pos

        self.skip_newlines()
        if not self.peek():
            return None

        if self.peek().type == "INDENT":
            indent = self.consume("INDENT")

            if indent.value < expected_indent:
                self.pos = start_pos
                return None

            if indent.value > expected_indent:
                raise SyntaxError(f"Неожиданный отступ {indent.value} в строке {indent.line}")

            if self.peek() and self.peek().type == "DASH":
                self.pos = start_pos
                return self.parse_list(expected_indent)
            elif self.peek() and self.peek().type == "KEY":
                self.pos = start_pos
                return self.parse_object(expected_indent)

        return None

    def parse_list(self, expected_indent: int):
        items = []

        while self.peek():
            start_pos = self.pos

            self.skip_newlines()
            if not self.peek():
                break

            if self.peek().type != "INDENT":
                break

            indent = self.consume("INDENT")

            if indent.value < expected_indent:
                self.pos = start_pos
                break

            if indent.value > expected_indent:
                raise SyntaxError(f"Неожиданный отступ {indent.value} в строке {indent.line}")

            if self.peek() and self.peek().type == "DASH":
                self.consume("DASH")

                current_item = {}

                if self.peek() and self.peek().type == "KEY":
                    key = self.consume("KEY").value
                    self.consume("COLON")
                    if self.peek() and self.peek().type == "STRING":
                        value = self.consume("STRING").value
                        current_item[key] = value

                while self.peek():
                    item_start_pos = self.pos

                    self.skip_newlines()
                    if not self.peek():
                        break

                    if self.peek().type != "INDENT":
                        break

                    item_indent = self.consume("INDENT")

                    if item_indent.value < expected_indent + 2:
                        self.pos = item_start_pos
                        break

                    if item_indent.value > expected_indent + 2:
                        raise SyntaxError(f"Неожиданный отступ {item_indent.value} в строке {item_indent.line}")

                    if self.peek() and self.peek().type == "KEY":
                        key = self.consume("KEY").value
                        self.consume("COLON")

                        if self.peek() and self.peek().type == "STRING":
                            value = self.consume("STRING").value
                            current_item[key] = value
                        elif self.peek() and self.peek().type == "NEWLINE":
                            self.consume("NEWLINE")
                            nested_value = self.parse_block(expected_indent + 4)
                            current_item[key] = nested_value if nested_value is not None else {}
                        else:
                            current_item[key] = None

                        if self.peek() and self.peek().type == "NEWLINE":
                            self.consume("NEWLINE")
                    else:
                        self.pos = item_start_pos
                        break

                items.append(current_item)
            else:
                self.pos = start_pos
                break

            if self.peek() and self.peek().type == "NEWLINE":
                self.consume("NEWLINE")

        return items

    def parse_object(self, expected_indent: int):
        obj = {}

        while self.peek():
            start_pos = self.pos

            self.skip_newlines()
            if not self.peek():
                break

            if self.peek().type != "INDENT":
                break

            indent = self.consume("INDENT")

            if indent.value < expected_indent:
                self.pos = start_pos
                break

            if indent.value > expected_indent:
                raise SyntaxError(f"Неожиданный отступ {indent.value} в строке {indent.line}")

            if self.peek() and self.peek().type == "KEY":
                key = self.consume("KEY").value
                self.consume("COLON")

                if self.peek() and self.peek().type == "STRING":
                    value = self.consume("STRING").value
                    obj[key] = value
                elif self.peek() and self.peek().type == "NEWLINE":
                    self.consume("NEWLINE")
                    nested_value = self.parse_block(expected_indent + 2)
                    obj[key] = nested_value if nested_value is not None else {}
                else:
                    obj[key] = None

                if self.peek() and self.peek().type == "NEWLINE":
                    self.consume("NEWLINE")
            else:
                self.pos = start_pos
                break

        return obj if obj else None

def serialize_binary(obj: Any) -> bytes:
    if obj is None:
        return b'\x00'
    elif isinstance(obj, bool):
        return b'\x01' + (b'\x01' if obj else b'\x00')
    elif isinstance(obj, int):
        return b'\x02' + struct.pack('>q', obj)
    elif isinstance(obj, float):
        return b'\x03' + struct.pack('>d', obj)
    elif isinstance(obj, str):
        encoded = obj.encode('utf-8')
        length = len(encoded)
        return b'\x04' + struct.pack('>I', length) + encoded
    elif isinstance(obj, list):
        result = b'\x05' + struct.pack('>I', len(obj))
        for item in obj:
            result += serialize_binary(item)
        return result
    elif isinstance(obj, dict):
        result = b'\x06' + struct.pack('>I', len(obj))
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValueError("Ключи должны быть строками")
            result += serialize_binary(key)
            result += serialize_binary(value)
        return result
    else:
        raise TypeError(f"Неподдерживаемый тип: {type(obj)}")

def deserialize_binary(data: bytes) -> Any:
    return _deserialize(data, 0)[0]
def _deserialize(data: bytes, position: int) -> tuple[Any, int]:
    if position >= len(data):
        raise ValueError("Неожиданный конец данных")
    type_byte = data[position:position + 1]
    position += 1
    if type_byte == b'\x00':
        return None, position
    elif type_byte == b'\x01':
        value = data[position:position + 1]
        position += 1
        return value == b'\x01', position
    elif type_byte == b'\x02':
        value = struct.unpack('>q', data[position:position + 8])[0]
        position += 8
        return value, position
    elif type_byte == b'\x03':
        value = struct.unpack('>d', data[position:position + 8])[0]
        position += 8
        return value, position
    elif type_byte == b'\x04':
        length = struct.unpack('>I', data[position:position + 4])[0]
        position += 4
        value = data[position:position + length].decode('utf-8')
        position += length
        return value, position
    elif type_byte == b'\x05':
        length = struct.unpack('>I', data[position:position + 4])[0]
        position += 4
        result = []
        for _ in range(length):
            item, position = _deserialize(data, position)
            result.append(item)
        return result, position
    elif type_byte == b'\x06':
        length = struct.unpack('>I', data[position:position + 4])[0]
        position += 4
        result = {}
        for _ in range(length):
            key, position = _deserialize(data, position)
            value, position = _deserialize(data, position)
            result[key] = value
        return result, position
    else:
        raise ValueError(f"Неизвестный тип байта: {type_byte}")


def yaml_to_binary(yaml_text: str) -> bytes:
    tokens = tokenize(yaml_text)
    parser = Parser(tokens)
    ast = parser.parse_document()
    binary_data = serialize_binary(ast)
    return binary_data

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

def binary_to_ron(binary_data: bytes) -> str:
    python_obj = deserialize_binary(binary_data)
    ron_text = to_ron_pretty(python_obj)
    return ron_text


def yaml_to_ron_via_binary(yaml_text: str) -> str:
    binary_data = yaml_to_binary(yaml_text)
    ron_result = binary_to_ron(binary_data)
    return ron_result

if __name__ == "__main__":
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            yaml_content = f.read()

        binary_data = yaml_to_binary(yaml_content)
        print("Результат бинарного перевода:")
        print(binary_data)
        bin_file = sys.argv[1].replace('.yaml', '.bin').replace("in", "out", 1)
        with open(bin_file, 'wb') as f:
            f.write(binary_data)
        print(f"Бинарный объект сохранен в {bin_file}")

        result = yaml_to_ron_via_binary(yaml_content)
        print("Результат RON:")
        print(result)
        output_file = sys.argv[1].replace('.yaml', '.ron').replace("in", "out", 1)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f"\nРезультат сохранен в {output_file}")

    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)