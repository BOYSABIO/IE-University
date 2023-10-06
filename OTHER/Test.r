library(mlbench)
library(caret)

# Retreive Data
data("BostonHousing")
data = BostonHousing

print(summary(data))

# MEDV is TARGET VARIABLE

# Split Data
index = createDataPartition(data$medv, p = 0.7, list = F)
train = data[index,]
test = data[-index,]


# Linear Regression
lm = train(medv~., data = train, method = 'lm')
print(lm)
print(lm$finalModel)
lmPred = predict(lm, newdata = test)
postResample(lmPred, test$medv) # Measure accuracy in prediction


# Regression KNN (Everytime you use knn you MUST use preProcess)
knnFit = train(medv~., data = train, method = 'knn', preProcess = c("center", "scale"), tuneGrid = expand.grid(k = seq(1, 30, by = 5)))
knnFit
knnPred = predict(knnFit, test)
postResample(knnPred, test$medv)


# Regression Tree
regtree = train(medv~., data = train, method ="rpart", tuneGrid = expand.grid(cp = seq(0.1, 1, by = 0.1)))
regtree
regtreePred = predict(regtree, test)
postResample(regtreePred, test$medv)

btree = train(medv~., data = train, method = 'bstTree')
btree

btree_tune = train(medv~., data = train, method = 'bstTree', tuneGrid = expand.grid(maxdepth = c(1:3), mstop = seq(20, 100, by = 20), nu = 0.1))
btree_tune
btreePred = predict(btree_tune, test)
postResample(regtreePred, test$medv)

