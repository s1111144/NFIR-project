"""
lijst = ['598d4c200461b81522a3328565c25f7c', 'c3add7b94781ee70ec7c817c79f7b7bd' ']
with open('hashes.txt', 'r') as bestand1:
    for item in lijst:          #hashes.txt is dan de file met hashes
        same = set(bestand1).intersection(lijst)

same.discard('\n')

with open('gevonden_hashes.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

Lijst = ['598d4c200461b81522a3328565c25f7c', 'c3add7b94781ee70ec7c817c79f7b7bd', '098f6bcd4621d373cade4e832627b4f6']
List = open("hashes.txt")
# for item in List:
  #hashes.txt is dan de file met hashes
same = set(List).intersection(Lijst)

same.discard('\n')

with open('gevonden_hashes.txt', 'a') as file_out:
    for line in same:
        file_out.write(line)
"""

lijst = ['598d4c200461b81522a3328565c25f7c', 'c3add7b94781ee70ec7c817c79f7b7bd']
with open('hashes.txt', 'r') as List:
    for line in List:
        same = set(List).intersection(lijst)

same.discard('\n')

with open('gevonden_hashes.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
