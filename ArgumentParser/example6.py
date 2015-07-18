import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="Number to square")
parser.add_argument("-v", "--verbose", help='verbose mode', action='store_true')
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("(%d)^2 = %d"%(args.square, answer))

