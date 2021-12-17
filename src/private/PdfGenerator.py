from io import BytesIO
from json import load as json_load
from os import path as os_path
from env import MAPPING_FILE_PATH, ROOT_PATH
from FormFiller import FormFiller
from FieldMapper import FieldMapper

class InvalidFormException(Exception):
    pass
class PdfGenerator:
    def __init__(self):
        if not os_path.isfile(MAPPING_FILE_PATH):
            raise FileNotFoundError("Mapping file not found!")
        else:
            with open(MAPPING_FILE_PATH) as field_mapping:
                self.__field_mapping = json_load(field_mapping)

    def getMapping(self):
        return self.__field_mapping

    def generatePdf(self, form : str, values: dict):
        if form in self.getMapping().keys():
            with open(f"{ROOT_PATH}/{form}.pdf", "rb") as pdf_template:
                filestream = BytesIO(pdf_template.read())
                if len(values) == 0:
                    return filestream
                mapper = FieldMapper(values, self.getMapping()[form])
                filler = FormFiller(filestream)
                filler.fillForm(mapper)
                return filler.getFilestream()
        else:
            raise InvalidFormException(f"Mapping for form {form} not found!")
