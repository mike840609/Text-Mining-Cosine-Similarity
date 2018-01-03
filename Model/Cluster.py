from Model.DocOperator import DocOperator
from heapq_max import *


class Cluster:
    def __init__(self):
        pass
        
    def EfficientHAC(self,docOpe_obj):

        doc_list = docOpe_obj.doc_list
        # Sort list by id 
        doc_list.sort(key=lambda x:int(x.id), reverse=False)

        # the similarity between clusters i and j.
        C = [[Element() for x in range (0, len(doc_list) + 1)]for y  in range(0 ,len(doc_list)+1)]

        # indicate which clusters are still available to be merged.
        I = [1] * (len(doc_list) + 1 )

        # an array of priority queue
        # P = [Element() for x in range (0, len(doc_list) + 1)]
        P = [None]*1096

        #  a list of merges
        A = []

        #  initialize phase =================================================
        for doc_1 in doc_list : 
            for doc_2 in doc_list : 

                # print(doc_1.terms["term"]["tf-idf"])
                cos_sin = 0 

                for key in doc_1.terms:
                    if key in doc_2.terms:
                        cos_sin += doc_1.terms[key]["tf-idf"] * doc_2.terms[key]["tf-idf"]

                C[int(doc_1.id)][int(doc_2.id)] = Element(cos_sin , int(doc_2.id))

        # print(C[1][2].index)
        # print(C[5][6].index)

        #  add heap to array P
        for doc in doc_list:
            
            #  call by value 
            P[int(doc.id)] = C[int(doc.id)][:]
            heapify_max(P[int(doc.id)])

            # print ([(ele.index, ele.sim) for ele in P[int(doc.id)]])
            # print("==================================")
            # print ([(ele.index, ele.sim) for ele in C[int(doc.id)]])
        

        #  Calculate phase =================================================
        # for i in range(1,len(doc_list)):
            # print (i)

            
                
            

            
    
        
        
        
                

                 

class Element(object) :
    sim  = 0
    index = 0
    
    def __init__(self, sim = 0 , index = 0):
        self.sim = sim
        self.index = index

    def __lt__(self, other):
        return self.sim < other.sim

    def __le__(self, other):
        return self.sim <= other.sim
      
    def __eq__(self, other):
        return self.sim == other.sim
      
    def __ne__(self, other):
        return self.sim != other.sim
      
    def __gt__(self, other):
        return self.sim > other.sim
      
    def __ge__(self, other):
        return self.sim >= other.sim

    def __str__(self):
        return "ind : " + str(self.index) + " sim : " + str(self.sim)


    # print ([(ele.index, ele.sim)for ele in heap_max ])


