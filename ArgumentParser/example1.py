import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo1", help='echo the string you use here')  # mandatory argument
args = parser.parse_args()
print(args.echo1)