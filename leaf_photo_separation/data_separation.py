
import os
import shutil

original_dataset_dir = "./dataset" # 데이터 셋 폴더
classes_list = os.listdir(original_dataset_dir)

base_dir="./splitted"
# os.mkdir(base_dir) # 한 번 폴더 만든 후에 계속 만들려고 해서 주석 걸어놓음.

train_dir = os.path.join(base_dir, 'train')
# os.mkdir(train_dir)

validation_dir = os.path.join(base_dir, 'val')
# os.mkdir(validation_dir)

test_dir = os.path.join(base_dir, 'test')
# os.mkdir(test_dir)
#
# for clss in classes_list:
#     os.mkdir(os.path.join(train_dir, clss))
#     os.mkdir(os.path.join(validation_dir, clss))
#     os.mkdir(os.path.join(test_dir, clss))

for clss in classes_list:
    os.path.join(train_dir, clss)
    os.path.join(validation_dir, clss)
    os.path.join(test_dir, clss)

# 위에가 폴더 생성 코드





