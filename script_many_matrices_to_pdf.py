from helperfunctions import extract_matrices_from_file
from generate_pdf import generate_pdf 
from reportlab.lib.units import inch


file_path = '../sudoku-generator/sudoku_puzzles.txt'
matrices = extract_matrices_from_file(file_path, typ = 'puzzle')

width = 8.5 * inch
height = 11 * inch
margin = 0.5 * inch
num_tables_per_page = 4 
title = "Sudoku"
docname = 'Test-Book1_Raetsel.pdf'
subtitle = 'Rätsel'
tables_per_row = 2 
# Generiere Puzzel 
generate_pdf(docname, 
             width, 
             height, 
             margin, 
             title, 
             matrices,
             subtitle, 
             num_tables_per_page,
             tables_per_row,
             table_font_size = 20,
             linesize = 2)

matrices = extract_matrices_from_file(file_path, typ = 'solution')
docname = 'Test-Book1_Loesung.pdf'
subtitle = 'Lösung'
num_tables_per_page = 9
tables_per_row = 3
# Generiere Puzzel 
generate_pdf(docname, 
            width, 
            height, 
            margin, 
            title, 
            matrices,
            subtitle, 
            num_tables_per_page,
            tables_per_row,
            table_font_size = 9)





