from fpdf import FPDF
import sys


def main():
    shirt_png_to_pdf(input('Name: '))

def shirt_png_to_pdf(str):
    output_pdf = FPDF(orientation='P', unit='mm', format='A4')
    output_pdf.add_page()
    output_pdf.set_font('helvetica', 'B', 48)
    output_pdf.cell(40, 40, text=f'CS50 Shirtificate', align='C', center=True)
    output_pdf.image('../shirtificate/shirtificate.png', 10, 75, output_pdf.epw)
    output_pdf.set_font('helvetica', 'B', 22)
    output_pdf.set_text_color(255, 255, 255)
    output_pdf.cell(None, 280, text=f'{str} took CS50', align='C', center=True)
    output_pdf.output(f'{str}-shirtificate.pdf')


if __name__ == '__main__':
    main()
