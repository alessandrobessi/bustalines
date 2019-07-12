from bustalines import FileMap
from torch.utils.data import Dataset


class FMDataset(Dataset):

    def __init__(self, filename: str):
        self.fm = FileMap(filename)

    def __len__(self) -> int:
        return len(self.fm)

    def __getitem__(self, item: int) -> str:
        return self.fm[item]


if __name__ == '__main__':
    fmdataset = FMDataset('.gitignore')
    print(len(fmdataset))
    print(fmdataset[0])
