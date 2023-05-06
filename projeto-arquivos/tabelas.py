from random import randint
from openpyxl import Workbook

ROWS, COLS = 100, 100

wb = Workbook()

# Seleciona planilha ativa
ws = wb.active

# Rows: linhas || Cols: colunas
for r in range(1, ROWS+1):
    for c in range (1, COLS+1):
        # preenche planilha ativa
        ws.cell(row=r, column=c, value=randint(1, 100))


wb.title = "Aleatorio"
wb.save("aleatorios.xlsx")