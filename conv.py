import argparse

parser = argparse.ArgumentParser(description='Convert base2, base10 and base16 numbers')

parser.add_argument('-it', type=str, required=True, help='Achieved points')
parser.add_argument('-n', type=int, required=True, help='Maximum points')
parser.add_argument('-ot', type=str, required=True, help='Maximum points')

args = parser.parse_args()

def main(inputtype, number, outputtype):
    match inputtype:
        case 'D':
            print("Decimal\n")
        case 'X':
            print("Hexadecimal\n")
        case 'B':
            print("Binary\n")
        case _:
            print("ERRROR: Invaild input type\n")

if __name__ == '__main__':
    main(args.it.upper(),args.n,args.ot.upper())