#Let's get started...

#setwd 
setwd("/Users/don/Documents/R/Anomaly//")

#getwd
getwd()








train_raw <- read.csv("Train_set.csv", header = TRUE) 

test_1 <- read.csv("Test_set_legit.csv", header = TRUE) 
test_2 <- read.csv("Test_set_with_other_deno.csv", header = TRUE)



#Convert each file.csv into a column-matrix
train_matrix <- cbind(train_raw)
test1_matrix <- cbind(test_1) 
test2_matrix <- cbind(test_2)  


#Covariances
train_cov <- cov(train_matrix)
test1_cov <- cov(test1_matrix)
test2_cov <- cov(test2_matrix)

#Inverse
train_inv <- cov(train_cov)
test1_inv <- cov(test1_cov)
test2_inv <- cov(test2_cov)


#For training set
D2_Train <- mahalanobis(train_matrix, colMeans(train_matrix), train_cov)  
D2_Test1 <- mahalanobis(test1_matrix, colMeans(train_matrix), train_cov) 
D2_Test2 <- mahalanobis(test2_matrix, colMeans(train_matrix), train_cov) 





plot(density(D2_Train, bw = 0.5),
     main="Squared Mahalanobis Distances (Training), Observations=96, Variables=79") ; rug(D2_Train)
plot(density(D2_Test1, bw = 0.5),
     main="Squared Mahalanobis Distances (Counterfeits), Observations=96, Variables=79") ; rug(D2_Test1)
plot(density(D2_Test2, bw = 0.5),
     main="Squared Mahalanobis Distances (Counterfeits vs Training), Observations=96, Variables=79") ; rug(D2_Test2)



################
#Q-Q Plots (Training)
D2_Train_Plot <- qqplot(qchisq(ppoints(100), df = 3), D2_Train,
                        main = expression("Q-Q plot of Mahalanobis" * ~D^2 *
                                            " vs. quantiles of" * ~ chi[3]^2))


D2_Train_cft_Plot <- qqplot(qchisq(ppoints(100), df = 3), D2_Test1,
                            main = expression("Q-Q plot of Mahalanobis" * ~D^2 *
                                                " vs. quantiles of" * ~ chi[3]^2))


D2_Train_cft_vs_legit_Plot <- qqplot(qchisq(ppoints(100), df = 3), D2_Test2,
                                     main = expression("Q-Q plot of Mahalanobis" * ~D^2 *
                                                         " vs. quantiles of" * ~ chi[3]^2))

abline(0,1,col='gray')  #I don't get why this is here...

#write D2's into csv.files for quick observations
write.table(D2_Train, file = "D2_Train.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
write.table(D2_Test1, file = "D2_Test1.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")
write.table(D2_Test2, file = "D2_Test2.csv",row.names=FALSE, na="",col.names=FALSE, sep=",")


