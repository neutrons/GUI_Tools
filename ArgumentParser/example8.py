import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--flag1", help='flag1', action="store_true")
parser.add_argument("-b", "--flag2", help='flag2', action="store_true")
args = parser.parse_args()
if args.flag1:
    print("Flag1 has been triggered")
if args.flag2:
    print("Flag2 has been trigerred")

