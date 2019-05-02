#!/usr/bin/python3

import json
import os
import re


def main():
    """Go through dashboard json, replace cloudwatch data source names"""

    rootdir = 'path/to/dashboards'
    search_str = "CloudWatch-mondev"
    new_data = "BETTERCLOUDWATCH"

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = os.path.join(subdir, file)
            # print(filepath)
            with open(filepath, 'r') as json_file:
                data = json.load(json_file)
                if re.search(search_str, str(data)):
                    mod = str(data).replace(search_str, new_data)
                    new_json = eval(mod)
                    # print(type(new_json))
                    with open('d.json', 'w') as outfile:
                        json.dump(new_json, outfile, sort_keys=True, indent=2)
                else:
                    pass


if __name__ == "__main__":
    main()
