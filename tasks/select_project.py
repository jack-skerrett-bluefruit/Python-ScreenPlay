from screenplay import Task, Actor, log_message
from actions.select_from_dropdown import select_from_dropdown
from pages.nav_header import nav_header


class select_project(Task):
    def __init__(self, project_name):
        self.project_name = project_name

    @log_message('Select the project')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            select_from_dropdown(nav_header.project_dropdown, self.project_name)
        )
