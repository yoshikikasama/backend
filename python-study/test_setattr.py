class Sample:
    def __init__(self, params):
        keys = ['name']
        for key in keys:
            if key not in params:
                raise KeyError(key)
            setattr(self, key, params[key])


d = {'name': 'take'}
Tom = Sample(d)
print(Tom.name)
