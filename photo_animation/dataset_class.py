from image_to_rgb import *

class ImageDataset(Dataset):
    def __init__(self, root, transforms_ = None, unaligned = False, mode='train'):
        self.transform = transforms.Compose(transforms_)
        self.unaligned = unaligned

        if mode == 'train':
            self.files_A = sorted(glob.glob(os.path.join(root,'trainA'+"/*.*")))
            self.files_B = sorted(glob.glob(os.path.join(root, 'trainB'+"/*.*")))
        else:
            self.files_A = sorted(glob.glob(os.path.join(root,'testA'+"/*.*")))
            self.files_B = sorted(glob.glob(os.path.join(root, 'testB'+"/*.*")))

    def __getitem__(self, index):
        image_A = Image.open(self.files_A[index % len(self.files_A)])

        if self.unaligned:
            image_B = Image.open(self.files_B[random.randint(0, len(self.files_B) - 1)])
        else:
            image_B = Image.open(self.files_B[index % len(self.files_B)])

        if image_A.mode != "RGB":
            image_A = to_rgb(image_A)
        if image_B.mode != "RGB":
            image_B = to_rgb(image_B)

        item_A = self.transform(image_A)
        item_B = self.transform(image_B)
        return {"A":item_A, "B":item_B}

    def __len__(self):
        return max(len(self.files_A), len(self.files_B))