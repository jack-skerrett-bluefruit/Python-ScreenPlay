from screenplay import Task

class StubTask(Task):
    def __init__(self):
        self.called = False

    def perform_as(self, actor):
        self.called = True
