from matplotlib import pyplot as plt

def plot_acc_loss(train_acc_history, test_acc_history, train_loss_history, test_loss_history):
  fig, axs = plt.subplots(2,2,figsize=(15,10))
  fig.suptitle("Training & Validation")

  axs[0, 0].plot(train_acc_history)
  axs[0, 0].set_title("Training Accuracy")

  axs[0, 1].plot(train_loss_history)
  axs[0, 1].set_title("Training Loss")

  axs[1, 0].plot(test_acc_history)
  axs[1, 0].set_title("Validation Accuracy")

  axs[1, 1].plot(test_loss_history)
  axs[1, 1].set_title("Validation Loss")

def plot_accuracy(train_history, val_history):
  _= plt.plot(train_history)
  _= plt.plot(val_history)
  _= plt.title('Model Accuracy')
  _= plt.ylabel('Accuracy')
  _= plt.xlabel('Epoch')
  _= plt.legend(['train', 'val'], loc='upper left')
  _= plt.show()

def plot_loss(train_history, val_history):
  _= plt.plot(train_history)
  _= plt.plot(val_history)
  _= plt.title('Model Loss')
  _= plt.ylabel('Loss')
  _= plt.xlabel('Epoch')
  _= plt.legend(['train', 'val'], loc='upper left')
  _= plt.show()
