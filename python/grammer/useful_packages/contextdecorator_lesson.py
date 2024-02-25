import contextlib


class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = f'<{name}>'
        self.end_tag = f'/<{name}>'

    def __enter__(self):
        # classが呼び出された時に最初に実行される
        print(self.start_tag)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # classが呼び出された時に最後に実行される
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print(self.end_tag)


with tag('h2'):
    raise Exception('error')
    print('test')
