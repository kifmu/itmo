import sys
from task_1 import deserialize_binary

def binary_to_xml(binary_data: bytes) -> str:
    data = deserialize_binary(binary_data)

    def to_xml(obj, tag="root"):
        if obj is None:
            return f'<{tag}>null</{tag}>'
        elif isinstance(obj, bool):
            return f'<{tag}>{str(obj).lower()}</{tag}>'
        elif isinstance(obj, (int, float)):
            return f'<{tag}>{obj}</{tag}>'
        elif isinstance(obj, str):
            return f'<{tag}><![CDATA[{obj}]]></{tag}>'
        elif isinstance(obj, list):
            items = [f'<{tag}>']
            for item in obj:
                items.append(to_xml(item, "item"))
            items.append(f'</{tag}>')
            return ''.join(items)
        elif isinstance(obj, dict):
            items = [f'<{tag}>']
            for key, value in obj.items():
                items.append(to_xml(value, str(key)))
            items.append(f'</{tag}>')
            return ''.join(items)
        else:
            return f'<{tag}>{obj}</{tag}>'

    return to_xml(data)


if __name__ == "__main__":
    with open(sys.argv[1], 'rb') as f:
        binary_data = f.read()

    xml_result = binary_to_xml(binary_data)
    print(xml_result)
    output_file = sys.argv[1].replace('.bin', '.xml').replace('in', 'out')
    with open(output_file, 'w') as f:
        f.write(xml_result)