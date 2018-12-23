import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-x')

args = parser.parse_args()

if args.x:
    print("-x is present")
    print("value: " + vars(args)["x"])
else:
    print("-x is not present")