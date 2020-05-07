# Directory Structure
```
.
├── data
│   └── AAPL-yahoo.csv
├── README.md
├── requirements.txt
├── run.py
└── utils
    ├── data.py
    ├── __init__.py
    └── model.py

2 directories, 7 files
```

# Data - Apple Stock Prices
```text
Features: Lag1, Lag2, Lag3, Lag4, Lag5
```
```text
Labels: UP or DOWN
```

# Experiments

## Model Selection
```text
LogisticRegression
```
```text
KNeighborsClassifier
```

```text
AdaBoostClassifier
```
```text
LinearSVC
```
```text
SVC
```

## Train models

### LogisticRegression
```text
Accuracy Score: 0.5436893203883495
```
### KNeighborsClassifier
```text
Accuracy Score: 0.6310679611650486

```
### AdaBoostClassifier
```text
Accuracy Score: 0.5631067961165048

```

### LinearSVC
```text
Accuracy Score: 0.5533980582524272

```

### SVC
```text
Accuracy Score: 0.5728155339805825
```


# Under The Maintenance