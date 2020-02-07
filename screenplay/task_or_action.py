from .log import log_message

class TaskOrAction:
    @log_message('TaskOrAction.description not overridden')
    def perform_as(self, actor):
        pass

