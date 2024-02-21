def solution(arr1, arr2):

    # len(arr1) 만큼 반복하여 행의 개수 구하기
    for i in range(len(arr1)):
        # len(arr1[i]만큼 반복하여 열의 개수 구하기
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]

    return arr1

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))
