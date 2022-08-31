from PyPDF2 import PdfFileMerger
def by_appending():
    merger = PdfFileMerger()
    f1 = open("samplePdf1.pdf", "rb")
    merger.append(f1)
    merger.append("samplePdf2.pdf")
    merger.write("mergedPdf.pdf")

def by_inserting():
    merger = PdfFileMerger()
    merger.append("samplePdf1.pdf")
    merger.merge(0, "samplePdf2.pdf")
    merger.write("mergedPdf1.pdf")

if __name__ == "__main__":
    by_appending()
    by_inserting()
