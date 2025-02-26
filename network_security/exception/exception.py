import sys
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()

        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in line [{0}] in file [{1}] with error message [{2}]".format(
            self.lineno,self.filename,str(self.error_message))
    
            

