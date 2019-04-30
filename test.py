# -*- coding: utf-8 -*-
#학생 리스트를 선업합니다
students = [
    { "name": "손현준", "korean": 87, "math": 98, "english": 88, "science": 95 },
    { "name": "손현준", "korean": 11, "math": 42, "english": 39, "science": 58 },
    { "name": "손현준", "korean": 45, "math": 85, "english": 29, "science": 15 },
    { "name": "손현준", "korean": 86, "math": 29, "english": 18, "science": 45 },
    { "name": "손현준", "korean": 94, "math": 92, "english": 62, "science": 65 },
    { "name": "손현준", "korean": 28, "math": 91, "english": 81, "science": 98 },
    { "name": "손현준", "korean": 94, "math": 75, "english": 26, "science": 92 }
]
# 학생을 한 명씩 반복합니다
print("이름", "총점", "평균", sep="\t");
for student in students:
    # 점수의 총합과 평균을 구합니다.
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4
    #출력합니다.
    print(student["name"], score_sum, score_average, sep="\t")
