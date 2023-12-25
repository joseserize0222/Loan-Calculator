import argparse
from math import log, ceil, floor

def calculate_payment(principal : float, interest : float, periods: int):
    aux = pow((1 + interest), periods)
    result = (principal * (interest * aux))/(aux - 1)
    return result


def calculate_principal(payment : float, interest :float, periods : int):
    aux = pow((1 + interest), periods)
    result = payment / ((interest * aux)/(aux - 1))
    return result

def calculate_periods(payment : float, principal : float, interest : int):
    result = ceil(log( (payment/(payment - interest*principal) ) , 1 + interest))
    return result

def annuity(payment, principal, periods, interest):
    if not payment:
        try:
            principal = float(principal)
            periods = int(periods)
            if principal < 0 or periods < 0:
                raise ValueError
            payment = calculate_payment(principal, interest, periods)
        except (ValueError, ZeroDivisionError):
            print("Incorrect parameters")
            exit()
        else:
            print(f"Your monthly payment = {ceil(payment)}!")
    if not principal:
        try:
            payment = float(payment)
            periods = int(periods)
            if payment < 0 or periods < 0:
                raise ValueError
            principal = calculate_principal(payment, interest, periods)
        except (ValueError, ZeroDivisionError):
            print("Incorrect parameters")
            exit()
        else:
            print(f"Your loan principal = {floor(principal)}!")
    if not periods:
        try:
            payment = float(payment)
            principal = float(principal)
            if payment < 0 or principal < 0:
                raise ValueError
            periods = calculate_periods(payment, principal, interest)
        except (ValueError, ZeroDivisionError):
            print("Incorrect parameters")
            exit()
        else:
            string = "It will take "
            if periods < 12:
                string += f"{periods} months " if periods > 1 else f"{periods} month "
            else:
                string += f"{periods // 12} years " if periods // 12 > 1 else f"{periods // 12} year "
                if periods % 12 != 0:
                    string += f"and {periods % 12} months " if periods % 12 > 1 else f"and {periods % 12} month "
            string += "to repay this loan!"
            print(string)
    print(f"Overpayment = {ceil(ceil(payment) * periods - principal)}")

def diff_payment(principal, periods, interest):
    try:
        principal = float(principal)
        periods = int(periods)
        interest = float(interest)
        if principal < 0 or periods < 0 or interest < 0:
            raise ValueError
        sum = 0
        for m in range(1,periods+1):
            res = ceil(principal/periods + interest*(principal - (principal*(m-1))/periods))
            sum += res
            print(f"Month {m}: payment is {res}")
        print()
        overpayment = sum - principal
        print(f"Overpayment = {ceil(overpayment)}")
    except (ValueError, ZeroDivisionError):
        print("Incorrect parameters")
        return


parser = argparse.ArgumentParser(description = "This program is for calculating some stuff")
parser.add_argument("--type", default=False)
parser.add_argument("--payment", default=False)
parser.add_argument("--principal", default=False)
parser.add_argument("--periods", default=False)
parser.add_argument("--interest", default=False)

args = parser.parse_args()
type = args.type
payment = args.payment
principal = args.principal
periods = args.periods
interest = args.interest

if not type or (type != "diff" and type != "annuity") or not interest:
    print("Incorrect parameters")
    exit()
try:
    interest = float(interest)
    interest /= 1200
    if interest < 0:
        raise ValueError
except ValueError:
    print("Incorrect parameters")
    exit()

cnt = 0

for arg in vars(args):
    #  print(f"{arg}: {getattr(args, arg)}")
    if not getattr(args, arg):
        cnt += 1

if cnt != 1:
    print("Incorrect parameters")
    exit()

if type == "annuity":
    annuity(payment, principal, periods, interest)

if type == "diff":
    if not periods or not interest or not principal:
        print("Incorrect parameters")
        exit()
    diff_payment(principal,periods,interest)
