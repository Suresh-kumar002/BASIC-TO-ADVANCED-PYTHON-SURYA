import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--optional", help="description of optional argument", default="default_value")

args = parser.parse_args()

print(args.optional)