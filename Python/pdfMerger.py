from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import sys

outputFile = PdfFileWriter()
arg1 = input(sys.argv[0])
arg2 = input(sys.argv[1])

print(arg1)
print(arg2)