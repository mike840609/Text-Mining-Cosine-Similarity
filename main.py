import urllib2
from Poter  import PorterStemmer

# from nltk.stem.lancaster import LancasterStemmer


# run code shortcut :  ctrl alt n 
#  load txt file  from  url 
def loadUrlFromUrl(url_temp): 

    temp = ''

    for line in urllib2.urlopen(url_temp):
        # print line
        temp += line

    return temp

#  load txt file  from  url 
def loadUrlFromTxt(url_temp):
    temp = ''
    file = open(url_temp) 
    return file.read() 
    

# ========================================================================================================



#  main program 

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
    

    #  poter algorithm
    stemmer = PorterStemmer()
    # arr = stemmer.stem(arr)


    #  type : remove same word    
    results = []
    for i in arr:
        if i not in results:
            results.append( stemmer.stem(i , 0 , len(i) - 1 ) )



    print results


if __name__ == '__main__':
    main()




