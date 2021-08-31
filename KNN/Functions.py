import numpy as np

def leaveOneOutCrossValidation(self):
    return 3

def searchFunction(self, tableData):
    setOfFeatures = []

    for i in size(tableData,2)-1:#,1 for python
        print("On the " + str(i) + " th level of the search tree")
        featureToAdd = []
        bestAccuracy = 0

        for k in size(tableData,2):
            if isempty(intersect(setOfFeatures, k)): #if k in setoffeatures
                print('--Considering adding the ' + str(k)+ ' feature')
                accuracy = leaveOneOutCrossValidation()

                if (accuracy > bestAccuracy):
                    bestAccuracy = accuracy
                    featureToAdd = k
    setOfFeatures[i] = featureToAdd
    print('On level '+ str(i)+' i added feature '+ str(featureToAdd) + ' to current set')


l = [1, 2]
nplist = np.array(l)
print(nplist)