import os
from Model.DocOperator import DocOperator
import json 
from collections import Counter
import math


class TrainingClassHolder:

    n = 0 

    #  store traing document 
    # key = class number , value = doc id list
    classDicID = {}

    # key = class number
    classDocFrequency = {}

    # document frequency in training data 
    trainingDocFrequency = {}

    # generate form for each term 
    classTermScore = {}

    featureTerm= {}

    def __init__(self,path):

        for line in open(path).read().splitlines():
            items = line.split()
            self.classDicID[items[0]] = items[1:]
            # print(self.classDic[items[0]])


    # select feature term 
    def selectFeature(self,docList_obj):

        # create classDocFrequency ===================================
        # 每個class 編號的 中 term 的doc frequency
        for classId in self.classDicID:
            
            self.classDocFrequency[classId] = []

            for docId in self.classDicID[classId]:
                doc_vocabulary = [doc for doc in docList_obj if  doc.id == docId]
                self.classDocFrequency[classId] += list(set(doc_vocabulary[0].obj.results))

                self.n += 1 

            self.classDocFrequency[classId] = dict(Counter(self.classDocFrequency[classId]))
            
            # print (self.classDocFrequency[classId])
            

        # training data doc frequency ===================================
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

        # print (json.dumps(self.trainingDocFrequency, indent=2))

        # generate Likelihood Ratios form  ================================================
        for key in self.trainingDocFrequency : 
            
            self.classTermScore[key] = dict()

            for classId in self.classDicID:

                self.classTermScore[key][classId] = dict(
                    {
                        "n11": self.classDocFrequency[classId].get(key , 0 ) ,
                        "n01" : self.trainingDocFrequency[key] - self.classDocFrequency[classId].get(key , 0 ) , 
                        "n10": 15 - self.classDocFrequency[classId].get(key , 0) , 
                        "n00" : 13*15 - (self.classDocFrequency[classId].get(key , 0 ) + (self.trainingDocFrequency[key] - self.classDocFrequency[classId].get(key , 0 )) + (15 - self.classDocFrequency[classId].get(key , 0))) 
                        }
                    )
                n11 = self.classTermScore[key][classId].get("n11")
                n01 = self.classTermScore[key][classId].get("n01")
                n10 = self.classTermScore[key][classId].get("n10")
                n00 = self.classTermScore[key][classId].get("n00")

                pt = (n11 + n01) / self.n
                p1 = n11 / (n11 + n10)
                p2 = n01 / ( n01 + n00)

                score = -2 * math.log(((pt)**n11 * (1-pt)**n10 * (pt)**n01 * (1-pt)**n00) / ((p1**n11) * (1-p1)**n10 * ( p2**n01) *((1-p2)**n00)))
                self.classTermScore[key][classId]["score"] = score
        
        # term select 
        for key in self.trainingDocFrequency:
            self.featureTerm[key] = 0
            for classId in self.classDicID:
                self.featureTerm[key] += self.classTermScore[key][classId]["score"]                                 
        
        self.featureTerm = sorted(self.featureTerm.items(), key= lambda x : x[1] , reverse=True)
        print( self.featureTerm)
        


        # print (json.dumps(self.classTermScore, indent=2))
        # print (self.classTermScore)






