import numpy as np


class Dataloader:
    cols = 0
    rows = 0
    windows = 0
    all_window = []
    window_size = 0
    train_set = []
    test_set = []

    def __init__(self, file, window_size=1, train_set_size=0):
        self.window_size = window_size
        with open(file, "rb") as fin:
            all_data = np.load(fin)
        self.rows, self.cols = np.shape(all_data)
        self.windows = self.rows - self.window_size + 1
        for i in range(self.windows):
            self.all_window.append(all_data[i:i + window_size])
        self.all_window = np.array(self.all_window)
        np.random.shuffle(self.all_window)
        self.train_set = self.all_window[:train_set_size]
        self.test_set = self.all_window[train_set_size:]

    def load_train_set(self):
        return self.train_set

    def load_test_set(self):
        return self.test_set

    def load_all_data(self):
        return self.all_window


if __name__ == "__main__":
    dataloader = Dataloader("norm.npy", 5)
    print(dataloader.rows, dataloader.cols, dataloader.windows)
    print(np.shape(dataloader.all_window))
