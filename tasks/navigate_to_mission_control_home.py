from screenplay import Task, Actor, log_message
from actions.navigate_to import navigate_to
from pages.nav_header import nav_header


class navigate_to_mission_control_home(Task):
    @log_message('The user navigates to Blast Off!')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            navigate_to("http://missioncontrol.bluefruit.co.uk/")
        )
