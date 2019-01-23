#! python3

import argparse
import os
import json


def load_config():
    parser = argparse.ArgumentParser(
        description='pyclient',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cfg", default="./config.json",
                        help="configure file", type=str)
    args = parser.parse_args()

    jsonfile = os.path.abspath(os.path.dirname(__file__)) + "/" + args.cfg
    if not os.path.exists(jsonfile):
        print("ERROR: cfg file not found. path = ", jsonfile)
        exit(0)

    f = open(jsonfile, 'rt')
    cfg = json.loads(f.read())
    f.close()
    return args, cfg
