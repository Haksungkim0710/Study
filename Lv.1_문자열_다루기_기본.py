def solution(s):
    #문자열 s의 길이가 4 or 6 인지 확인
    if len(s) == 4 or len(s) == 6:
        #문자열 s가 '숫자'로만 이루어져있는지 확인
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False

print(solution('a234'))
print(solution('1234'))
