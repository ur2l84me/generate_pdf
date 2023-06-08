from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math
from helperfunctions import calculate_font_size

def generate_pdf(docname, width, height, margin, title, matrices,subtitle, 
num_tables_per_page = 4,
                tables_per_row = 2, table_font_size=9, linesize = 1):

    pdfmetrics.registerFont(TTFont('Lobster', 'Fonts/Lobster-Regular.ttf')) 
    pdfmetrics.registerFont(TTFont('DancingScript', 'Fonts/DancingScript-VariableFont_wght.ttf'))
    # Konfig
    title_font = "Lobster"
    title_size = 20

    subtitle_font = "DancingScript"
    subtitle_size = 18

    

    number_rows = math.ceil(num_tables_per_page/tables_per_row)
    # Erstellen eines Canvas-Objekts für das PDF
    c = canvas.Canvas(docname, pagesize=(width, height))

    # Setzen des Titels auf jeder Seite
    c.setFont(title_font, title_size)
    c.drawCentredString(width / 2, height - margin, title)

    num_matrices = len(matrices)

    # Berechnung der Breite einer Tabelle
    table_width_tmp = (width - (3 * margin)) / tables_per_row
    table_height_tmp = (height - (3 * margin)) / number_rows
    table_width = min(table_width_tmp,table_height_tmp )
    # Berechnung der Höhe einer Tabelle, um das Seitenverhältnis beizubehalten
    table_height = table_width
    space_between_tables_cols =  (width - 2.1*margin - tables_per_row * table_width)/tables_per_row
    space_between_tables_row =  (height - 2.1*margin - number_rows * table_height)/number_rows
    


    cell_width = table_width/10
    cell_height = table_height/10
    font_name = "Arial"
    initial_font_size = 40
    sample_text = '9'
    # table_font_size = calculate_font_size(table_width, table_height, 
    # cell_width, cell_height, font_name, initial_font_size, sample_text)

    print('table_font_size: '+ str(table_font_size) )



    print('num_tables_per_page: ' + str(num_tables_per_page))
    print('table_width: '+ str(table_width))

    # Berechnung der Anzahl der Seiten basierend auf der Anzahl der Matrizen und Tabellen pro Seite
    num_pages = (num_matrices + num_tables_per_page - 1) // num_tables_per_page

    for page in range(num_pages):
        # Neue Seite
        c.showPage()

        for table_idx in range(num_tables_per_page):
            matrix_idx = (page * num_tables_per_page) + table_idx
            #print(matrix_idx)
            if matrix_idx >= num_matrices:
                # Alle Matrizen wurden auf den Seiten platziert
                break

            matrix = matrices[matrix_idx]

            # Berechnung der Position der Tabelle auf der Seite
            row = table_idx // tables_per_row
            col = table_idx % tables_per_row
            table_x = margin + col * table_width +col * space_between_tables_cols
            table_y = height - (2 *margin + (row + 1) * table_height) - row * space_between_tables_row

            data = matrix

            table = Table(data, colWidths=[table_width / len(data[0])] * len(data[0]),
                          rowHeights=[table_height / len(data)] * len(data))

            
            linecolor = colors.black
            table.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 1, linecolor),  # Rahmenlinien für alle Zellen
                ("BOX", (0, 0), (-1, -1), linesize + 1, linecolor),  # Rahmenlinien für äußere Tabelle
                ("BOX", (0, 0), (2, 2), linesize +1, linecolor) ,  # Dickere Rahmenlinien für 3x3-Blöcke
                ("BOX", (0, 0), (5, 5), linesize +1, linecolor),
                ("BOX", (0, 0), (8, 8), linesize +1, linecolor),
                ("BOX", (3, 3), (8, 8), linesize +1, linecolor),
                ("BOX", (6, 6), (8, 8), linesize +1, linecolor),     
           ("VALIGN", (0, 0), (-1, -1), "TOP"),       # Vertikale Ausrichtung mittig
                ("FONTSIZE", (0, 0), (-1, -1), table_font_size),    # Schriftgröße der Tabelleneinträge
                ("TEXTCOLOR", (0, 0), (-1, -1), linecolor),# Textfarbe
               ("ALIGN", (0, 0), (-1, -1), "CENTER")
            ]))

            

            table.wrapOn(c, table_width, table_height)
            table.drawOn(c, table_x, table_y)

            # Hinzufügen des Texts "Rätsel" + Nummer der Matrix über der Tabelle
            c.setFont(subtitle_font, subtitle_size)
            text = f"{subtitle} {matrix_idx + 1}"
            text_width = c.stringWidth(text, subtitle_font, subtitle_size)
            text_x = table_x + (table_width - text_width) / 2
            text_y = table_y + table_height + margin / 2
            c.drawString(text_x, text_y, text)

    # Speichern und Schließen des PDF-Dokuments
    c.save()




