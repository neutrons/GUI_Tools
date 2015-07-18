import argparse
parser = argparse.ArgumentParser()
parser.add_argument("factor1", help='factor 1', type=int)
args = parser.parse_args()
print("Value of factor1 is: %d" %args.factor1)
