import os

for nr in range(10, 200):
    if nr == 148:
        continue

    file_name = "random_files/file" + str(nr)
    rename_file = False
    with open(file_name, 'rb') as f:
        if f.read(2) == b"\xff\xd8":
            rename_file = True
    if rename_file:
        os.rename(file_name, file_name + ".jpeg")
    else:
        os.remove(file_name)

