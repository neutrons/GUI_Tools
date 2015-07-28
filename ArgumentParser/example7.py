import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="Number to square")
parser.add_argument("-v", "--verbose", type=int, choices=[0,1,2], 
                    help='verbose mode')
args = parser.parse_args()
answer = args.square**2
if args.verbose == 2:
    print("(%d)^2 = %d"%(args.square, answer))
elif args.verbose == 1:
    print("answer is: %d" %answer)
else:
    print("Done!")

