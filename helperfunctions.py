import re
import math

def extract_matrices_from_file(file_path, typ='puzzle'):
    """
    Extracts matrices from a text file.

    Args:
        file_path (str): The path to the text file containing the matrices.

    Returns:
        list: A list of matrices extracted from the file.

    Raises:
        FileNotFoundError: If the file specified by 'file_path' does not exist.

    Notes:
        - The function assumes that the text file follows a specific format:
            - Each matrix is preceded by a title line starting with 'Rätsel' followed by a space and a digit.
            - The matrix is represented as a string enclosed in square brackets [].
            - Each row of the matrix is comma-separated.
            - The matrix is followed by an empty line separating it from the next matrix.

        - The function uses regular expressions to extract the matrices from the file.
        - The matrices are stored as nested lists of integers or string values, depending on the content.

        - Caution: The use of 'eval' to convert the matrix strings to actual lists can be potentially unsafe
          if dealing with untrusted input. Ensure that the file content is trusted or validate it before usage.

    Example:
        Given a file 'sudoku_puzzles.txt' containing the following content:

        Rätsel 1
        [['  ', 2, '  ', 4, 5, 6, 7, '  ', 9], [4, 5, '  ', '  ', 8, '  ', '  ', '  ', 3], ['  ', 8, 9, '  ', '  ', '  ', '  ', 5, 6]]

        Rätsel 2
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        The function call extract_matrices_from_file('sudoku_puzzles.txt') will return:
        [
            [['  ', 2, '  ', 4, 5, 6, 7, '  ', 9], [4, 5, '  ', '  ', 8, '  ', '  ', '  ', 3], ['  ', 8, 9, '  ', '  ', '  ', '  ', 5, 6]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ]
    """
    if typ == 'puzzle':
        matrix_pattern = r"Rätsel \d+\n(.+?)\n\n"
    elif typ == 'solution':
        matrix_pattern = r"Solution \d+\n(.+?)\n\n"
    matrices = []
    with open(file_path, 'r') as file:
        content = file.read()
        
        matches = re.findall(matrix_pattern, content, re.DOTALL)
        for match in matches:
            matrix = eval(match)
            matrices.append(matrix)
    return matrices


##file_path = '../sudoku-generator/sudoku_puzzles.txt'
##matrices = extract_matrices_from_file(file_path)

def calculate_font_size(table_width, table_height, cell_width, cell_height, font_name, initial_font_size, sample_text):
    max_chars_horizontally = math.floor(cell_width / measure_text_width(font_name, initial_font_size, sample_text))
    max_chars_vertically = math.floor(cell_height / measure_text_height(font_name, initial_font_size, sample_text))

    max_font_size_width = initial_font_size
    max_font_size_height = initial_font_size

    while measure_text_width(font_name, max_font_size_width, sample_text) > cell_width:
        max_font_size_width -= 1

    while measure_text_height(font_name, max_font_size_height, sample_text) > cell_height:
        max_font_size_height -= 1

    max_font_size = min(max_font_size_width, max_font_size_height)

    return max_font_size


def measure_text_width(font_name, font_size, sample_text):
    # Calculate and return the width of a text based on the font name and size
    # You can use a library such as Pillow or reportlab to measure text width

    # Example implementation using Pillow:
    from PIL import ImageFont

    # Set the font name and size
    font = ImageFont.truetype(font_name, font_size)

    # Measure the width of a sample text
    text_width = font.getsize(sample_text)[0]

    return text_width


def measure_text_height(font_name, font_size, sample_text):
    # Calculate and return the height of a text based on the font name and size
    # You can use a library such as Pillow or reportlab to measure text height

    # Example implementation using Pillow:
    from PIL import ImageFont

    # Set the font name and size
    font = ImageFont.truetype(font_name, font_size)

    # Measure the height of a sample text
    text_height = font.getsize(sample_text)[1]

    return text_height

'''
# Example usage:
table_width = 252
table_height = 252
cell_width = table_width/9
cell_height = table_height/2
font_name = "Arial"
initial_font_size = 20
sample_text = '9'

font_size = calculate_font_size(table_width, table_height, cell_width, cell_height, font_name, initial_font_size)
print(f"Recommended Font Size: {font_size}")

''' 





