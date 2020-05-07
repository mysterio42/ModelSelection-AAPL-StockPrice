import os

import numpy as np
import pandas as pd
import pandas_datareader.data as web

DATA_DIR = 'data/'


def fetch_stock(stock_symbol, data_source, start_date, end_date, lags=5):
    path = DATA_DIR + stock_symbol + '-' + data_source + '.csv'

    if not os.path.isfile(path):
        print(f'fetching into {path}')
        s = web.DataReader(stock_symbol, data_source, start_date, end_date)['Adj Close']
        daily_returns = ((s / s.shift(1)) - 1) * 100
        df = pd.DataFrame()
        df['Today'] = daily_returns
        for i in range(lags):
            df[f'Lag{str(i + 1)}'] = daily_returns.shift(i + 1)
        df['Direction'] = np.sign(df['Today'])
        df.drop(df.index[:6], inplace=True)
        df.to_csv(path, index=True)


def load_data(path, label, *features):
    df = pd.read_csv(path, index_col='Date')
    df.index = pd.to_datetime(df.index)
    return df[list(*features)], df[label]


def train_test_split(features, labels, sep):
    features_train, features_test, = features[features.index < sep], features[features.index >= sep]
    labels_train, labels_test = labels[labels.index < sep], labels[labels.index >= sep]
    data = {
        'features': {
            'train': features_train,
            'test': features_test
        },
        'labels': {
            'train': labels_train,
            'test': labels_test
        }
    }
    return data
