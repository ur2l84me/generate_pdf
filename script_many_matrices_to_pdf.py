from helperfunctions import extract_matrices_from_file
from generate_pdf import generate_pdf 
from generate_sudoku_one_per_page_pdf import generate_single_page
from reportlab.lib.units import inch


file_path = '../sudoku-generator/sudoku_puzzles_large_print_book1_easy.txt'
matrices = extract_matrices_from_file(file_path, typ = 'puzzle')

width = 8.5 * inch
height = 11 * inch
margin = 0.5 * inch
num_tables_per_page = 1 
title = "Sudoku"
docname = 'sudoku_puzzles_large_print_book1_easy_Raetsel.pdf'
subtitle = 'Puzzle'
subsubtitle = 'Easy'
tables_per_row = 1
# Generiere Puzzel 
generate_pdf(docname, 
             width, 
             height, 
             margin, 
             title, 
             matrices,
             subtitle, 
             subsubtitle,
             num_tables_per_page,
             tables_per_row,
             table_font_size = 20,
             linesize = 2)

# matrices = extract_matrices_from_file(file_path, typ = 'solution')
# docname = 'Test-Book1_Loesung.pdf'
# subtitle = 'Lösung'
# num_tables_per_page = 9
# tables_per_row = 3
# # Generiere Puzzel 
# generate_pdf(docname, 
#             width, 
#             height, 
#             margin, 
#             title, 
#             matrices,
#             subtitle, 
#             num_tables_per_page,
#             tables_per_row,
#             table_font_size = 9)





