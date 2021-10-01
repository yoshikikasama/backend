import abc


# metaclass=abc.ABCMeta→抽象クラスであるということを表している
class Person(metaclass=abc.ABCMeta):
    def __init__(self, age=1):
        self.age = age

    # @abc.abstractmethod→継承先で必ず実装して下さいとなる
    @abc.abstractmethod
    def drive(self):
        pass


class Baby(Person):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        raise Exception('No drive')


class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('ok')


baby = Baby()
adult = Adult()


class Car():
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')

    def ride(self, person):
        person.drive()


class ToyotaCar(Car):
    pass


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        self._enable_auto_run = is_enable


car = Car()
car.run()
car.ride(adult)
toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar('Model A')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
