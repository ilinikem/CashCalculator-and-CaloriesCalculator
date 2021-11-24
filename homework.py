import datetime as dt

FORMAT = '%d.%m.%Y'


class Record:
    '''
    Make records about spent cash or calories, date and comment.
    '''
    def __init__(self, amount, date=None, comment='') -> None:
        self.amount = amount
        self.date = (dt.datetime.strptime(date, FORMAT).date()
                     if date else dt.date.today())
        self.comment = comment


class Calculator:
    '''
    Define limit calories or cash, have methods add_record, get_today_stats,
    get_week_stats
    '''
    def __init__(self, limit) -> None:
        self.limit = limit
        self.records: list = []

    def add_record(self, record) -> None:
        '''
        To add data object "Record" to list
        '''
        self.records.append(record)

    def get_today_stats(self) -> int:
        '''
        To calculate value that spend for today
        '''
        sum = 0
        for i in self.records:
            if i.date == dt.date.today():
                sum += i.amount
        return sum

    def get_week_stats(self) -> int:
        '''
        To calculate value that spend for one week
        '''
        sum_week = 0
        today = dt.datetime.now().date()
        delta = dt.timedelta(days=6)
        early_week = today - delta
        for i in self.records:
            if early_week <= i.date <= today:
                sum_week += i.amount
        return sum_week


class CaloriesCalculator(Calculator):
    '''
    Class for calculate calories, have method get_calories_remained
    '''
    def get_calories_remained(self):
        '''
        Count how many calories have already been eaten today
        '''
        balance = self.limit - self.get_today_stats()
        if balance > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с'
                    f' общей калорийностью не более {balance} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    '''
    Class for calculate money, have method get_today_cash_remained
    '''
    USD_RATE = 72.5
    EURO_RATE = 84.5

    def get_today_cash_remained(self, currency='rub'):
        '''
        Count how much money have already been spent today
        '''
        exchage = {'rub': (1.0, 'руб'),
                   'usd': (self.USD_RATE, 'USD'),
                   'eur': (self.EURO_RATE, 'Euro')}

        balance = self.limit - self.get_today_stats()
        rate, coin = exchage[currency]
        money = round(balance/rate, 2)
        if balance > 0:
            return f'На сегодня осталось {money} {coin}'
        elif balance == 0:
            return 'Денег нет, держись'
        else:
            money = abs(money)
            return f'Денег нет, держись: твой долг - {money} {coin}'


r1 = Record(9000, '20.11.2021')
r2 = Record(2000)
maksim = CaloriesCalculator(10000)
maksim.add_record(r1)
maksim.add_record(r2)
print(maksim.get_calories_remained())
