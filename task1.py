from datetime import datetime

def get_days_from_today(date_string: str) -> int:
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d").date()
        today = datetime.today().date()
        diff = today - date
        return diff.days
    except ValueError:
        raise ValueError("Invalid date format, please use YYYY-MM-DD")