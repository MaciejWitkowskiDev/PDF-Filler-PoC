#This is going to be our main dispatch.
#Usage:
# $ python generate_pdf.py formname key1:value1 key2:value2 ... keyn:valuen
# Example:
# $ python generate_pdf.py pit-example rok:2021 krs:0000012345 

from PdfGenerator import PdfGenerator
from FileResponse import FileResponse
from FileResponse import Status
from sys import argv
from base64 import b64encode
from urllib.parse import unquote
from re import match

class InvalidKeyException(Exception):
    pass

def generate_values(pairs : list):
    values = dict()
    for pair in pairs:
        if match("\w+:\w+", pair):
            pair = pair.split(":")
            values[unquote(pair[0])] = unquote(pair[1])
        else:
            raise InvalidKeyException(f"Passed an invalid key:value pair to the pdf generation script: {pair}")
    return values


def main():
    response = FileResponse()
    try:
        values : dict = generate_values(argv[2:])
        pdf_generator = PdfGenerator()
        response_filestream = pdf_generator.generatePdf(argv[1], values)
        response_filestream.seek(0)
        pdf_bytes = response_filestream.read()
        response.setStatus(Status.OK)
        response.setMessage("")
        response.setBody(b64encode(pdf_bytes).decode('latin1'))
        return response.getResponse()
    except Exception as err:
        response.setStatus(Status.ERROR)
        response.setMessage(str(err))
        response.setBody("")
        return response.getResponse()

print(main())