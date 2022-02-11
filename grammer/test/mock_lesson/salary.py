import requests

class ThirdPartyBonusRestApi():
    def bonus_price(self, year):
        # paramは query parameterになる
        r = requests.get('http://localhost/bonus', params={'year': year})
        # {"price": 100}
        return r.json()['price']

class Salary():
    def __init__(self, base=100, year=2017):
        self.bonus_api = ThirdPartyBonusRestApi()
        self.base = base
        self.year = year
    
    def calculation_salary(self):
        bonus = 0
        if self.year < 2021:
            bonus = self.bonus_api.bonus_price(year=self.year)
        return self.base + bonus