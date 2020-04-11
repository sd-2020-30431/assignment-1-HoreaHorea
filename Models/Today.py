from datetime import date, datetime, timedelta

# idk how to make a better static instance

now_date = datetime.today()


def today_date():
    global now_date
    return datetime.strptime(now_date, '%Y-%m-%d')


def today():
    global now_date
    now_date = datetime.today()


def tomorrow():
    global now_date
    now_date += timedelta(days=1)


def yesterday():
    global now_date
    now_date = now_date + timedelta(days=-1)

#
# print(now_date)
# tomorrow()
# print(now_date)
