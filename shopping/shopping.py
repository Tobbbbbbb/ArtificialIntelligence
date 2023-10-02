import csv
import sys
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open("shopping.csv") as sheet:
        reader = csv.reader(sheet)
        next(reader)
        evidence = []
        labels = []
        for row in reader:
            ev = []
            ev.append(int(row[0]))
            ev.append(float(row[1]))
            ev.append(int(row[2]))
            ev.append(float(row[3]))
            ev.append(int(row[4]))
            ev.append(float(row[5]))
            ev.append(float(row[6]))
            ev.append(float(row[7]))
            ev.append(float(row[8]))
            ev.append(float(row[9]))
            if(row[10]=="Jan"):
                ev.append(0)
            elif(row[10]=="Feb"):
                ev.append(1)
            elif(row[10]=="Mar"):
                ev.append(2)
            elif(row[10]=="Apr"):
                ev.append(3)
            elif(row[10]=="May"):
                ev.append(4)
            elif(row[10]=="June"):
                ev.append(5)
            elif(row[10]=="Jul"):
                ev.append(6)
            elif(row[10]=="Aug"):
                ev.append(7)
            elif(row[10]=="Sep"):
                ev.append(8)
            elif(row[10]=="Oct"):
                ev.append(9)
            elif(row[10]=="Nov"):
                ev.append(10)
            elif(row[10]=="Dec"):
                ev.append(11)
            ev.append(int(row[11]))
            ev.append(int(row[12]))
            ev.append(int(row[13]))
            ev.append(int(row[14]))
            if(row[15]=="Returning_Visitor"):
                ev.append(1)
            else:
                ev.append(0)
            if(row[16]=="TRUE"):
                ev.append(1)
            else:
                ev.append(0)
            evidence.append(ev)
            if(row[17]=="TRUE"):
                labels.append(1)
            else:
                labels.append(0)
    return evidence, labels
    #raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    #raise NotImplementedError
    arrEvidence = np.ndarray(shape=(1,17), dtype=object)
    for row in evidence:
        temp = np.array(row, dtype=object)
        arrEvidence = np.vstack((arrEvidence,temp))
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(arrEvidence[1:], labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    #raise NotImplementedError
    sens = 0
    sensDiv = 0
    spec = 0
    specDiv = 0

    for i in range(len(labels)):
        if(labels[i]==1):
            sensDiv+=1
            if(labels[i]==predictions[i]):
                sens+=1
        else:
            specDiv+=1
            if(labels[i]==predictions[i]):
                spec+=1
    return (sens/sensDiv, spec/specDiv)


if __name__ == "__main__":
    main()
