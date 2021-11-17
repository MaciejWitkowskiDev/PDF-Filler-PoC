
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from enum import Enum
import json


class Status(Enum):
    OK = 0
    ERROR = 1


class FileResponse(object):

    def __init__(self):
        self.__status = Status.OK
        self.__message = u''
        self.__response_body = u''

    def setStatus(self, status):
        self.__status = status

    def setMessage(self, message):
        self.__message = message

    def setBody(self, response):
        self.__response_body = response

    def getStatus(self):
        return self.__status

    def getMessage(self):
        return self.__message

    def getBody(self):
        return self.__response_body

    def getResponse(self):
        return json.dumps({
            u'status': self.getStatus().value,
            u'message': self.getMessage(),
            u'response_body': self.getBody(),
        })
