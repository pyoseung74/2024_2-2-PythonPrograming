# 4주차 파이썬프로그래밍 연습
# 리스트 실습
a = [1, "kim", 3]
print(type(a))

# 리스트 슬라이싱
print(a[0:2) # == 1 kim 3

# 리스트 함수
print(a.index("kim")) # = 1
print(a+b)

a=80
b=75
c =55
scores = []
scores = {"name":"홍길동", "kor":80, "eng":75, "math":55}

scores.append(score)
score["name"] = "춘향이"
score["kor"] = 50
score["eng"] = 85
score["math"] = 95
{"kor":50,"eng":85, "math":95}
scores.append(score)

avg = (scores["kor"]+scores["eng"]+scores["math"]) /(len(scores)-1)
print("홍길동 학생의 점수는 {avg} 입니다.")
