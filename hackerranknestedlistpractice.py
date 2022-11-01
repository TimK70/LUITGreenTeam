if __name__ == '__main__':
    students =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda col: (col[1], col[0]))
    lowest = second_lowest = students[0][1]
    value_update = 0
    i = 0
    size = len(students)
    
    while i < size:
        if students[i][1] > second_lowest:
            second_lowest = students[i][1]
            value_update += 1
        if value_update == 1:
            print(students[i][0])
        if lowest != second_lowest and value_update > 1:
            break
        i +=1 