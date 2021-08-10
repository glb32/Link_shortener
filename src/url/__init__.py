import random,string
from urllib.parse import urlparse

base_url = "http://127.0.0.1:5000/a/"

class Link:
    
    def __init__(self, LongURL):
        self.LongURL = LongURL 
        self.ShortURL = None
        self.URLid = None
        
               
    def Shorten(self):
        test = urlparse(self.LongURL)
        if(all([test.scheme,test.netloc])):
            self.URLid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
            self.ShortURL= base_url + self.URLid
            return {'URL':self.LongURL,'URLid':self.URLid,'ShortURL':self.ShortURL}
        else:
            return Exception("InvalidURLError")
             
   
