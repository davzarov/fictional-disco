"""
https://unix.stackexchange.com/questions/36531/format-of-cookies-when-using-wget

Netscape format:

-------------------------------------------------------------
| domain | flag | path | secure | expiration | name | value |
-------------------------------------------------------------

domain: The domain that created AND that can read the variable.

flag: A TRUE/FALSE value indicating if all machines within a given
domain can access the variable. This value is set automatically by
the browser, depending on the value you set for domain.

path: The path within the domain that the variable is valid for.

secure: A TRUE/FALSE value indicating if a secure connection with
the domain is needed to access the variable.

expiration: The UNIX time that the variable will expire on. UNIX
time is defined as the number of seconds since Jan 1, 1970 00:00:00 GMT.

name: The name of the variable.

value: The value of the variable.
"""

import os
import shutil
from pathlib import Path
from typing import Generator, List

BASE_DIR = Path(__file__).resolve().parent
FILES_DIR = BASE_DIR / "files"
COOKIES_DIR = BASE_DIR / "cookies"


def open_file(f: Path) -> List[str]:
    if not f.exists():
        raise FileExistsError

    if f.suffix != '.txt':
        raise TypeError

    cookies = f.read_text().split("\n")
    return cookies


def list_files(dir: Path) -> Generator[Path, None, None]:
    for f in dir.iterdir():
        if f.exists() and f.is_file():
            yield f


def make_directory(dir: Path) -> Path:
    if not dir.exists():
        try:
            dir.mkdir(parents=True)
        except FileExistsError:
            pass
        else:
            print(f"directory {dir.name} created.")
    return dir


def make_cookie_file(f: Path):
    output = COOKIES_DIR / (f"{f.stem}_cookies{f.suffix}")

    if not output.exists():
        output.touch()

    return output


def move_file(o: Path, d: Path) -> None:
    shutil.move(os.fspath(o), os.fspath(d))


def copy_file(o: Path, d: Path) -> None:
    shutil.copy(os.fspath(o), os.fspath(d))


def remove_file(f: Path) -> None:
    f.unlink()
