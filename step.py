import json

class Step(object):
    """A step in an adventure"""

    def __init__(self, data):
        self.title = data['title']
        self.text = data['text']
        if 'choices' in data:
            self.choices = data['choices']
        else:
            self.choices = None
