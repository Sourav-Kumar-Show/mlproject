
# Logger's purpose is to log all the information of the execution in a file
# so that, if exception occured track it an log it in the file.


import logging
import os
from datetime import datetime 

# create the name of log file (format of information stored in log file )
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  
# file_name will be WHAT DATETIME TIME IT IS COMING futhur will be MONTH DATE YEAR HOUR MINUTE SECOND

# PATH  for Log_file            cwd -> current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)   #folder name should have log in front, then inside this naming convension.

# Even though there is file keep on appending the file inside, whenever want to create file
os.makedirs(logs_path, exist_ok=True)       

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# To override the functionality of login, need to set this in basic Config
logging.basicConfig(
    # File name -> to save
    filename= LOG_FILE_PATH,

    #Format to use inside the log file
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO     # In case of INFO only, it going to print the specific message


)

# if __name__ == "__main__":
#     logging.info('Logging has Started..')