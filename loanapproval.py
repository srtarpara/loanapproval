from sklearn import tree

#[income, number_of_dependents, credit_score, length_of_employment(in months)]
training_data = [[54000, 0, 750, 36], [38400, 2, 680, 12], [72000, 1, 720, 48], [33600, 3, 650, 8], [90000, 0, 800, 60], 
                 [60000, 1, 700, 24], [48000, 2, 680, 18], [45600, 3, 600, 12], [96000, 0, 780, 72], [30000, 4, 640, 6], 
                 [78000, 1, 720, 36], [66000, 0, 740, 30], [36000, 3, 650, 15], [86400, 0, 810, 50], [50400, 2, 670, 20]]

#whether or not the entry in the training data yields an approval for the loan.
outcome = ["Approved", "Declined", "Approved", "Declined", "Approved", 
           "Approved", "Declined", "Declined", "Approved", "Declined", 
           "Approved", "Approved", "Declined", "Approved", "Declined"]

#Preparing the decision tree to be trained on the training data by calling the constructor and assigning it to the decision_tree variable.
decision_tree = tree.DecisionTreeClassifier()

#The .fit() method trains the decision tree by learning patterns from the corresponding training_data and resulting outcome of whether or not the individual got approved for the loan.
decision_tree = decision_tree.fit(training_data, outcome)

#Getting userinput so that this data can then be classified by the decisison tree as approved or declined.
ui_income = input("Enter yearly income: ")
ui_number_of_dependents = input("Enter the number of dependents: ")
ui_credit_score = input("Enter the credit score: ")
ui_length_of_employment = input("Enter the length of employmenet **IN MONTHS**: ")

user_input = [ui_income, ui_number_of_dependents, ui_credit_score, ui_length_of_employment]

#The .predict() method now uses the trained model to predict whether or not the inidivdual gets approved or declined for the loan based on learned patterns.
decision = decision_tree.predict([user_input])

#Prints out the decision of the trained model.
print (decision)