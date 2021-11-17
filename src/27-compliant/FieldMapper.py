
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class InvalidMappingException(Exception):
    pass


class FieldMapper(object):

    def __generateDict__(self, values, mapping):
        ret = dict()
        for (field, key) in mapping.items():
            if (not (key in values.keys())):
                continue
            ret[field] = values[key]
        return ret

    def __verifyMapping__(self, values, mapping):
        for key in values.keys():
            if (not (key in list(mapping.values()))):
                raise InvalidMappingException(u''.join(
                    [u'Invalid mapping provided: value of ', u'{}'.format(key), u' not mapped.']))
        return True

    def __init__(self, values, mapping):
        if self.__verifyMapping__(values, mapping):
            self.valuedict = self.__generateDict__(values, mapping)

    def getValues(self):
        return self.valuedict
