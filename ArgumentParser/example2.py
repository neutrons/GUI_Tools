import argparse
parser = argparse.ArgumentParser()
parser.add_argument("factor1", help='factor 1')
parser.add_argument("factor2", help='factor 2')
args = parser.parse_args()
print("Value of factor1 is: %s" %args.factor1)
print("Value of factor2 is: %s" %args.factor2)
