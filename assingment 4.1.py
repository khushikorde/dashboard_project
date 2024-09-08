def count_lines_words_characters(input_file, output_file):
    """Counts the number of lines, words, and characters in a text file and writes the results to a new file.

    Args:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """

    lines = 0
    words = 0
    characters = 0

    with open(input_file, 'r') as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)

    with open(output_file, 'w') as f:
        f.write(f"Lines: {lines}\n")
        f.write(f"Words: {words}\n")
        f.write(f"Characters: {characters}\n")

