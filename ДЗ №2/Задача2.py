import random

size = int(input())
lst = [i for i in range(0, size)]
train_size = (size*80) // 100
test_size = size - train_size

control = set()
control.add(random.choice(lst))
control.add(random.choice(lst))

train = set()
while len(train) < train_size:
    train.add(random.choice(lst))

test = set()
for el in lst:
    if not(el in train):
        test.add(el)

print(train, test, control)