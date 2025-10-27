from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        
        if 0 <= delta_days < 7:
            if birthday_this_year.weekday() >= 5:
                if birthday_this_year.weekday() == 5:
                    congratulation_date = birthday_this_year + timedelta(days=2)
                else:
                    congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
            
    return upcoming_birthdays

# Приклад використання
# Встановлюємо дату для тестування, наприклад, 27 жовтня 2025 (понеділок)
# Тестові дати: сьогодні - 2025.10.27
# John Doe: 1985.01.23 -> 2026.01.23 (не входить в наступні 7 днів)
# Jane Smith: 1990.01.27 -> 2025.01.27 (минулий) -> 2026.01.27 (не входить)
# Sam Wilson: 1992.10.25 -> 2025.10.25 (минулий) -> 2026.10.25 (субота, переноситься на 27.10.2026)
# Lana Lane: 1993.10.26 -> 2025.10.26 (неділя, переноситься на 27.10.2025)
# Pete: 1991.10.30 -> 2025.10.30 (четвер)
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Sam Wilson", "birthday": "1992.10.25"},
    {"name": "Lana Lane", "birthday": "1993.10.26"},
    {"name": "Pete", "birthday": "1991.10.30"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)