import datetime


def fee_settlement(carIn, carExit):
    defult_fee = 10000
    defult_time = datetime.timedelta(minutes=30)
    ten_minutes = datetime.timedelta(minutes=10)
    ten_fee = 1500
    two_day = datetime.timedelta(days=2)

    if carExit:
        fee_time = carExit - carIn
        if fee_time == defult_time:
            fee = defult_fee
            return fee
        elif fee_time > defult_time:
            fee = ((fee_time - defult_time) / ten_minutes) * ten_fee + defult_fee
            if 20000 <= fee < 30000:
                fee = fee * 0.9
                return fee
            elif fee >= 30000:
                fee = 30000
            return fee
        else:
            return "Free"

    else:
        return "None"


a = datetime.datetime.now()
b = datetime.timedelta(days=3)
c = a + b
d = datetime.datetime.now()
print(fee_settlement(a, c))
# print(a + b)
e = datetime.timedelta(days=7)
# print(e)
