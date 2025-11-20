import time
import yaml
import sys

from task_1 import yaml_to_binary, binary_to_ron, to_ron_pretty, deserialize_binary
from task_3 import binary_to_xml


def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        yaml_content = f.read()

    print("Стократное время выполнения:")
    start = time.perf_counter()
    for _ in range(100):
        binary_data_custom = yaml_to_binary(yaml_content)
    time1 = (time.perf_counter() - start) * 1000
    print(f"YAML -> binary: {time1:.2f} мс")

    start = time.perf_counter()
    for _ in range(100):
        result = binary_to_ron(binary_data_custom)
    time2 = (time.perf_counter() - start) * 1000
    print(f"binary -> RON: {time2:.2f} мс")

    start = time.perf_counter()
    for _ in range(100):
        binary_data_temp = yaml_to_binary(yaml_content)
        result = binary_to_ron(binary_data_temp)
    time3 = (time.perf_counter() - start) * 1000
    print(f"YAML -> binary -> RON: {time3:.2f} мс")

    start = time.perf_counter()
    for _ in range(100):
        data = yaml.safe_load(yaml_content)
        result = to_ron_pretty(data)
    time4 = (time.perf_counter() - start) * 1000
    print(f"YAML -> RON: {time4:.2f} мс")

    start = time.perf_counter()
    for _ in range(100):
        binary_data_temp = yaml_to_binary(yaml_content)
        result = binary_to_xml(binary_data_temp)
    time5 = (time.perf_counter() - start) * 1000
    print(f"YAML -> binary -> XML: {time5:.2f} мс")


if __name__ == "__main__":
    main()