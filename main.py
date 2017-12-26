from __future__ import print_function
from Model.IR import *
import os

from Model.DocOperator import DocOperator
from collections import Counter

from Model.TrainingClassHolder import TrainingClassHolder
from Model.Cluster import Cluster
import nltk


#  R06725054
# main program  ========================================================================================================
def main():
    
    # lemmatization
    nltk.download('wordnet')

    #  initialize obj
    
    # you can use the url or local file to initialize object
    # obj = IR_operator('https://ceiba.ntu.edu.tw/course/35d27d/content/28.txt ')

    # hw1 =================================================================================
    # obj = IR_operator('Static_txt/test.txt')
    # obj.tokenization()
    # obj.removeStopWord('Static_txt/stopList.txt')
    # obj.stemming()
    # obj.removeSameWordAndStopWord('Static_txt/stopList.txt')
    # obj.writeResultToFile('result.txt')
    # obj.log()

    # HW2   ==============================================================================
    
    # 1/3  Calculate DocumentFrequency & Generate dictionary.txt =========================  
    
    # docOpe_obj = DocOperator("./Static_txt/IRTM/")
    docOpe_obj = DocOperator("./Static_txt/test/")

    docOpe_obj.genrateDoc()
    docOpe_obj.docFreqCal()
    docOpe_obj.indexingDict()
    docOpe_obj.writeToFile('dictionary.txt')

    # print documents
    print ('Document frequenct task done')
    
    # 2/3 Calctulate TF-IDF & Generate unit vector for terms in each documents's ===========
    docOpe_obj.cal_Tf_Idf()
    docOpe_obj.write_Tf_Idf_ToFile('./Tf-Idf_unit_vector/')
    print ('tf-idf task done')

    # 3/3 Calculate Consine Similarity between two Doc =======================================
    
    txt1 = 1
    txt2 = 2

    consine_similarity = docOpe_obj.calCosineSimilarity("./Tf-Idf_unit_vector/", txt1 , txt2)
    # print ('file : {}   \nfile : {} \nconsine similarity is : {}'.format(str(txt1) ,str(txt2) ,str(consine_similarity)) )
    print ('all task done')
    
    # HW3 =====================================================================================
    # trainingData = TrainingClassHolder("./Static_txt/training.txt")
    # result_dict = trainingData.selectFeature(docOpe_obj.doc_list)
    # docOpe_obj.writeDictToFile('output.txt', result_dict)


    # HW4 =====================================================================================
    cluster_obj = Cluster()
    cluster_obj.EfficientHAC(docOpe_obj)

if __name__ == '__main__':
    main()
    




    
