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

    
    # hw2  ============================================================
    
    # test folder just one doc 
    # docOpe_obj = DocOperator("./Static_txt/IRTM/")
    docOpe_obj = DocOperator("./Static_txt/test/")

    docOpe_obj.genrateDoc()
    docOpe_obj.docFreqCal()
    docOpe_obj.indexingDict()

    # print docOpe_obj.getDoc()

    docOpe_obj.writeToFile('dictionary.txt')

    # print documents



if __name__ == '__main__':
    main()
    




    
