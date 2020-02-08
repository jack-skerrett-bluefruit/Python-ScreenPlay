from screenplay import Action, Actor, log_message
from tasks.navigate_to import navigate_to


class open_google(Action):
    @log_message('Open google homepage')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            navigate_to('https://www.google.co.uk')
            )
