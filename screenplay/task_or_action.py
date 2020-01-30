class TaskOrAction:
    def perform_as(self, actor):
        pass

    @property
    def description(self):
        return 'TaskOrAction.description not overridden'
