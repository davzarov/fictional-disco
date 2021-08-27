"""
# Title
Python script to convert cookies to [Netscape format](https://curl.se/docs/http-cookies.html) 
to consume in applications like `curl`, `wget` or `youtube-dl`.

## Netscape format
* domain: the domain name.
* flag: include subdomains.
* path: path.
* secure: send/receive over HTTPS only.
* expiration: seconds since Jan 1st 1970, or 0.
* name: name of the cookie.
* value: value of the cookie.

## Requirements
* [Python](https://www.python.org/downloads/)
* Cookies copied from Chrome DevTool Application Tab
"""

from pathlib import Path

from utils import is_empty, list_files, make_directory, make_file, open_file
from utils.parsing import to_boolean, to_dict, to_domain, to_timestamp

BASE_DIR = Path(__file__).resolve().parent
FILES_DIR = BASE_DIR / "files"
COOKIES_DIR = BASE_DIR / "cookies"


def main() -> None:
    # make files and cookies directories
    created, files_dir = make_directory(FILES_DIR)
    _, cookies_dir = make_directory(COOKIES_DIR)

    if is_empty(files_dir):
        if created:
            print("[Info]: dirs created, get some cookies and run again.")
        else:
            print("[Error]: files dir is empty, try again later.")
        return

    for file in list_files(files_dir):
        print(f"processing {file.name}...")
        cookies = open_file(file)
        # clean empty list elements
        cookies = list(filter(None, cookies))
        # touch output file in cookies dir
        output_file = make_file(cookies_dir, file)
        # list of formatted cookies
        formatted_cookies = ["# Netscape HTTP Cookie File", ]

        for row in cookies:
            # access each cookie as a dictionary
            cookie = to_dict(row)
            # get all values
            domain = to_domain(cookie["domain"])
            flag = "TRUE"
            path = cookie["path"]
            secure = to_boolean(cookie["secure"])
            expiration = to_timestamp(cookie["expires"])
            name = cookie["name"]
            value = cookie["value"]
            # append cleaned values separated by tabs
            formatted_cookies.append(
                "\t".join([domain, flag, path, secure,
                          expiration, name, value]))
        # write each cleaned cookie to the output file
        output_file.write_text("\n".join(formatted_cookies))

    print("[Done]: all files converted to Netscape format.")


if __name__ == "__main__":
    main()
