from mycroft import MycroftSkill, intent_file_handler


class LazyTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.lazy.intent')
    def handle_test_lazy(self, message):
        self.speak_dialog('test.lazy')


def create_skill():
    return LazyTest()

