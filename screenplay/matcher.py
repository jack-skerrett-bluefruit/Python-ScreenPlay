class Matcher:
    def matches(self, answer) -> bool:
        return False

    @property
    def fail_message(self):
        return 'Matcher fail message not specified'
