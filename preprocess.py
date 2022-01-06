# import numpy as np
# arr=np.arange(10)
# arr2=np.arange(20).reshape(10,2)
# with open("test.npy","wb") as f:
#     np.save(f,arr2)
# with open("test.npy","rb") as f:
#     print(np.shape(np.load(f)),np.shape(arr2))
#
#
# exit()
import os
from tqdm import tqdm
import numpy as np

with open("allwashed.csv", "r") as fin:
    lines = fin.readlines()
    rows = len(lines)
    cols = len(lines[0].strip().split(","))
    print(rows, cols)
ls = []
with tqdm(total=rows, ascii=True) as pbar:
    for line in lines:
        ls.append(list(map(float, line.strip().split(","))))
        pbar.update(1)

ls = np.array(ls)
with open("unnorm.npy","wb") as fout:
    np.save(fout,ls)
ls = np.transpose(ls)

max_of_row = ls.max(axis=1)
min_of_row = ls.min(axis=1)
interval_of_row = max_of_row - min_of_row
ls = (ls - min_of_row[:, np.newaxis]) / interval_of_row[:, np.newaxis]

ls = np.transpose(ls)
with open("norm.npy", "wb") as fout:
    np.save(fout, ls)

with open("norm.npy","rb") as fin:
    print(np.shape(np.load(fin)))

# with open("20.11.01.csv","w") as fout:
#     with open("data/day_TS/2020-11-01.csv","r") as f:
#         for line in f.readlines():
#             words=line.strip().split(",")
#             print(len(words))
#             list=[]
#             for i in words[2:13]:
#                 list.append(i)
#             for i in words[17:22]:
#                 list.append(i)
#             for i in words[24-1:39-1]:
#                 list.append(i)
#             for i in words[40-1:56-1]:
#                 list.append(i)
#             for i in words[57-1:66-1]:
#                 list.append(i)
#             for i in words[69-1:81-1]:
#                 list.append(i)
#             for i in words[90-1:103-1]:
#                 list.append(i)
#             for i in words[105-1:]:
#                 list.append(i)
#             print(len(list))
#             print(",".join(list),file=fout)


# list.append(words[3:14])
# list.append(words[18:23])
# list.append(words[24:39])
# list.append(words[40:56])
# list.append(words[57:66])
# list.append(words[69:81])
# list.append(words[90:102])
# list.append(words[104:])

exit()
with open("allwashed.csv", "w") as fout:
    for filelist in os.walk(r"data/day_TS"):
        for filename in filelist[2]:
            with open(os.path.join("data", "day_TS", filename), "r") as fin:
                print(filename)
                for line in fin.readlines()[1:]:
                    words = line.strip().split(",")
                    list = []
                    for i in words[2:13]:
                        list.append(i)
                    for i in words[17:22]:
                        list.append(i)
                    for i in words[24 - 1:39 - 1]:
                        list.append(i)
                    for i in words[40 - 1:56 - 1]:
                        list.append(i)
                    for i in words[57 - 1:66 - 1]:
                        list.append(i)
                    for i in words[69 - 1:81 - 1]:
                        list.append(i)
                    for i in words[90 - 1:103 - 1]:
                        list.append(i)
                    for i in words[105 - 1:]:
                        list.append(i)
                    print(",".join(list), file=fout)
