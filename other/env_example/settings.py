class CommonEnv:
    def __init__(self, sample_a, sample_b):
        self.__sample_a = sample_a
        self.__sample_b = sample_b

    # gettter method
    @property
    def sample_a(self):
        return self.__sample_a

    @property
    def sample_b(self):
        return self.__sample_b


class SpecialEnv:
    def __init__(self, sample_c):
        self.__sample_c = sample_c
        self.__messages = []

    # gettter method
    @property
    def sample_c(self):
        return self.__sample_c


    @property
    def messages(self):
        return self.__messages

    # setter method
    @messages.setter
    def messages(self, messages):
        self.__messages.append(messages)