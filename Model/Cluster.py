from Model.DocOperator import DocOperator


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
        P = [Element() for x in range (0, len(doc_list) + 1)]

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

                C[int(doc_1.id)][int(doc_2.id)] = cos_sin

        #  Calculate phase =================================================
        # for k in range(1 , len(doc_list)):
            # if I[k] = 1 :
                
            

            
    
        
        
        
                

                 

class Element(object) :
    sim  = 0
    index = 0
    
    def __init__(self, sim = 0 , index = 0):
        self.sim = sim
        self.index = index

    
    def setSim(self,sim):
        self.sim = sim

    def setIndex (self, ind):
        self.index = ind



    # 



