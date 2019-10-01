import urllib.request
import os
import re


def check_result(__output_dir: str, __ext: str):
    check_counter = 0
    pattern = ".*" + __ext + "$"
    file = open("./source/squid_access_sorted.log", "r")
    for line in file:
        if re.search(pattern, line):
            check_counter += 1
    path, dirs, files = next(os.walk(__output_dir))
    if check_counter == len(files):
        print("All packages downloaded right")
    else:
        print("Not all packages downloaded. Please check files")
    file.close()


def make_filename(__url: str, __path: str):
    return __path + "/" + __url.split("/")[-1]


def download_package(__url: str, __ext: str, __output_dir: str):
    pattern = ".*" + __ext + "$"
    if re.search(pattern, __url):
        urllib.request.urlretrieve(__url, make_filename(__url, __output_dir))


def main(__output_dir: str, __source_file: str, __ext: str):
    if not os.path.exists(__output_dir):
        os.makedirs(__output_dir)
    file = open(__source_file, "r")
    for url in file:
        download_package(url, __ext, __output_dir)
    file.close()
    check_result(__output_dir, __ext)


if __name__ == "__main__":
    main("./packages", "./source/squid_access_sorted.log", "deb")
