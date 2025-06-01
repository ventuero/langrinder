import json

TAB = " " * 4


def dump_to_pack(obj: dict) -> str:
    dumped = json.dumps(obj, indent=4, ensure_ascii=False)
    fixed_lines = []
    for idx, line in enumerate(dumped.split("\n")):
        if idx == 0:
            fixed_lines.append(line)
            continue
        fixed_lines.append(TAB + line)
    return "\n".join(fixed_lines)
