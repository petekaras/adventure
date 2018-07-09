import json
from step import Step

class Adventure(object):
    """Adventure definition"""

    def __init__(self, name):
        self.adventureMap = {}
        for item in json.loads(open(name).read()):
            self.adventureMap[item['id']] = Step(item)

    def title(self, step):
        return self.adventureMap[step].title

    def text(self, step):
        return self.adventureMap[step].text

    def type(self, step):
        return self.adventureMap[step].type

    def choices(self, step):
        if self.adventureMap[step].choices:
            return self.adventureMap[step].choices

    def getStep(self, step):
        return self.adventureMap[step]
