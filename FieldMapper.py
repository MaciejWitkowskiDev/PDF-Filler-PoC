class InvalidMappingException(Exception):
    pass

class FieldMapper:

    def __generateDict__(values : dict, mapping : dict):
        ret : dict = dict()
        for field, key in mapping.items():
            ret[field] = values[key]
        return ret 

    def __verifyMapping__(values : dict, mapping : dict):
        for key in values.keys():
            if key not in mapping.keys():
                raise InvalidMappingException(f"Invalid mapping provided: value of {key} not mapped.")
        return True

    def __init__(self, values : dict, mapping : dict):
        if self.__verifyMapping__(mapping, values):
            self.__valuedict = self.__generateDict__(values, mapping)
    
    def getMapping(self):
        return self.__valuedict