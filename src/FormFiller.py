# For more flexibility, the FormFiller constructor takes in an already read byte array of the  pdf file, NOT a python File object!
import pdfrw
from env import *
from io import BytesIO
from FieldMapper import FieldMapper
class FormFiller:

    def __fill_pdf__(self,input_pdf_filestream, data_dict):
        template_pdf = pdfrw.PdfReader(input_pdf_filestream)
        filled_pdf_filestream : bytes = BytesIO()
        for page in template_pdf.pages:
            annotations = page[ANNOT_KEY]
            if annotations:
                for annotation in annotations:
                    if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                        if annotation[ANNOT_FIELD_KEY]:
                            key = annotation[ANNOT_FIELD_KEY][1:-1]
                            if key in data_dict.keys():
                                if data_dict[key] == 'Tak':
                                    annotation.update( pdfrw.PdfDict( V=pdfrw.PdfName(data_dict[key]) , AS=pdfrw.PdfName(data_dict[key])))
                                    annotation.update(pdfrw.PdfDict(Ff=1))
                                else:
                                    annotation.update(
                                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                                    )
                                    annotation.update(pdfrw.PdfDict(AP=''))
                                    annotation.update(pdfrw.PdfDict(Ff=1))
        template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
        pdfrw.PdfWriter().write(filled_pdf_filestream, template_pdf)
        return filled_pdf_filestream

    def fillForm(self,mapper : FieldMapper):
        value_mapping = mapper.getValues()
        self.filestream : bytes  = self.__fill_pdf__(self.filestream, value_mapping)

    def getFilestream(self):
        return self.filestream

    def __init__(self, filestream : bytes):
        self.filestream : bytes = filestream