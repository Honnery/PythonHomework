import pycalc.difcalc as difcalc
import pycalc.CheckAndChange as CheckAndChange
import argparse


calculator = difcalc.ComplexCalc()
cheker = CheckAndChange. CheckAndChange()

parser = argparse.ArgumentParser(description='Calculation')
parser.add_argument('a', type=str, help='input your expression')
parser.add_argument('-m', type=str, help='your oun module ')
args = parser.parse_args()


def start():

    try:

        if args.a != "--help":

            a = cheker.do_all_changes(args.a, args.m)
            a = calculator.calculate(args.a)

        else:
            print("help yourself")

    except Exception as e:
        print("ERROR:  " + str(e))
    else:
        print(a)
