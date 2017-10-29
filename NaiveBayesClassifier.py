#The first step is to handle the data by loading it into a CSV file and
import csv
def loadCsv(filename):
    lines = csv.reader(open(filename, 'rb'))# read in binary mode
    dataset = list(lines)
    for i in range(len(dataset)):# we start the condition
        dataset[i] = [float(x) for x in dataset[i]]#ok data will be in float
     return dataset

filename = 'pima-indians-diabetes.data.csv'
dataset = loadCsv(filename)
print 'loaded data file {0} with {1} rows'.format(filename, len(dataset))

# the function will split dataset into a given split ratio
import random
def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset)*splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))# we will find a random range from the dataset
        trainSet.append(copy.pop(index)) # we will return the last dataset[]
        return [trainSet, copy]

dataset = [[1],[2],[3],[4],[5]]
splitRatio = 0.67

train, test = splitDataset(dataset, splitRatio)
print "Split {0} rows into train with {1} and test with {2}".format(len(dataset), train, test)

# now we will start to summarise the data
