
from itertools import groupby


fd =open("file.txt",'r')


print(fd.read())




fd.close()

fd = open("file2.txt","a");

fd.write("gdfdf\n")

fd.close()


dic = [{"name":"Abhi","age":12},{"name":"Bhai","age":13},{"name":"Bhai2","age":13}];


values = groupby(dic,key=lambda k:k['age'])
for key,value in values:
    print(key)
    print(list(value))

from helper import logger
logger.warning("Warningdd");
logger.debug("Defbug");
logger.error("Error");
logger.info("INfo");


import logging
loger = logging.getLogger(__name__)


#create handler
stream_h= logging.StreamHandler()
stream_f = logging.FileHandler('file.log')

stream_h.setLevel(logging.WARNING)
stream_f.setLevel(logging.ERROR)

loger.addHandler(stream_f);
loger.addHandler(stream_h);


loger.info("Heeelo");
loger.debug("Debug");
loger.error("Error");
loger.warning("WWarnign");