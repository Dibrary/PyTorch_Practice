
import os

# dataset 폴더에 미리 데이터를 넣어놓고 실행하면 splitted 폴더 생기면서 옮겨짐.
original_dataset_dir = "./dataset/dataset" # 데이터 셋 폴더
classes_list = os.listdir(original_dataset_dir)

base_dir="./splitted"
os.mkdir(base_dir) # 한 번 폴더 만든 후에 계속 만들려고 해서 주석 걸어놓음.

train_dir = os.path.join(base_dir, 'train')
os.mkdir(train_dir) # train 폴더 만들기

validation_dir = os.path.join(base_dir, 'val')
os.mkdir(validation_dir) # val 폴더 만들기

test_dir = os.path.join(base_dir, 'test')
os.mkdir(test_dir) # test 폴더 만들기



for clss in classes_list: # ./dataset/dataset 안에 있는 폴더 전부 하나씩 나온다.
    os.mkdir(os.path.join(train_dir, clss))
    os.mkdir(os.path.join(validation_dir, clss))
    os.mkdir(os.path.join(test_dir, clss)) # 각 폴더마다 똑같이 만든다.

for clss in classes_list:
    print(os.path.join(train_dir, clss)) # 폴더 내부가 제대로 생성되었는지 확인.
    print(os.path.join(validation_dir, clss))
    print(os.path.join(test_dir, clss))

# 위에가 폴더 생성 코드
# 이 코드만 실행하면 폴더만 만들어진다.
# 데이터도 같이 옮기려면 data_check 파일을 실행해야 한다.




