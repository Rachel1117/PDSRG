from sklearn.ensemble import RandomForestClassifier

def SVM_Score(x_train, y_train, x_test):
    model1 = RandomForestClassifier(n_estimators=160 , max_depth=8)
    model1.fit(x_train, y_train)
    y_pred1 = model1.predict_proba(x_test)[:, 1]
    return y_pred1