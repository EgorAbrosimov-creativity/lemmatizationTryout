import pandas as pd


def tax_data_clean_to_list(data_df: pd.DataFrame) -> list:
    # leave only one column, the useful one
    data = data_df.iloc[:, 1]

    # into list
    data_list = data.values.tolist()
    data_list = [el for el in data_list]

    return data_list


def string_in_charset(s: str, chrset: set):
    # may be optimized duno
    return set(s).issubset(chrset)


def latin_nonlatin_split(s: str):
    # tokenize
    tokens = s.split(' ')
    # define two sets of symbols for two parts of 'sentence'
    latin_plus_nums = set([chr(ind) for ind in range(65, 91)]
                          + [chr(ind) for ind in range(97, 122)]
                          + [chr(ind) for ind in range(48, 58)])

    non_latin_chars = set([chr(ind) for ind in range(ord('а'), ord('я') + 1)]
                          + [chr(ind) for ind in range(ord('А'), ord('Я') + 1)])
    # store split data as two lists, every element structured like (original_index, value)
    latin = [(ind, tokens[ind])
             for ind in range(len(tokens))
             if string_in_charset(tokens[ind], latin_plus_nums)
             ]

    non_latin = [(ind, tokens[ind])
                 for ind in range(len(tokens))
                 if string_in_charset(tokens[ind], non_latin_chars)
                 ]

    return latin, non_latin


def latin_non_latin_all_data(l: list) -> list:
    return [latin_nonlatin_split(rec) for rec in l]


def arrange_in_lists(latin_nonlatin_processed: list, initial_data_list: list) -> list:
    right_order_list = []

    result_non_latin = [rec[1] for rec in latin_nonlatin_processed]
    latin = [rec[0] for rec in latin_nonlatin_processed]
    for i in range(len(latin_nonlatin_processed)):
        # get initial sentence length
        sent_len = len(initial_data_list[i].split(' '))
        # create new version of sentence
        sent = [''] * sent_len
        # fill latins and non-latins
        for word_pos in latin[i]:
            sent[word_pos[0]] = word_pos[1]
        for word_pos in result_non_latin[i]:
            sent[word_pos[0]] = word_pos[1]
        # save the result
        right_order_list.append(sent)

    return right_order_list


def make_right_order_sentences(latin_nonlatin_processed: list, initial_data_list: list) -> list:
    right_order_sentences = [
        ' '.join(l)
        for l in arrange_in_lists(latin_nonlatin_processed, initial_data_list)
    ]
    return right_order_sentences