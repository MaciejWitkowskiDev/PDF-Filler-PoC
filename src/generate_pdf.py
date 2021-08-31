
#This is going to be our main dispatch.
#Usage:
# $ python generate_pdf.py formname key1:value1 key2:value2 ... keyn:valuen
# Example:
# $ python generate_pdf.py pit-example rok:2021 krs:0000012345 

from PdfGenerator import PdfGenerator
from FileResponse import FileResponse
from FileResponse import Status
from sys import argv
from re import L, match

class InvalidKeyException(Exception):
    pass

#pairs never empty in this context
def generate_values(pairs : list):
    values = dict()
    for pair in pairs:
        if match("\w+:\w+", pair):
            pair = pair.split(":")
            values[pair[0]] = pair[1]
        else:
            raise InvalidKeyException(f"Passed an invalid key:value pair to the pdf generation script: {pair}")
    return values


def main():
    response = FileResponse()
    values : dict = generate_values(argv[2:])
    pdf_generator = PdfGenerator()
    response_filestream = pdf_generator.generatePdf(argv[1], values)
    response_filestream.seek(0)
    response.setStatus(Status.OK)
    response.setMessage("")
    response.setBody(response_filestream.read().decode('utf-8'))
    return response.getResponse()


print(main())