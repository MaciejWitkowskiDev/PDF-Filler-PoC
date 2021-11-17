
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from io import BytesIO
from json import load as json_load
from os import path as os_path
from FormFiller import FormFiller
from FieldMapper import FieldMapper


class InvalidFormException(Exception):
    pass


class PdfGenerator(object):

    def __init__(self):
        if (not os_path.isfile(u'mapping.json')):
            raise FileNotFoundError(u'Mapping file not found!')
        else:
            with open(u'mapping.json') as field_mapping:
                self.__field_mapping = json_load(field_mapping)

    def getMapping(self):
        return self.__field_mapping

    def generatePdf(self, form, values):
        if (form in self.getMapping().keys()):
            with open(u''.join([u'{}'.format(form), u'.pdf']), u'rb') as pdf_template:
                filestream = BytesIO(pdf_template.read())
                if (len(values) == 0):
                    return filestream
                mapper = FieldMapper(values, self.getMapping()[form])
                filler = FormFiller(filestream)
                filler.fillForm(mapper)
                return filler.getFilestream()
        else:
            raise InvalidFormException(
                u''.join([u'Mapping for form ', u'{}'.format(form), u' not found!']))
