import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--factor1", help='factor 1')
args = parser.parse_args()
if args.factor1:
    print(args.factor1)

