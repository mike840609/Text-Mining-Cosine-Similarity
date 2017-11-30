
import os

class TrainingClassHolder:

    #  store traing document 
    # key = class number , value = doc id list
    classDicID = {}

    # key = class number , value = all vocabulary
    classVocabularyDict = {}
    calssTermSCore = {}
    
    def __init__(self,path):

        for line in open(path).read().splitlines():
            items = line.split()
            self.classDicID[items[0]] = items[1:]
            # print(self.classDic[items[0]])


    
    def selectFeature(self,docList_obj):

        for classId in self.classDicID:
            self.classVocabularyDict[classId] = []

            for docId in self.classDicID[classId]:

                doc_vocabulary = [doc for doc in docList_obj if  doc.id == docId]
                
                self.classVocabularyDict[classId] += doc_vocabulary[0].obj.results

            # print (self.classVocabularyDict[classId])
            print (len(self.classVocabularyDict[classId]))
            self.classVocabularyDict[classId] = set(self.classVocabularyDict[classId])
            print (len(self.classVocabularyDict[classId]))
            print ('===============================================================================================')


        
        # for doc in docOpe_obj.doc_list:
        #     print("============================================")
        #     print (doc.id)
        #     print (doc.obj.results)
        #     print("============================================")



