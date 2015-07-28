import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
group.add_argument("-q", "--quiet", help="quiet", action="store_true")
args = parser.parse_args()
if args.quiet:
    print('mode quiet is ON')
elif args.verbose:
    print('mode verbose is ON')
else:
    print("Neither quiet or verbose are on")


