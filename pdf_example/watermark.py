import PyPDF4

template = PyPDF4.PdfFileReader(open('merged.pdf', 'rb'))
watermark = PyPDF4.PdfFileReader(open('213_wtr.pdf', 'rb'))
output = PyPDF4.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermakedoutput.pdf', 'wb') as file:
        output.write(file)