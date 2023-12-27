def finding_number(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j and array[i] == array[j]:
                count += 1

    return count//2

list=[1,2,5,4,5,5,7]

print(f"Given list={list}\nRepeated number's count={finding_number(list)}")