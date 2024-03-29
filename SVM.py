# Note: This is just a basic SVM(Support Vector Machine) classifier done for my practice.
# Let's import the dependencies
# Dependencies:
	# sklearn
	# required datasets from sklearn package
print("<-----------Support Vecor Machine Classifier----------->")
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import datasets

# Load the dataset, here I'm going to use the iris dataset

iris = datasets.load_iris()
# Let's see the shape of our data
print("Data Shape: ", iris.data.shape)
print("Target Shape: ", iris.target.shape)
# split the dataset in order to validate our classifier's performance
print()
print("<------------------------------------------------------>\n")

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)

# Here I'm using 40% of the data for testing purpose

print("Training Data Shape: ", x_train.shape) #training data
print("Testing Shape: ", x_test.shape) #testing data
print()
print("<------------------------------------------------------>\n")
# Here comes the classifier, we use the fit() to fit the data into our classifier

clf = SVC(kernel='linear').fit(x_train, y_train)

print("Score: ", clf.score(x_test, y_test)) 

# Thanks for having a look!
