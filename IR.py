import urllib2
import re

from Poter_Algo.Poter import PorterStemmer
from Poter_Algo.Poter2 import Porter2Stemmer


#  text operator 
class IR_operator:

    txt_str_temp = ''
    arr = []
    results = []

    # constructor 
    def __init__(self , txt_file_path):
        """path to the file which can be the  url or local file
        """
        self.txt_str_temp = self.loadUrlFromTxtOrUrl(txt_file_path)
        

    #  load txt file  from  url or local file  
    def loadUrlFromTxtOrUrl(self,path):
        if "http" in path: 
            temp = ''
            for line in urllib2.urlopen(path):
                temp += line
            return temp

        else:
            file = open(path) 
            return file.read() 

    # lower case &  regular expression make token conform to specification 
    def tokenization(self):

        #  lower case
        self.txt_str_temp = self.txt_str_temp.lower()
        
        # regular expression
        # Strip everything but spaces and alphanumeric
        self.txt_str_temp = re.sub(r'([^\s\w]|_)+', '', self.txt_str_temp)

        #  split str into array by space
        self.arr = self.txt_str_temp.split()

    
    # stemming
    def stemming(self):
        #  poter algorithm , Porter2Stemmer is better 
        # stemmer_test = PorterStemmer()
        stemmer = Porter2Stemmer()

        for ele in self.arr:
            self.results.append( stemmer.stem(ele) )

    
    # remove the stopWord & SameWord 
    def removeSameWordAndStopWord(self,path):
        """path to the file which can be the  url or local file
        """
        # make the list to the set , subtract same word
        self.results = set(self.results)
        
        # stop list 
        stop_temp = self.loadUrlFromTxtOrUrl(path)
        stop_arr = set(stop_temp.lower().split())
        
        #  subtract stop word 
        self.results = self.results.difference(stop_arr)
        

    # write to txt.file 
    def writeResultToFile(self):
            with open("result.txt", "w") as f:
                for word in self.results:
                    f.write(str(word) +"\n")

    # debug log
    def log(self):
        print self.results