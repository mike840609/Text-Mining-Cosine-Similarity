import os
from Model.DocOperator import DocOperator

class TrainingClassHolder:

    #  store traing document 
    # key = class number , value = doc id list
    classDicID = {}

    # key = class number , value = all vocabulary set 
    classVocabularyDict = {}

    # document frequency in training data 
    trainingDocFrequency = {}

    # generate form for each term 
    classTermScore = {}

    
    def __init__(self,path):

        for line in open(path).read().splitlines():
            items = line.split()
            self.classDicID[items[0]] = items[1:]
            # print(self.classDic[items[0]])


    # select feature term 
    def selectFeature(self,docList_obj):

        # create classVocabularyDict ===================================
        for classId in self.classDicID:
            self.classVocabularyDict[classId] = []

            for docId in self.classDicID[classId]:

                doc_vocabulary = [doc for doc in docList_obj if  doc.id == docId]

                self.classVocabularyDict[classId] += doc_vocabulary[0].obj.results

            print ("before set : {}".format(str(len(self.classVocabularyDict[classId]))))
            self.classVocabularyDict[classId] = set(self.classVocabularyDict[classId])
            print ("after set : {}".format(str(len(self.classVocabularyDict[classId]))))
            print ('====================================================================')

        # training data term frequency ===================================
        for classId in self.classDicID:
            for docId in self.classDicID[classId]:

                #  all id in class 
                document_list = [doc for doc in docList_obj if  doc.id == docId]
                unique_term_in_doc = set(document_list[0].obj.results)

                for term in unique_term_in_doc:
                    if term in self.trainingDocFrequency.keys():
                        self.trainingDocFrequency[term] += 1 
                    else:
                        self.trainingDocFrequency[term] = 1

        # print(self.trainingDocFrequency) 

        # generate Likelihood Ratios form  ================================================







        
        # for doc in docOpe_obj.doc_list:
        #     print("============================================")
        #     print (doc.id)
        #     print (doc.obj.results)
        #     print("============================================")



