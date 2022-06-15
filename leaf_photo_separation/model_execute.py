from data_loader import *
from model import *
from model_evaluate import *
from model_train import *
from multiprocessing import freeze_support

import time, copy

def train_baseline(model, train_loader, val_loader,
                   optimizer, num_epochs = 30):

    best_acc = 0.0
    best_model_wts = copy.deepcopy(model.state_dict())

    for epoch in range(1, num_epochs + 1):
        since = time.time()
        train(model, train_loader, optimizer)
        train_loss, train_acc = evaluate(model, train_loader)
        val_loss, val_acc = evaluate(model, val_loader)

        if val_acc > best_acc:
            best_acc = val_acc
            best_model_wts = copy.deepcopy(model.state_dict())

        time_elapsed = time.time() - since
        print(f"================== epoch {epoch}==================")
        print("train Loss: {:.4f}, Accuracy: {:.2f}%".format(train_loss, train_acc))
        print("val Loss: {:.4f}, Accuracy: {:.2f}%".format(val_loss, val_acc))
        print("Completed in {:.0f}m {:.0f}s".format(time_elapsed // 60, time_elapsed % 60))
    model.load_state_dict(best_model_wts)
    return model

if __name__=="__main__":
    freeze_support()
    base = train_baseline(model_base, train_loader, val_loader, optimizer, EPOCH)






