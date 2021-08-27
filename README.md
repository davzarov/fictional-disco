# fictional-disco
Python script to convert cookies to [Netscape format](https://curl.se/docs/http-cookies.html) to consume in applications like `curl`, `wget` or `youtube-dl`.

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