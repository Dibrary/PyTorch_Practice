from writted_alphabet_separation.cnn_module_code import *
from writted_alphabet_separation.mnist_data_get import test_loader

model.train()
i = 1
for epoch in range(epoch_num):
    for data, target in train_loader:
        data = data.to(device)
        target = target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if i % 1000 == 0:
            print('Train Step: {}\tLoss: {:.3f}'.format(i, loss.item()))
        i += 1

model.eval()
correct = 0
for data, target in test_loader:
#     data, target = Variable(data, volatile=True), Variable(target)
    data = data.to(device)
    target = target.to(device)
    output = model(data)
    prediction = output.data.max(1)[1]
    correct += prediction.eq(target.data).sum()

print('Test set: Accuracy: {:.2f}%'.format(100. * correct / len(test_loader.dataset)))
'''
Train Step: 1000	Loss: 0.298 이런 식으로 나오는데 CPU를 써버리면 굉장히 오래 걸린다.
Train Step: 2000	Loss: 0.395
Train Step: 3000	Loss: 0.069 <= 여기서 갑자기 좋아짐.
'''

print(correct)

print(prediction.eq(target.data))