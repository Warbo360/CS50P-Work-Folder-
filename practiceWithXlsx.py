from openpyxl import load_workbook


def main():
    wb = load_workbook(filename='Cleaning Samples Template.xlsx')
    ws = wb.active
    c = ws['B1':'C5']
    for row in ws.values:
        for i in range(len(row)):
            print(row[i])


main()
