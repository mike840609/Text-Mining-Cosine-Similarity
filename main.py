import urllib2
import re

from Poter_Algo.Poter import PorterStemmer
from Poter_Algo.Poter2 import Porter2Stemmer


# run code shortcut :  ctrl alt n 
#  load txt file  from  url 
def loadUrlFromUrl(url_temp): 
    temp = ''
    for line in urllib2.urlopen(url_temp):
        temp += line

    return temp

#  load txt file  from  url 
def loadUrlFromTxt(url_temp):
    file = open(url_temp) 

    return file.read() 

    
# main program  ========================================================================================================
def main():
    # load txt from url
    # str_temp =  loadUrlFromUrl('https://ceiba.ntu.edu.tw/course/35d27d/content/28.txt')

    # load txt from local file 
    str_temp = loadUrlFromTxt('Static_txt/test.txt')

    #  lower case 
    str_temp = str_temp.lower()

    # Strip everything but spaces and alphanumeric
    str_temp = re.sub(r'([^\s\w]|_)+', '', str_temp)
    # print str_temp

    #  split str into array by space 
    arr = str_temp.split()
    
    #  poter algorithm , Porter2Stemmer is better 
    # stemmer_test = PorterStemmer()
    # result_temp = []

    stemmer = Porter2Stemmer()

    # stemming
    results = []

    for i in arr:
            # result_temp.append( stemmer_test.stem(i , 0 , len(i) - 1 ) )
            results.append( stemmer.stem(i) )

    #  type : remove same word
    results = set(results)
    
    # results = list(results)
    # print results 
    # print '\n'

    # stop list 
    stop_temp = loadUrlFromTxt('Static_txt/stopList.txt')
    stop_arr = set(stop_temp.lower().split())
    
    #  subtract stop word 
    results = results.difference(stop_arr)
    print results

    with open("result.txt", "w") as f:
        for word in results:
            f.write(str(word) +"\n")

            
if __name__ == '__main__':
    main()