from datetime import datetime, date

current_date = date.today()

def get_days_from_today(date_string: str) -> int:
    try:
        given_date = datetime.strptime(date_string, '%Y-%m-%d').date()
        days_difference = current_date - given_date
        return days_difference.days

    except ValueError:
        print("Помилка: Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'.")
        return None

# Приклад використання
print(get_days_from_today("2021-10-09"))
print(get_days_from_today(str(current_date)))
print(get_days_from_today("2020-01-01"))
print(get_days_from_today("Це явно не дата :)"))