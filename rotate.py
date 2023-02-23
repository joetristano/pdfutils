import PyPDF2
import click
import shutil

@click.command()
@click.option('--file')
@click.option('--page_range', nargs=2, type=int)
@click.option('--angle', default=90.0, type=float)
def rotate(file,page_range,angle):
    print(file)
    print(page_range)
    print(angle)
    pdf = open(file,'rb')
    pdf_reader = PyPDF2.PdfReader(pdf)

    pdf_writer = PyPDF2.PdfWriter()
    r = range(page_range[0],page_range[1]+1)
    pagenum = 1
    for page in pdf_reader.pages:
        print(pagenum)
        if pagenum in r:
            print("\trotate page #%s" % pagenum)
            page.rotate(angle)
        pdf_writer.add_page(page)
        pagenum += 1

    pdf_out = open('rotated.pdf','wb')
    pdf_writer.write(pdf_out)

    pdf_out.close()
    pdf.close()

    shutil.move('rotated.pdf',file)

if __name__ == '__main__':
    rotate()
