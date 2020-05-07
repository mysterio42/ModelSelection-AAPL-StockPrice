from datetime import datetime

import numpy as np
from sklearn.preprocessing import MinMaxScaler

from utils.data import fetch_stock, load_data, train_test_split
from utils.model import train_model

if __name__ == '__main__':
    np.random.seed(1)

    fetch_stock('AAPL', "yahoo", datetime(2012, 1, 1), datetime(2017, 5, 31), lags=5)

    features, labels = load_data('data/AAPL-yahoo.csv', 'Direction', ('Lag1', 'Lag2', 'Lag3', 'Lag4'))

    features[['Lag1', 'Lag2', 'Lag3', 'Lag4']] = MinMaxScaler(feature_range=(0, 1)).fit_transform(
        features[['Lag1', 'Lag2', 'Lag3', 'Lag4']])

    data = train_test_split(features, labels, datetime(2017, 1, 1))

    train_model(data)
