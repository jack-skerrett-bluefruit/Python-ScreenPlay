from .question import Question
from .matcher import Matcher


class Condition:
    def __init__(self, question: Question, expected: Matcher):
        self.question = question
        self.expected = expected

    def check_as(self, actor):
        assert self.expected.matches(self.question.answered_by(actor)), self.expected.fail_message


see_that = Condition
