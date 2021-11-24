# Калькулятор денег и калорий

Два калькулятора: для подсчёта денег и калорий. Написана только логика — отдельный класс для каждого из калькуляторов.

# Калькулятор денег умеет:
- Сохранять новую запись о расходах методом <code>add_record()</code>
- Считать, сколько денег потрачено сегодня методом <code>get_today_stats()</code>
- Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод <code>get_today_cash_remained(currency)</code>
- Считать, сколько денег потрачено за последние 7 дней — метод <code>get_week_stats()</code>

# Калькулятор калорий умеет:
- Сохранять новую запись о приёме пищи— метод <code>add_record()</code>
- Считать, сколько калорий уже съедено сегодня — метод <code>get_today_stats()</code>
- Определять, сколько ещё калорий можно/нужно получить сегодня — метод <code>get_calories_remained()</code>
- Считать, сколько калорий получено за последние 7 дней — метод <code>get_week_stats()</code>

## Инструкция по установке

Клонируем репозиторий 

<code>git clone https://github.com/ilinikem/CashCalculator-and-CaloriesCalculator.git</code>

Переходим в папку с проектом

<code>Calculator-and-CaloriesCalculator</code>

Устанавливаем отдельное виртуальное окружение для проекта

<code>python -m venv venv</code>

Активируем виртуальное окружение

<code>venv\Scripts\activate</code>

Устанавливаем модули необходимые для работы проекта

<code>pip install -r requirements.txt</code>

# Требования
Python 3.7 +

Работает под ОС Linux, Windows, macOS, BSD
