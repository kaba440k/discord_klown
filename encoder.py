from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Message):
            return {'user': obj.user, 'text': obj.text}


class Message(MyEncoder):

    def __init__(self, user, text):
        super().__init__()
        self.user = user.display_name
        self.text = text