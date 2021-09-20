from requests import get

constraint_dict = {'Means like': 'ml', 'Sounds like': 'sl', 'Spelled like': 'sp'}
optional_hint = {'Nothing': '', 'Topic words': 'topics', 'Left context': 'lc', 'Right context': 'rc'}

def search_word(main, main_word, hint='', hint_word=''):
    if hint_word == '' or hint == '':
        request = f'https://api.datamuse.com/words?{main}={main_word}'
    else:
        request = f'https://api.datamuse.com/words?{main}={main_word}&{hint}={hint_word}'

    request_words = get(request).json()

    # for info in request_words:
    #     # var.insert(str(info) + '\n')
    #     print(info) # , end='\n')

    # [info for info in request_words]
    return request_words

if __name__ == '__main__':
    search_word()