import download
import helperFunctions
import pyMorphyLemmatizer

df = download.download_tax_data('data/tax-suggestions-ru.csv')
print(df.head(5), '\n')

data_list = helperFunctions.tax_data_clean_to_list(df)
print(data_list[:5], '\n')

data_eng_ru_split = helperFunctions.latin_non_latin_all_data(data_list)
print(data_eng_ru_split[:5], '\n')

data_eng_ru_lem = pyMorphyLemmatizer.transform(data_eng_ru_split)
print(data_eng_ru_lem[:30])

new_sentences = helperFunctions.make_right_order_sentences(data_eng_ru_lem, data_list)
print(new_sentences[:5])