from sklearn.linear_model import SGDClassifier

classifier = SGDClassifier()
#sevens = tylko obrazki z 7
#cały zbiór zmienić label
#dla 7 label True
#dla innych label False
#classifier.fit(zbiór_orazow, zbior_labeli)
#Sprawdzamy skuteczność -- ile znaków ze zbioru testowego zostało zakwalifikowane poprawnie
#classifier.predict(zbior)