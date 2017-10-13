from Model.IR import *
import os

from Model.DocOperator import DocOperator
from collections import Counter
import collections

#  R06725054
# main program  ========================================================================================================
def main():
    #  initialize obj
    
    # you can use the url or local file to initialize object
    # obj = IR_operator('https://ceiba.ntu.edu.tw/course/35d27d/content/28.txt ')

    # hw1 ================================================
    # obj = IR_operator('Static_txt/test.txt')
    # obj.tokenization()
    # obj.removeStopWord('Static_txt/stopList.txt')
    # obj.stemming()
    # obj.removeSameWordAndStopWord('Static_txt/stopList.txt')
    # obj.writeResultToFile('result.txt')
    # obj.log()

    
    # hw2  ============================================================
    
    # test folder just one doc 
    # docOpe_obj = DocOperator("./Static_txt/IRTM/")
    docOpe_obj = DocOperator("./Static_txt/test/")

    all_doc_list = docOpe_obj.getDoc()
    
    documents = {}

    # low performance 
    for i in all_doc_list:
    
        for k,v in i.getTermDict().items():
            if k in documents.keys():
                documents[k]['df'] += 1 
            else:
                documents[k] = v
    # document frequency done ==========================================

    # sorted dict ============================================================
    documents = collections.OrderedDict(sorted(documents.items()))

    for idx , k in enumerate( documents.keys()):
        documents[k]['index'] = idx

    

    print documents


        
    

        

if __name__ == '__main__':
    main()
    




    
