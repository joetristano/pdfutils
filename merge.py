import PyPDF2
import click
import shutil

@click.command()
@click.option('--file',multiple=True,default=[])
@click.option('--outputfile',default='merge.pdf')
def merge(file,outputfile):
    print(file)
    print(outputfile)
    pdf_out = open(outputfile,'wb')
    pdf_writer = PyPDF2.PdfWriter()
    for fname in file:
        pdf = open(fname,'rb')
        pdf_reader = PyPDF2.PdfReader(pdf)

        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
        pdf.close()

    pdf_writer.write(pdf_out)

    pdf_out.close()


if __name__ == '__main__':
    merge()
