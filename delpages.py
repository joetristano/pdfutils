import PyPDF2
import click
import shutil

@click.command()
@click.option('--file')
@click.option('--page_range', nargs=2, multiple=True,type=int)
def delpages(file,page_range):
    print(file)
    print(page_range)
    pdf = open(file,'rb')
    pdf_reader = PyPDF2.PdfReader(pdf)

    pdf_writer = PyPDF2.PdfWriter()
    pagenum = 1
    for page in pdf_reader.pages:
        print(pagenum)
        delPage = False
        for tup in page_range:
            r = range(tup[0],tup[1]+1)
            if pagenum in r:
                delPage = True
        if not delPage:
            pdf_writer.add_page(page)
        pagenum += 1

    pdf_out = open('delpagesd.pdf','wb')
    pdf_writer.write(pdf_out)

    pdf_out.close()
    pdf.close()

    shutil.move('delpagesd.pdf',file)

if __name__ == '__main__':
    delpages()
