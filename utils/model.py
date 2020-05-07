from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC


def train_model(data):
    models = [LogisticRegression(),
              KNeighborsClassifier(310),
              AdaBoostClassifier(),
              LinearSVC(max_iter=3000),
              SVC(C=1000.0, degree=5, gamma=0.0001, kernel='rbf')]
    for model in models:
        model.fit(data['features']['train'], data['labels']['train'])

        preds = model.predict(data['features']['test'])

        score = accuracy_score(preds, data['labels']['test'])
        cm = confusion_matrix(preds, data['labels']['test'])
        print(f'{model.__class__}: {score}')
