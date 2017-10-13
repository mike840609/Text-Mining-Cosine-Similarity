import os
import re
import collections

from IR import IR_operator
from collections import Counter


class DocOperator:

    doc_list = []
    stopWord_list = []

    documents = {}
    

    def __init__(self , doc_path):
        
        self.doc_path = doc_path
        stop_temp = open('Static_txt/stopList.txt').read()
        self.stopWord_list = stop_temp.lower().split()

    def genrateDoc(self):

        self.doc_list = []
        all_files = os.listdir(self.doc_path)

        for file_name in all_files:

            file = open(self.doc_path + file_name)
            file_name = re.sub(r'([^0-9]|_)+', '', file_name)
            doc_obj = Doc(file_name , file.read(), self.stopWord_list)
            self.doc_list.append(doc_obj)
        
        return self.doc_list
    
    def docFreqCal(self):
            for i in self.doc_list:    
                for k,v in i.getTermDict().items():
                    
                    if k in self.documents.keys():
                        self.documents[k]['df'] += 1 
                    else:
                        self.documents[k] = v

    def indexingDict(self):
        
        self.documents = collections.OrderedDict(sorted(self.documents.items()))
        
        for idx , k in enumerate( self.documents.keys()):
            self.documents[k]['index'] = (idx + 1)
    
    def getDoc(self):
        return self.documents

    def writeToFile(self, path):

        with open(path , "w") as f :

            for k , v in self.documents.items():

                print '{:<15}'.format(v['index']) + '{:<30}'.format(k) + '{:<10}'.format(v['df'])

                
                f.write('{:<15}'.format(v['index']) + '{:<30}'.format(k) + '{:<10}'.format(v['df']) + '\n' )

                # print v['index']
                # print k
                # print v['df'] 

            # with open(path , "w") as f :
            #     f.write("123" + '')
            


    
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
    
    def getResultstList(self):
        return self.obj.results

    # get all term ,  value == 1 
    def getTermDict(self):
        self.freqs = dict((k,{'index': 0 ,'df': 1, 'tf-idf': 0 }) for k in self.getResultstList())
        return self.freqs


class Term:
    index = ''
    term = ''
    df = 0

    def __init__(self , index ,term ):
        self.index = index
        self.term = term