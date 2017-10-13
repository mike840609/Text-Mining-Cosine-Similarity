import os
import re
import math
import collections

import os
import errno

from IR import IR_operator
from collections import Counter


class DocOperator:

    doc_list = []
    stopWord_list = []

    documentsFreq = {}
    

    def __init__(self , doc_path):
        
        self.doc_path = doc_path
        stop_temp = open('Static_txt/stopList.txt').read()
        self.stopWord_list = stop_temp.lower().split()

    def genrateDoc(self):

        self.doc_list = []

        all_files = os.listdir(self.doc_path)

        for file_name in all_files:

            file = open(self.doc_path + file_name)
            file_name = re.sub(r'([^0-9]|_)+', '', file_name)

            doc_obj = Doc(file_name , file.read(), self.stopWord_list)

            self.doc_list.append(doc_obj)
        
        return self.doc_list
    
    def docFreqCal(self):
            for i in self.doc_list:    
                for k,v in i.getTermDict().items():
                    
                    if k in self.documentsFreq.keys():
                        self.documentsFreq[k]['df'] += 1 
                    else:
                        self.documentsFreq[k] = v

    def indexingDict(self):
        
        self.documentsFreq = collections.OrderedDict(sorted(self.documentsFreq.items()))
        
        for idx , k in enumerate( self.documentsFreq.keys()):
            self.documentsFreq[k]['index'] = (idx + 1)
    

    # calculate each terms tf-idf
    def cal_Tf_Idf(self):
        
        N = float(len(self.doc_list))

        for doc in self.doc_list:

            # print doc.id + '================================================================================='
            tf_idf_unit_vector_addition = 0 
            for term in doc.getTermFrequency():

                tf =  doc.getTermFrequency()[term]
                df = float(self.documentsFreq[term]['df'])
                idf = math.log10(N/df)
                tf_idf = tf * idf

                # print 'N : ' + str(N)
                # print 'tf : ' + str(tf)  + '  df :' + str(df) + '   idf :'+ str(idf) 
                # print 'term :' + str(term) + '   tf-idf :' + str(tf_idf)

                tf_idf_unit_vector_addition += math.pow(tf_idf,2)
                doc.getTermDict()[term]['tf-idf'] = tf_idf
            

            # tf_idf unit vector
            unit_denominator = math.sqrt(tf_idf_unit_vector_addition)
            for term in doc.getTermFrequency():
                doc.getTermDict()[term]['tf-idf'] /= unit_denominator
                # print 'term :' + str(term) + '   tf-idf :' + str(doc.getTermDict()[term]['tf-idf'])
    

    def write_Tf_Idf_ToFile(self,path):

        for doc in self.doc_list:
            
            self.make_sure_path_exists(path)

            file_path = path +'%s.txt' %str(doc.id)
            

            with open(file_path , "w") as f :

                # print "document id: " + str(doc.id) + '================================================='
                # print "doc length : " + str(len(doc.getTermFrequency()))
                f.write(str(len(doc.getTermFrequency())) + '\n')

                for term in doc.getTermFrequency():
                    # print  self.documentsFreq[term]['index']
                    # print  doc.getTermDict()[term]['tf-idf']
                    f.write('{:<15}'.format(self.documentsFreq[term]['index']) + '{:<30}'.format(doc.getTermDict()[term]['tf-idf'])+ '\n' )




    def getDoc(self):
        return self.documentsFreq

    def writeToFile(self, path):

        with open(path , "w") as f :

            for k , v in self.documentsFreq.items():

                # print '{:<15}'.format(v['index']) + '{:<30}'.format(k) + '{:<10}'.format(v['df'])

                f.write('{:<15}'.format(v['index']) + '{:<30}'.format(k) + '{:<10}'.format(v['df']) + '\n' )

                # print v['index']
                # print k
                # print v['df'] 

            # with open(path , "w") as f :
            #     f.write("123" + '')
            
    def make_sure_path_exists(self , path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    
#  each Doc Implement 
class Doc:

    id = '' 
    obj = ''
    all_terms_length = 0
    terms = {}
    termsFrequency = {}

    def __init__(self,id ,content, stopWord_list):

        self.id = id

        # IR opration
        self.obj = IR_operator() 
        self.obj.set_str_temp(content)
        self.obj.tokenization()
        self.obj.removeStopWord(stopWord_list)
        self.obj.stemming()

        self.initTermFrequency()
        self.calTermFrequency()
        

    def initTermFrequency(self):
        
        results_set = set(self.obj.results)
        self.terms = dict((k,{'index': 0 ,'df': 1, 'tf-idf': 0 }) for k in results_set)
    
    def calTermFrequency(self):
        self.termsFrequency = dict(Counter(self.obj.results))

    # get all term ,  value == 1 
    def getTermDict(self):
        return self.terms

    def getTermFrequency(self):
        return self.termsFrequency


