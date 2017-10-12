import os
import re

from IR import IR_operator
from collections import Counter

class DocOperator:

    doc_list = []
    stopWord_list = []

    # save all terms Set 
    allTermsSet = set()

    def __init__(self , doc_path):
        
        self.doc_path = doc_path
        stop_temp = open('Static_txt/stopList.txt').read()
        self.stopWord_list = stop_temp.lower().split()

    
    def getDoc(self):
        self.doc_list = []
        all_files = os.listdir(self.doc_path)

        for file_name in all_files:

            file = open(self.doc_path + file_name)
            file_name = re.sub(r'([^0-9]|_)+', '', file_name)
            doc_obj = Doc(file_name , file.read(), self.stopWord_list)
            self.doc_list.append(doc_obj)
        
        return self.doc_list

#  each Doc Implement 
class Doc:

    id = '' 
    obj = ''
    freqs = Counter()

    def __init__(self,id ,content, stopWord_list):

        self.id = id

        # IR opration
        self.obj = IR_operator() 
        self.obj.set_str_temp(content)
        self.obj.tokenization()
        self.obj.removeStopWord(stopWord_list)
        self.obj.stemming()
    

    def getResultstSet(self):
        return set(self.obj.results)

    def getResultstList(self):
        return self.obj.results

    # get all term ,  value == 1 
    def getTermDict(self):
        self.freqs = dict((k,1) for k in self.getResultstList())
        return self.freqs

    # get all term 
    def getTermFreqs (self):
        self.freqs = Counter(self.getResultstList())
        return self.freqs



class Term:
    index = ''
    term = ''
    df = 0

    def __init__(self , index ,term ):
        self.index = index
        self.term = term