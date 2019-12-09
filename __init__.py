from mycroft import MycroftSkill, intent_file_handler


class Szakal(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('szakal.intent')
    def handle_szakal(self, message):
        self.speak_dialog('szakal')


def create_skill():
    return Szakal()

