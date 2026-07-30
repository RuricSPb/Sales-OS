from models.object import Object


class ObjectCard:

    def __init__(self, obj: Object):

        self.object = obj

        self.customer = None

        self.contractor = None

        self.designer = None