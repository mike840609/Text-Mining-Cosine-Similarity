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
            
            #  add heap to array P
            #  call by value 
            P[int(doc_1.id)] = C[int(doc_1.id)][:]
            heapify_max(P[int(doc_1.id)])
            # P[int(doc_1.id)].sort(key=lambda x: x.sim, reverse=True)
            
            # delete self sim
            P[int(doc_1.id)] = [item for item in  P[int(doc_1.id)] if item.index != int(doc_1.id)]

        # print([(ele.index, ele.sim) for ele in C[1]])
        # print ([(ele.index, ele.sim) for ele in P[1]])
        # print("=============")
        # print([(ele.index, ele.sim) for ele in C[2]])
        # print ([(ele.index, ele.sim) for ele in P[2]])
    

        #  Calculate phase ==================================================================================================

        for time in range(1,len(doc_list)):

            max_sim = -1
            max_idx = 0

            # argmax  1 - 1095 
            for idx in range(1,1096):
                if I[idx] == 1 : 
                    if P[idx][0].sim > max_sim:
                        max_idx = idx
                        max_sim = P[max_idx][0].sim

            k1_idx = max_idx
            k2_idx = P[k1_idx][0].index            

            A.append([k1_idx,k2_idx])

            I[k2_idx] = 0 

            P[k1_idx] = []

            for idx in range(1,1096):

                if (I[idx] == 1 and idx != k1_idx):

                    # delete (C[i][k1])  , delete (C[i][k2])
                    P[idx] = [ele for ele in P[idx] if (ele.index != k1_idx and ele.index != k2_idx)]
                    
                    C[k1_idx][idx].sim = min(C[k1_idx][idx].sim , C[k2_idx][idx].sim)
                    P[k1_idx].append(C[k1_idx][idx])
                    
                    C[idx][k1_idx].sim = C[k1_idx][idx].sim
                    P[idx].append(C[idx][k1_idx])
                    
                    heapify_max(P[idx])
                    heapify_max(P[k1_idx])

                    # P[idx].sort(key=lambda x: x.sim, reverse=True)


        return A
                    
    
    def writeClusterToFile(self, pair_list):

        cluster_num  = [ 8 ,13 ,20 ] 

        # cluster_num  = [ 20] 
        for num in cluster_num:
            #  8 ,13, 20     
            # init list ============================================================================================================
            Clusters = list(range(1,1096))
            for idx,ele in enumerate(Clusters):
                Clusters[idx] = [ele]

            # print (Clusters)

            # Calculate  ============================================================================================================
            for pair in pair_list:
                if len(Clusters) == num:
                    break
            
                idx1 = -1
                idx2 = -1

                for idx , clu in enumerate(Clusters):
                    # print (clu)
                    if pair[0] in clu:
                        idx1 = idx
                    if pair[1] in clu:
                        idx2 = idx
                
                Clusters[idx1] = Clusters[idx1] + Clusters[idx2]
                del Clusters[idx2]
            
            # write to file ========================================================================================================
            text_file = open(str(num) + '.txt', "w")
            for idx , clu in enumerate(Clusters) :
                Clusters[idx] =  sorted(clu)
                
                for doc_id in Clusters[idx]:
                    text_file.write(str(doc_id)+'\n')
                
                text_file.write('\n')






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


