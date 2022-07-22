import json
class Log(object):
    def __init__(self,path):
        self._log_ptr = open(path,"a+")
        self.log_path = path
    def cout(self,message):
        self._log_ptr.write(message)
        self._log_ptr.write("\n")
    def coutJson(self,message):
        self._log_ptr.write(json.dumps(message,indent=4))
        self._log_ptr.write("\n")
    def close(self):
        self._log_ptr.close()
    def __del__(self):
        self.close()
