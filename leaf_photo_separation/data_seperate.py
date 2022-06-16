import math
import shutil # 파일 복사할 때 쓸 수 있는 모듈.

from leaf_photo_separation.making_folder import *

for cls in classes_list:
    path = os.path.join(original_dataset_dir, cls)
    fnames = os.listdir(path) # list로 안에 있는 이미지파일 '이름'들이 리스트로 나옴.

    train_size = math.floor(len(fnames) * 0.6) # fnames는 list로 나오므로 전체 리스트 길이의 60% 값이 train_size가 됨.
    validation_size = math.floor(len(fnames) * 0.2) # fnames는 list로 나오므로 전체 리스트 길이의 20% 값이 validation_size가 됨.
    test_size = math.floor(len(fnames) * 0.2)

    ############################################################
    train_fnames = fnames[:train_size] # train_size까지 리스트 슬라이싱
    print("Train size(", cls, "): ", len(train_fnames))

    for fname in train_fnames:
        src = os.path.join(path, fname)
        dst = os.path.join(os.path.join(train_dir, cls), fname)
        shutil.copyfile(src, dst) # 여기서 파일 복사가 이뤄진다.

    ############################################################
    validation_fnames = fnames[train_size:(validation_size + train_size)] # train_size부터 20% 슬라이싱
    print("Validation size(", cls, "): ", len(validation_fnames))
    for fname in validation_fnames:
        src = os.path.join(path, fname)
        dst = os.path.join(os.path.join(validation_dir, cls), fname)
        shutil.copyfile(src, dst) # 여기서 파일 복사가 이뤄진다.

    ############################################################
    test_fnames = fnames[(train_size + validation_size):(validation_size + train_size + test_size)] # 맨 마지막 20% 슬라이싱

    print("Test size(", cls, "): ", len(test_fnames))
    for fname in test_fnames:
        src = os.path.join(path, fname)
        dst = os.path.join(os.path.join(test_dir, cls), fname)
        shutil.copyfile(src, dst) # 여기서 파일 복사가 이뤄진다.

    '''
Train size( Apple___Apple_scab ):  378
Validation size( Apple___Apple_scab ):  126
Test size( Apple___Apple_scab ):  126
Train size( Apple___Black_rot ):  372
Validation size( Apple___Black_rot ):  124
Test size( Apple___Black_rot ):  124
Train size( Apple___Cedar_apple_rust ):  165
Validation size( Apple___Cedar_apple_rust ):  55
Test size( Apple___Cedar_apple_rust ):  55
Train size( Apple___healthy ):  987
Validation size( Apple___healthy ):  329
Test size( Apple___healthy ):  329
Train size( Cherry___healthy ):  512
Validation size( Cherry___healthy ):  170
Test size( Cherry___healthy ):  170
Train size( Cherry___Powdery_mildew ):  631
Validation size( Cherry___Powdery_mildew ):  210
Test size( Cherry___Powdery_mildew ):  210
Train size( Corn___Cercospora_leaf_spot Gray_leaf_spot ):  307
Validation size( Corn___Cercospora_leaf_spot Gray_leaf_spot ):  102
Test size( Corn___Cercospora_leaf_spot Gray_leaf_spot ):  102
Train size( Corn___Common_rust ):  715
Validation size( Corn___Common_rust ):  238
Test size( Corn___Common_rust ):  238
Train size( Corn___healthy ):  697
Validation size( Corn___healthy ):  232
Test size( Corn___healthy ):  232
Train size( Corn___Northern_Leaf_Blight ):  591
Validation size( Corn___Northern_Leaf_Blight ):  197
Test size( Corn___Northern_Leaf_Blight ):  197
Train size( Grape___Black_rot ):  708
Validation size( Grape___Black_rot ):  236
Test size( Grape___Black_rot ):  236
Train size( Grape___Esca_(Black_Measles) ):  829
Validation size( Grape___Esca_(Black_Measles) ):  276
Test size( Grape___Esca_(Black_Measles) ):  276
Train size( Grape___healthy ):  253
Validation size( Grape___healthy ):  84
Test size( Grape___healthy ):  84
Train size( Grape___Leaf_blight_(Isariopsis_Leaf_Spot) ):  645
Validation size( Grape___Leaf_blight_(Isariopsis_Leaf_Spot) ):  215
Test size( Grape___Leaf_blight_(Isariopsis_Leaf_Spot) ):  215
Train size( Peach___Bacterial_spot ):  1378
Validation size( Peach___Bacterial_spot ):  459
Test size( Peach___Bacterial_spot ):  459
Train size( Peach___healthy ):  216
Validation size( Peach___healthy ):  72
Test size( Peach___healthy ):  72
Train size( Pepper,_bell___Bacterial_spot ):  598
Validation size( Pepper,_bell___Bacterial_spot ):  199
Test size( Pepper,_bell___Bacterial_spot ):  199
Train size( Pepper,_bell___healthy ):  886
Validation size( Pepper,_bell___healthy ):  295
Test size( Pepper,_bell___healthy ):  295
Train size( Potato___Early_blight ):  600
Validation size( Potato___Early_blight ):  200
Test size( Potato___Early_blight ):  200
Train size( Potato___healthy ):  91
Validation size( Potato___healthy ):  30
Test size( Potato___healthy ):  30
Train size( Potato___Late_blight ):  600
뭐 이런 출력 결과가 나온다.
    '''

print("END")