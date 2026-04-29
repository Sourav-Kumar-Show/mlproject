
# sys -> Provide various functions and variables that are used to manipulate different part of python runtime enviroment
import sys
from logger import logging

def error_messsage_detail(error, error_detail:sys): # Whenever error occur, this function will be called.
    _, _, exc_tb = error_detail.exc_info()          # exc_tb will give, in which line or file exception occured.
    file_name = exc_tb.tb_frame.f_code.co_filename  # this wil get you the file
    # How the error should look like when occured -> the formate
    # Here 0, 1, 2 are placeholder where the value will be placed.
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# created own Coustom exception class which is inheriting from parent Exception
class CustomException(Exception):
    # Overridden the init function
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        # initializing this error message with function's error message (error_message_details())
        self.error_message = error_messsage_detail(error_message, error_detail = error_detail)


    def __str__(self):
        return self.error_message               # whenever try to print it, get the error message here


# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info("Divide by zero.")
#         raise CustomException(e, sys)