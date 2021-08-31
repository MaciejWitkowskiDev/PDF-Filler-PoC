from enum import Enum
import json 

class Status(Enum):
    OK = 0
    ERROR = 1

class FileResponse:
    def __init__(self):
      self.__status = Status.OK
      self.__message = ""
      self.__response_body = ""
    
    def setStatus(self, status : Status):
        self.__status = status
    
    def setMessage(self, message : str):
        self.__message = message
    
    def setBody(self, response : bytes):
        self.__response_body = response

    def getStatus(self):
        return self.__status
    
    def getMessage(self):
        return self.__message
    
    def getBody(self):
        return self.__response_body
    
    def getResponse(self):
        return json.dumps(
            {
                "status" : self.getStatus(),
                "message" : self.getMessage(),
                "response_body" : self.getResponse()
            }
        )