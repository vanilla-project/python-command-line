from io import StringIO
from sample.example import Example
from sample.main import Main

class TestMain:
    def test_prints_example_output(self):
        output = StringIO()
        main = Main(output)

        main.run()

        assert Example().greeting() in output.getvalue()

