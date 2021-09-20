import os, csv

def update_content_table():
    try:
        os.remove('words_content_table.csv')
    except:
        pass

    with open('words_content_table.csv', 'w', newline='') as content_table:
        word_content = csv.writer(content_table)
        word_content.writerow(['Word', 'FirstRow', 'EndRow'])

    with open('words.csv') as words_csv:
        words_table = csv.reader(words_csv)
        tag_word, first_row, end_row = '', 1, 1
        with open('words_content_table.csv', 'a', newline='') as content_table:
            word_content = csv.writer(content_table)
            for index, row in enumerate(words_table):
                if index == 1:
                    tag_word = row[1]
                    break

            for row in words_table:
                if tag_word == row[1]:
                    end_row += 1
                else:
                    word_content.writerow([tag_word, first_row, end_row])
                    tag_word = row[1]
                    end_row += 1
                    first_row = end_row

            word_content.writerow([tag_word, first_row, end_row])

if __name__ == '__main__':
    update_content_table()