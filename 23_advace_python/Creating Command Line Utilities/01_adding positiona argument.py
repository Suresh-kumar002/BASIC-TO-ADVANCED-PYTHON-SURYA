import argparse

parser = argparse.ArgumentParser()

parser.add_argument("positional", help="description of positional argument")

args = parser.parse_args()

print(args.positional)