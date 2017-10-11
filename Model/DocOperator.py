import os
import re

from IR import IR_operator


class DocOperator:

    doc_list = []

    stopWord_list = []

    docs_path = ''



    def __init__(self , doc_path):
        # self.getDoc(doc_path)
        self.doc_path = doc_path
        # stop_temp = open('Static_txt/stopList.txt').read()
        # self.stopWord_list = stop_temp.lower().split()
        # print len(self.stopWord_list)
    

    def getDoc(self):

        all_files = os.listdir(self.doc_path)

        for file_name in all_files:

            file = open(self.doc_path + file_name)
            file_name = re.sub(r'([^0-9]|_)+', '', file_name)
            doc_obj = Doc(file_name , file.read())
            self.doc_list.append(doc_obj)
            
        return self.doc_list
        

class Doc:

    id = ''
    content = ''

    # all terms in document
    terms_without_set = []

    def __init__(self,id ,content):

        self.id = id
        self.content = content

        # IR opration
        obj = IR_operator() 
        obj.set_str_temp(content)
        obj.tokenization()
        obj.stemming()
        # obj.removeStopWord()

