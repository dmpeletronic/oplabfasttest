import argparse
import sys
sys.path.append('src')
from operations import operations

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bignumber")
    args = parser.parse_args()
    print(operations.get_operations(args.bignumber))


if __name__ == '__main__':
    main()
    