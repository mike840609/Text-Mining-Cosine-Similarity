import urllib2
from Poter  import PorterStemmer
from Poter2 import Porter2Stemmer

# from nltk.stem.lancaster import LancasterStemmer


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
    str_temp = loadUrlFromTxt('test.txt')

    #  lower case 
    str_temp = str_temp.lower()
    str_temp = str_temp.replace('.', '')
    str_temp = str_temp.replace(',', '')

    #  split str into array by space 
    arr = str_temp.split()

    # print str_temp
    
    #  poter algorithm , Porter2Stemmer is better 

    # stemmer = PorterStemmer()
    stemmer = Porter2Stemmer()

    
    # stemming
    results = []
    
    for i in arr:
            # results.append( stemmer.stem(i , 0 , len(i) - 1 ) )
            results.append( stemmer.stem(i) )

    #  type : remove same word
    results = set(results)
    
    # results = list(results)
    print results 
    print '\n'
    

    # stop list 
    stop_temp = loadUrlFromTxt('stopList.txt')
    stop_temp = stop_temp.lower()
    stop_arr = set(stop_temp.split())
    # print stop_arr

    #  subtract stop word 
    results = results.difference(stop_arr)
    print results

            

if __name__ == '__main__':
    main()




