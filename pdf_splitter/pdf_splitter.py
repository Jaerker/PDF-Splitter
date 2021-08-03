from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def Split(pathToSplit, finishPath = None):
    
    if finishPath == None:
        finishPath = pathToSplit[:len(pathToSplit)-4]
    
    inputpdf = PdfFileReader(open(pathToSplit, "rb"),strict=False)
    splitpath = pathToSplit.split('/')
    
    fName = splitpath[len(splitpath)-1][:-4]
        
    
    if not os.path.exists(finishPath):
        os.mkdir(finishPath)
		
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open( finishPath + "/" + fName + "-" + str(i+1) + ".pdf", "wb") as outputStream:
            output.write(outputStream)		
                

def Test():
    return "it works"