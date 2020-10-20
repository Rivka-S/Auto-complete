import json
import os
import re
from json.decoder import JSONDecodeError

files = []  # to ask margalit, if not change


def from_key_to_regulars(key):
    regulars = []
    for index, k in enumerate(key):
        if 0 < index < len(key):
            regulars.append(key[:index] + '.' + key[index + 1:])

    return regulars


def sub_strings(line):
    sub_str = []
    line = re.sub(' +', ' ', line)
    line = "".join(re.split("[^a-zA-Z0-9 ]*", line))
    line = line.casefold()
    len_ = len(line)
    for i in range(1, len_):
        for j in range(i + 1, min(len_, i + 10)):
            sub_str.append(line[i:j])
            #sub_str.extend(from_key_to_regulars(line[i:j]))

    return sub_str


def read_from_file(file):  # to split to function and rename
    index_file = len(files) - 1
    # ==============================================
    print("FILE", file)
    # ==============================================
    for index_line, line in enumerate(file):
        if line.strip():
            substring = sub_strings(line)
            # ==================================
            print(substring)
            # ==================================
            for x in substring:
                score = len(x) * 2
                data = [index_file, index_line + 1, score]
                json_name = x[0] + ".json"

                # check if move to func
                cache = [{}]
                # if get expensive the time
                # ========================================
                print(json_name)
                # ========================================
                # if delete the files---

                if os.path.exists(os.path.join("json_files", json_name)):
                    with open(os.path.join("json_files", json_name), "r")as f:
                        try:
                            cache = json.load(f)
                        except JSONDecodeError:  # check
                            pass

                if not cache[0].get(x):  # cache[0]
                    cache[0][x] = []
                if len(cache[0][x]) == 5:
                    if cache[0][x][-1][2] < data[2]:
                        cache[0][x][-1] = data
                        cache[0][x].sort(reverse=True,key=lambda w: w[2])
                else:
                    cache[0][x].append(data)
                    cache[0][x].sort(reverse=True, key=lambda w: w[2])

                with open("json_files/" + json_name, "w") as f:
                    json.dump(cache, f)  # what is indent 4?

def read_root(root_name):
    for root_name, dirs, files_name in os.walk(root_name):
        for index,file in enumerate(files_name):
            with open(os.path.join(root_name, file), "r", encoding='utf8') as auto:
                files.append(auto.name)
                with open("files.json", "w") as ff:
                    json.dump(files, ff)
                print(auto.name)
                print(files)

                read_from_file(auto)


        print("==============end of init=================")


read_root("technology_texts")  # run function