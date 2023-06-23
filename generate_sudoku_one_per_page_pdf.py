from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_single_page(c,width, height, margin, title, subtitle, matrix):

    pdfmetrics.registerFont(TTFont('Lobster', 'Fonts/Lobster-Regular.ttf')) 
    pdfmetrics.registerFont(TTFont('DancingScript', 'Fonts/DancingScript-VariableFont_wght.ttf'))
    # Konfig
    title_font = "Lobster"
    title_size = 80

    subtitle_font = "DancingScript"
    subtitle_size = 50

    table_font_size = 30
        # Erstellen eines Canvas-Objekts für das PDF
    #c = canvas.Canvas(docname, pagesize=(width, height))

    # Setzen der Schriftart und -größe für den Titel
    c.setFont(title_font, title_size)
    # Positionierung und Schreiben des Titels
    c.drawCentredString(width / 2, height - 2 * margin, title)

    # Setzen der Schriftart und -größe für den Untertitel
    c.setFont(subtitle_font, subtitle_size)
    # Positionierung und Schreiben des Untertitels
    c.drawCentredString(width / 2, height - 3.5  * margin, subtitle)

    # Leere Zeile
    c.drawString(margin, height - 6 * margin, "")

    # Berechnung der verfügbaren Breite für die Tabelle
    table_width = width - 5 * margin

    # Berechnung der Tabellenhöhe entsprechend zur Tabellenbreite
    table_height = table_width

    # Erstellen der Tabelle
    data = matrix

    # Erstellen eines Stylesheets für die Tabelleneinträge
    stylesheet = getSampleStyleSheet()
    cell_style = stylesheet['BodyText']
    cell_style.alignment = 1  # Zentrierte Ausrichtung der Zellen

    table = Table(data, colWidths=table_width / len(data[0]),
                        rowHeights=table_height / len(data))

    # Festlegen der Rahmenlinien für die Tabelle
    linesize = 3
    linecolor = colors.black
    table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 1, linecolor),  # Rahmenlinien für alle Zellen
        ("BOX", (0, 0), (-1, -1), linesize + 1, linecolor),  # Rahmenlinien für äußere Tabelle
        ("BOX", (0, 0), (2, 2), linesize, linecolor) ,  # Dickere Rahmenlinien für 3x3-Blöcke
         ("BOX", (0, 0), (5, 5), linesize, linecolor),
          ("BOX", (0, 0), (8, 8), linesize, linecolor),
        ("BOX", (3, 3), (8, 8), linesize, linecolor),
        ("BOX", (6, 6), (8, 8), linesize, linecolor),     
       ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),       # Vertikale Ausrichtung mittig
        ("FONTSIZE", (0, 0), (-1, -1), table_font_size),    # Schriftgröße der Tabelleneinträge
        ("TEXTCOLOR", (0, 0), (-1, -1), linecolor),# Textfarbe
        ("ALIGN", (0, 0), (-1, -1), "CENTER")
    ]))

    # Berechnung der Position, um die Tabelle mittig auf der Seite zu platzieren
    table_x = (width - table_width) / 2
    table_y = height - 2 * margin - table_height

    # Zeichnen der Tabelle auf dem Canvas
    table.wrapOn(c, table_width, table_height)
    table.drawOn(c, table_x, table_y)

    table.drawOn

    #c.show
    # Speichern und Schließen des PDF-Dokuments
    #c.save()



'''
# Beispielaufruf der Funktion
width = 8.5 * inch  # Breite des Dokuments (in diesem Fall 8,5 Zoll)
height = 11 * inch  # Höhe des Dokuments (in diesem Fall 11 Zoll)
margin = 0.5 * inch  # Rand des Dokuments (in diesem Fall 0,5 Zoll)
title = "Sudoku"
subtitle = "Rätsel 1"
matrix = [
    [1, 2, 3, 4, 5, " ", 7, 8, 9],
    [4, 5, 6, 7, 8, " ", 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]
font_size = 10  # Schriftgröße für die Tabelleneinträge
docname = "output1.pdf"
generate_pdf(docname,width, height, margin, title, subtitle, matrix)
'''

#generate_multiple_page()
