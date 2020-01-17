def compare_hash():
    list1 = []
    list2 = ["098f6bcd4621d373cade4e832627b4f6", "598d4c200461b81522a3328565c25f7c", "c3add7b94781ee70ec7c817c79f7b7bd"]

    list1 = [line.rstrip('\n') for line in open("hashes.txt", 'r')]

    intersection = set(list1).intersection(list2)

    for line in intersection:
        print(line)

    with open('gevonden_hashes.txt', 'w') as file_out:
        for line in intersection:
            file_out.write(line + "\r\n")

compare_hash()
