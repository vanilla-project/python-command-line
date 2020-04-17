import sys
from sample.example import Example


class Main:
    def __init__(self, stdout):
        self._stdout = stdout

    def run(self):
        example = Example()

        self._stdout.write(f"{example.greeting()}\n")


if __name__ == "__main__":
    Main(sys.stdout).run()

