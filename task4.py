from datetime import datetime, timedelta, date

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = get_birthday_this_year(birthday, today)

        days_to_birthday_this_year = (birthday_this_year - today).days
        if 0 <= days_to_birthday_this_year <= 7:
            congratulation_date = get_congratulation_date(birthday)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming

def get_birthday_this_year(birthday: date, today: date) -> date:
    birthday_this_year = birthday.replace(year=today.year)
    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)
    return birthday_this_year

def get_congratulation_date(birthday: date) -> date:
    if birthday.weekday() == 5:  # субота
        return birthday + timedelta(days=2)
    elif birthday.weekday() == 6:  # неділя
        return birthday + timedelta(days=1)
    else:
        return birthday