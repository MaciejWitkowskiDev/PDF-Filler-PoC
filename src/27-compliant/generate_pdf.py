
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from PdfGenerator import PdfGenerator
from FileResponse import FileResponse
from FileResponse import Status
from sys import argv
from base64 import b64encode
try:
    from urllib.parse import unquote
except ImportError:
    from six.moves.urllib_parse import unquote
from re import match


class InvalidKeyException(Exception):
    pass


def generate_values(pairs):
    values = dict()
    for pair in pairs:
        if match(u'\\w+:\\w+', pair):
            pair = pair.split(u':')
            values[unquote(pair[0])] = unquote(pair[1])
        else:
            raise InvalidKeyException(u''.join(
                [u'Passed an invalid key:value pair to the pdf generation script: ', u'{}'.format(pair)]))
    return values


def main():
    response = FileResponse()
    try:
        values = generate_values(argv[2:])
        pdf_generator = PdfGenerator()
        response_filestream = pdf_generator.generatePdf(argv[1], values)
        response_filestream.seek(0)
        pdf_bytes = response_filestream.read()
        response.setStatus(Status.OK)
        response.setMessage(u'')
        response.setBody(b64encode(pdf_bytes).decode(u'latin1'))
        return response.getResponse()
    except Exception as err:
        response.setStatus(Status.ERROR)
        response.setMessage(unicode(err))
        response.setBody(u'')
        return response.getResponse()


print(main())
