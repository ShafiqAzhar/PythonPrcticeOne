has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible to get loan")
else:
    print("Not eligible to get loan")

if has_good_credit or has_high_income:
    print("Eligible to get loan")
else:
    print("Not eligible to get loan")

if has_good_credit and not has_criminal_record:
    print("Eligible to get loan")
else:
    print("Not eligible to get loan")

if has_good_credit or not has_criminal_record:
    print("Eligible to get loan")
else:
    print("Not eligible to get loan")

