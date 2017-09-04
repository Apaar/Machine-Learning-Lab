import csv
import random
import math
import operator

#Loading our dataset
def dataload(file,split,train=[],test=[]):
    with open(file,'r') as csvfile:
        lines=csv.reader(csvfile)
        data=list(lines)
        for x in range(len(data)-1):
            for y in range(4):
                data[x][y]=float(data[x][y])
            if(random.random()<split):
                train.append(data[x])
            else:
                test.append(data[x])
                
#Checking if this^ function works
trainingSet=[]
testSet=[]
dataload('IRIS.csv', 0.66, trainingSet, testSet)
print('Train: ',len(trainingSet))
print('Test: ',len(testSet))

#Calculating Euclidean diastance
'''
def Edistance(x1, x2, n):
    distance = 0.0
    for i in range(n):
        distance = distance + abs(float(x2[i]) * float(x2[i]) - float(x1[i]) * float(x1[i]))
        distance = pow(distance,0.5)
    return distance
'''

#minkowski
def Edistance(x1, x2, n):
    distance = 0.0
    for i in range(n):
        distance = distance + pow(abs(float(x2[i]) - float(x1[i])),n)
    distance = pow(distance,1/n)
    return distance


#Checking this function
x1 = [2, 2, 2]
x2 = [4, 4, 4]
distance = Edistance(x1, x2, 3)
print(distance)

#Returning K nearest neighbours based on distance
def Neighbors(train, test, k):
    distances = []
    length = len(test)-1
    for x in range(len(train)):
        dist = Edistance(test, train[x], length)
        distances.append((train[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

#Checking this function
train = [[2, 2, 2,'a'], [4, 4, 4,'b']]
test = [5, 5, 5]
k = 1
print(Neighbors(train, test, 1))

#Voting the classes obtained from Neighbours
def Response(neighbors):
    Votes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in Votes:
            Votes[response] += 1
        else:
            Votes[response] = 1
    sortedVotes = sorted(Votes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

#Checking response
neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = Response(neighbors)
print(response)

#Calculating Accuracy
def Accuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

#Checking accuracy
testSet = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
predictions = ['a', 'a', 'a']
accuracy = Accuracy(testSet, predictions)
print(accuracy)


#Combining all functions to get KNN

trainingSet=[]
test=[]
split = 0.67
dataload('IRIS.csv', split, trainingSet, test)
print('Train set: ',len(trainingSet))
print('Test set: ',len(test))
predictions=[]
k = 1
for x in range(len(test)):
    neighbors = Neighbors(trainingSet, test[x], k)
    result = Response(neighbors)
    predictions.append(result)
    print('Predicted=',result,', Actual=',test[x][-1])
accuracy =Accuracy(test, predictions)
print(accuracy)