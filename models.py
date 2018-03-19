class BusinessObject(object):
    def __init__(self, busObId=None, busObPublicId=''):
        self.busObId = busObId
        self.busObPublicId = busObPublicId
        self.persist = True
        self.fields = []


class BusinessObjectFields(object):
    def __init__(self, fieldId, name, value, dirty):
        self.fieldId = fieldId
        self.name = name
        self.value = value
        self.dirty = dirty
