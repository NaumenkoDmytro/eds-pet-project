import json


def write_result(result: dict, path: str) -> None:
    with open(path, 'w') as json_file:
        json.dump(result, json_file, indent=4, ensure_ascii=False)
    print("Data has been written to ./result/result.json")
