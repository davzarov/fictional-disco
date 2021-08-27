import os
import shutil
from pathlib import Path
from typing import Generator, List, Tuple


def open_file(f: Path) -> List[str]:
    """opens raw file and returns cookies"""
    if not f.exists():
        raise FileExistsError("File doesn't exist.")

    if f.suffix != '.txt':
        raise TypeError("File must be of type .txt")

    cookies = f.read_text().split("\n")
    return cookies


def list_files(dir: Path) -> Generator[Path, None, None]:
    """list files in a directory"""
    for f in dir.iterdir():
        if f.exists() and f.is_file():
            yield f


def make_directory(dir: Path) -> Tuple[bool, Path]:
    """creates directory in the desired path"""
    created = False
    if not dir.exists():
        try:
            dir.mkdir(parents=True)
            created = True
        except FileExistsError:
            pass
        else:
            print(f"[Created]: {dir.name} directory.")
    return created, dir


def is_empty(dir: Path) -> bool:
    """checks if directory is empty"""
    return not any(dir.iterdir())


def make_file(dir: Path, f: Path):
    """outputs a file in a dir using the current file features"""
    output = dir / (f"{f.stem}_cookies{f.suffix}")

    if not output.exists():
        output.touch()

    return output


def move_file(o: Path, d: Path) -> None:
    """moves file from o (origin) to d (destination)"""
    shutil.move(os.fspath(o), os.fspath(d))


def copy_file(o: Path, d: Path) -> None:
    """moves file from o (origin) to d (destination)"""
    shutil.copy(os.fspath(o), os.fspath(d))


def remove_file(f: Path) -> None:
    """removes file or link passed"""
    f.unlink()
