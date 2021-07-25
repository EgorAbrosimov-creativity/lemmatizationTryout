import pandas as pd
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='ru')


def transform(latin_nonlatin_list: list) -> list:
    result_non_latin = []
    for record in latin_nonlatin_list:
        new_record = [(elem[0],
                        morph.parse(elem[1])[0].normal_form)
                        for elem in record[1]
                      ]
        result_non_latin.append(new_record)

    result = [
        (latin_nonlatin_list[i][0], result_non_latin[i])
        for i in range(len(latin_nonlatin_list))
    ]

    return result