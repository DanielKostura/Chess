from pathlib import Path
from os import remove

def open_file(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines

def write_file(file_path: str, lines: list[str]) -> None:
    with open(file_path, "w") as f:
        f.writelines(lines)

def append_file(file_path: str, text: str) -> None:
    with open(file_path, "a") as f:
        f.write(text)

def delete_file(file_path: str) -> None:
    remove(file_path)

def open_directory(directory: str) -> list[str]:
    path = Path(directory)

    if not path.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    return [item.name for item in path.iterdir() if item.is_file()]

def only_txt_files(files: list[str]) -> list[str]:
    return [file[:-4] for file in files if file.endswith(".txt")]

def parse_opening_variants(file: str) -> dict[int, tuple[str, list[str]]]:
        variants: dict[int, tuple[str, list[str]]] = {}
        lines = open_file(f"openings/{file}")

        for i, line in enumerate(lines):
            name, moves_str = line.split(":", 1)
            moves = moves_str.strip().split()
            variants[i] = (name.strip(), moves)

        return variants