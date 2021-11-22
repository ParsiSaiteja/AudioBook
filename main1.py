import pyttsx3
import PyPDF4

book = open('oops.pdf', 'rb')
pdfReader = PyPDF4.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(7, pages):
 page = pdfReader.getPage(7)
 text = page.extractText()
 speaker.say(text)
 speaker.runAndWait()