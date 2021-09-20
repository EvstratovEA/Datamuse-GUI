import os, csv


def write_to_file(words, search_word):
    num_lines = 0

    if os.path.exists('words.csv'):
        with open('words.csv') as file_words_csv:
            for line in file_words_csv:
                num_lines += 1
    else:
        with open('words.csv', 'w', newline='') as file_words_csv:
            words_csv = csv.writer(file_words_csv)
            words_csv.writerow(['', 'MainTag', 'Word', 'Score', 'LinkType'])
            num_lines = 1

    new_line_for_this_word = num_lines

    with open('words.csv', 'a', newline='') as file_words_csv:
        words_csv = csv.writer(file_words_csv)
        for line in words:
            words_csv.writerow([num_lines, search_word, line['word'], line.get('score'), line.get('tags')])
            num_lines += 1

    if not os.path.exists('words_content_table.csv'):
        with open('words_content_table.csv', 'w', newline='') as file_words_table:
            words_table = csv.writer(file_words_table)
            words_table.writerow(['Word', 'FirstRow', 'EndRow'])

    with open('words_content_table.csv', 'a', newline='') as file_words_table:
        words_table = csv.writer(file_words_table)
        words_table.writerow([search_word, new_line_for_this_word, num_lines - 1])


if __name__ == '__main__':
    write_to_file()
