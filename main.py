from IR import *
#  R06725054
# main program  ========================================================================================================
def main():
    #  initialize obj
    
    # you can use the url or local file to initialize object
    # obj = IR_operator('https://ceiba.ntu.edu.tw/course/35d27d/content/28.txt ')
    obj = IR_operator('Static_txt/test.txt')
    obj.tokenization()
    obj.stemming()
    obj.removeSameWordAndStopWord('Static_txt/stopList.txt')
    obj.writeResultToFile('result.txt')

    obj.log()

if __name__ == '__main__':
    main()
    




    
