class InvalidMappingException(Exception):
    pass

class FieldMapper:

    def __generateDict__(self, values : dict, mapping : dict):
        ret : dict = dict()
        for field, key in mapping.items():
            if not(key in values.keys()):
                continue
            ret[field] = values[key]
        return ret

    def __verifyMapping__(self, values : dict, mapping : dict):
        for key in values.keys():
            if not(key in list(mapping.values())):
                raise InvalidMappingException(f"Invalid mapping provided: value of {key} not mapped.")
        return True

    def __init__(self, values : dict, mapping : dict):
        if self.__verifyMapping__(values, mapping):
            self.valuedict = self.__generateDict__(values, mapping)

    def getValues(self):
        return self.valuedict
