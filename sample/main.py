from sample.example import Example


class Main:
    def __init__(self, stdout):
        self._stdout = stdout

    def run(self):
        example = Example()

        self._stdout.write(example.greeting())

