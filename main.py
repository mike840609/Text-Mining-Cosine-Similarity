from Model.IR import *
import os

from Model.DocOperator import DocOperator
from collections import Counter


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

    
    # hw2  ================================================
    
    # test folder just one doc 
    docOpe_obj = DocOperator("./Static_txt/IRTM/")
    # docOpe_obj = DocOperator("./Static_txt/test/")
    all_doc_list = docOpe_obj.getDoc()

    # documentFrequency = {}
    documentFrequency = Counter()

    # low performance 
    for i in all_doc_list:
        # print i.getTermDict()
        documentFrequency = documentFrequency + Counter(i.getTermDict())

        # for k,v in i.getTermDict().items():
        #     if k in documentFrequency.keys():
        #         documentFrequency[k] += 1 
        #     else:
        #         documentFrequency[k] = v
            

    print documentFrequency

        

if __name__ == '__main__':
    main()
    




    
