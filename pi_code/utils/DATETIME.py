# This program returns the current date and time

import datetime

def GetDateTime():

    # Let us format the date into DD-MM-YYYY
    data = datetime.datetime.now()
    date = data.strftime("%d")+'/'+data.strftime("%m")+'/'+data.strftime("%Y")    
    time = data.strftime("%I")+':'+data.strftime("%M")+':'+data.strftime("%S")+' '+data.strftime("%p")
    
    return date,time


if __name__ == "__main__":
    GetDateTime()
