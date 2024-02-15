import matplotlib.pyplot as plt


def visualize_accuracy(accuracy):
    plt.bar(['Accuracy'], [accuracy])
    plt.title('Model Accuracy')
    plt.ylabel('Accuracy')
    plt.ylim(0, 1)
    plt.show()

#creating baar chaart to visualize the accuracy of the model.
#the value of y is between 0 and 1 ensure clarity in viualizing the acuracy chart.