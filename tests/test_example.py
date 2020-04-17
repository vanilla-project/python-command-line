from sample.example import Example


class TestExample:
    def test_returns_message(self):
        example = Example()

        assert example.greeting() == "Python Example"

