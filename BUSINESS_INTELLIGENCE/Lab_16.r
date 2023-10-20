library(mlbench)
library(caret)
install.packages('MLeval')
library(MLeval)

# Retrieve Data
data("PimaIndiansDiabetes")
data = PimaIndiansDiabetes

# We particularly want to predict the positive rather than the negatives
summary = summary(data$diabetes)
print(summary)
data$diabetes = relevel(data$diabetes, ref = "pos") #This function allows us to select the reference level


#Split data into train and test
index = createDataPartition(data$diabetes, p = 0.7, list = F)
train = data[index,]
test = data[-index,]


# TUNING
tree = train(diabetes~., data = train, method = "rpart", 
        tuneGrid = expand.grid(cp = seq(0.1, 1, by = 0.1)),
        trControl = trainControl(method = "cv", number = 10))

print(tree) #Accuracy coming from cross-validation

# If you are not happy with accuracy you can use AUC & ROC
tree_auc = train(diabetes~., data = train, method = "rpart",
        tuneGrid = expand.grid(cp = seq(0.1, 1, by = 0.1)),
        trControl = trainControl(method = "cv", number = 10,
        classProbs = TRUE, summaryFunction = twoClassSummary, 
        savePredictions = TRUE))
tree_auc

X = evalm(tree_auc,  gnames = "tree")


# Test Set Evaluation
pred_tree_class = predict(tree_auc, newdata = test) #Predict class
pred_tree_prob = predict(tree_auc, newdata = test, type = "prob") #Predict probability

# CONFUSION MATRIX
confusionMatrix(pred_tree_class, test$diabetes)

# ROC curves on test set
pred_tree_prob$obs = test$diabetes #Creating new variable called obs (observations)
X = evalm(pred_tree_prob)

#Lift Chart
lift = lift(test$diabetes~pred_tree_prob$pos)
ggplot(lift, values = 60) #If you want to predict 60%




# REGRESSION
data("BostonHousing")
data2 = BostonHousing

index = createDataPartition(data$medv, p = 0.7, list = F)
train2 = data2[index,]
test2 = data2[-index,]

knnFit = train(medv~., data = train2, method = "knn", preProcess = c("center", "scale"),
        tuneGrid = expand.grid(k = c(1:20)),
        trControl = trainControl(method = "cv", number = 10))
knnFit

btree = train(medv~., data = train2, method = "bstTree", tuneGrid = expand.grid(nu = 0.1, maxdepth = c(1:5), mstop = 50), # nolint
        trControl = trainControl(method = "cv", number = 10)) #Only adding train control # nolint
print(btree)

pred_knn = predict(knnFit, test2)
pred_btree = predict(btree, test2)

postResample(pred_knn, test2$medv)
postResample(pred_btree, test2$medv)

