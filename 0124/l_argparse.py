import argparse


def option_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo")
    parser.add_argument("square", help="square number", type=int)
    parser.add_argument("-v","--vers", help="option check", action="store_true")
    args = parser.parse_args()
    print(args.echo)
    print(args.square**2)
    if args.vers:
        print("test test test")

def main():
    option_parser()


if __name__ == '__main__':
    main()
