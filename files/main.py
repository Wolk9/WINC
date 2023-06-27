__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from zipfile import ZipFile

base_path = os.getcwd()
cache_path = os.path.join(base_path, "cache")
data_path = os.path.join(base_path, "data.zip")


def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir("cache")


def cache_zip(zip, cache):
    with ZipFile(zip, "r") as zipObj:
        zipObj.extractall(cache)


def cached_files():
    cached_files_list = []
    for path in os.listdir(cache_path):
        full_path = os.path.join(cache_path, path)
        cached_files_list.append(full_path)
    print(cached_files_list)
    return cached_files_list


def find_password(list_of_files):
    for file in list_of_files:
        with open(file) as f:
            for line in f:
                if "password" in line:
                    split_line = line.split(" ", 1)
                    result = split_line[1].replace("\n", "")
                    print(result)
                    return result
