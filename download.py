import pandas as pd


def download_tax_data(location: str) -> pd.DataFrame:
    # put into pd.DataFrame
    tx_data = pd.read_csv('data/tax-suggestions-ru.csv')

    return tx_data