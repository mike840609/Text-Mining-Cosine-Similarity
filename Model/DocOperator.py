import os
import re

class DocOperator:

    doc_list = []
    docs_path = ''

    def __init__(self , doc_path):
        # self.getDoc(doc_path)
        self.doc_path = doc_path

    
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

    def __init__(self,id ,content):
        self.id = id
        self.content = content
