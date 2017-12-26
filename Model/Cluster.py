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
        I = [1] * len(doc_list)

        # an array of priority queue
        P = [Element() for x in range (0, len(doc_list) + 1)]

        #  a list of merges
        A = []

        #  initialize phase =================================================
        for n_obj in doc_list:
            n = int(n_obj.id)

            for i_obj in doc_list:    
                i = int(i_obj.id)

                consine_similarity = docOpe_obj.calCosineSimilarity("./Tf-Idf_unit_vector/", n , i )
                C[n][i].setSim(consine_similarity)
                C[n][i].setIndex(i)

                # print(consine_similarity)
            
            # insert queue to Array P 
            C[n][n].setSim(0) 
            
            # TODO: Maximum Heap sort List element
            P[n] = sorted(C[n], key= lambda x : x.sim , reverse=True)

        
        #  Calculate phase =================================================
        
            
    
        
        
        
                

                 

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



