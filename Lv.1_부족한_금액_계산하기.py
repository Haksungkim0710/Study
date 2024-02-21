def solution(price, money, count):
    sum = 0

    #1부터 count까지 sum에 price와 횟수만큼 곱해준 값을 더한다
    for i in range(1, count+1):
        sum += price * i
    #money에서 sum을 빼준다
    money -= sum

    #money가 양수면 0을 출력, 음수면 abs로 절대값을 리턴
    if money > 0:
        return 0
    else:
        return abs(money)

print(solution(3,20,4))
