import argparse

parser = argparse.ArgumentParser(description='Convert base2, base10 and base16 numbers')

parser.add_argument('-it', type=str, required=True, help='Input Type')
parser.add_argument('-n', type=str, required=True, help='Number')
parser.add_argument('-ot', type=str, required=True, help='Output Type')

args = parser.parse_args()

def matchoutputtype(number, outputtype):
    match outputtype:
        case 'D' | '10':
            print(f"Decimal output: {number}\n")
        case 'X' | '16':
            print(f"Hexadecimal output: {str(hex(number))[2:].upper()}\n")
        case 'B' | '2':
            print(f"Binary output: {str(bin(number))[2:]}\n")
        case _:
            print("ERROR: Invalid output type")

def main(inputtype, number, outputtype):
    match inputtype:
        case 'D' | '10':
            print(f"Decimal input: {number}")
            matchoutputtype(int(number), outputtype)
        case 'X' | '16':
            print(f"Hexadecimal input: {number}")
            matchoutputtype(int(number, 16), outputtype)
        case 'B' | '2':
            print(f"Binary input: {number}")
            matchoutputtype(int(number, 2), outputtype)
        case _:
            print("ERRROR: Invaild input type")

if __name__ == '__main__':
    main(args.it.upper(),args.n,args.ot.upper())