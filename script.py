import requests
import json
import base64
import xmltodict
import const
base_url="https://api.github.com/repos";
uri="/contents/a.txt";
import logging
import random
# logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)

logging.basicConfig(level=logging.INFO, format="%(name)s -- %(levelname)s -- %(message)s");
logger = logging.getLogger(__name__);

def getFile(uri):

      response = requests.get(base_url+uri);
      dict = json.loads(response.text);

      encoded_content= dict['content'];
      
      
      dict = xmltodict.parse(message)   
      print(dict['project']['modelVersion']);  


# getFile("/contents/a.txt")

def uploadFile(templete,repo,file):
    encoded_content = convert_dict_to_base64(templete)
    body = {}
    body['message']="Data commit for {}".format(file)
    body['content']=encoded_content
    print(base_url+repo+file)
    response = requests.put(base_url+repo+file,data=json.dumps(body),headers={"Authorization":const.token})
    print(response.text)    


def convert_base65_to_string(encoded_content):
    base64_bytes = encoded_content.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    return message

def convert_dict_to_base64(dict):
    json_string = json.dumps(dict)

    message_bytes = json_string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    print(base64_message)
    return base64_message

def getPomFile(repo):
      response = requests.get(base_url+repo+uri)
      dict = json.loads(response.text)
      encoded_content= dict['content']
      message = convert_base65_to_string(encoded_content)
      dict = xmltodict.parse(message) 
      return dict


def process(repo,templete):

    pomdata= getPomFile(repo)
    templete['version']=pomdata['project']['modelVersion']
    templete['location']=pomdata['project']['artifactId']
    val = random.choice(range(1,30000))
    uploadFile(templete,repo,"/contents/"+str(val)+"abhi.txt");

def read(file):
    logger.info("reading the data");
    list =[]
    with open(file,"r") as f:
         list = [line.rstrip() for line in f]

    return list; 

def load_templete(file):
    logger.info("reading the templete");
    list ='';
    with open(file,"r") as f:
         list = f.read()

    return json.loads(list)
    

def performMigration():
    read_csv_array = read("data.csv")
    templete_data = load_templete("templete.json")
    

    for i in read_csv_array:
        row_data = i.split(',')
        logger.info("perfoming  action on {}".format(row_data))
        process(row_data[1],templete_data.copy())



if __name__=="__main__":
    performMigration();