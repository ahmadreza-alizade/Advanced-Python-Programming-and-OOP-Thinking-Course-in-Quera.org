from datetime import datetime


def day_calculator(date):
    sajad_dt = "1999-01-14"
    sajad_birth = list(map(int, sajad_dt.split("-")))
    sajad_dt = datetime(*sajad_birth)

    date = list(map(int, date.split("-")))
    date = datetime(*date)

    difftime = date - sajad_dt
    diff_days = difftime.days

    if diff_days > 0:
        return (diff_days)
    else:
        return ("Not yet born")


