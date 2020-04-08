#Author:Anliu
student1 = ['数计学院',['计科','网络','数学'],[1701,1702]]
student2 = ['电信学院',['电气','电科','物理'],[1702,1702]]
print(1,student1[0])
print(2,student2[0])
college = input('请选择您所在的学院:')
college = int(college)
if college == 1:
    print(1,student1[1][0])
    print(2,student1[1][1])
    print(3,student1[1][2])
    speciality = input('请选择您的专业：')
    speciality = int(speciality)
    if speciality < 4:
        print(1,student1[2][0])
        print(2,student1[2][1])
        class1 = input('请选择您的班级：')
        class1 = int(class1)
        if class1 == 1:
            print('您在',student1[0],student1[1][speciality-1],student1[2][0],'班')
        elif class1 == 2:
            print('您在', student1[0], student1[1][speciality-1], student1[2][1], '班')
        else:
            print('输入错误，退出！')
    else:
        print('输入错误，退出！')
elif college == 2:
    print(1,student2[1][0])
    print(2,student2[1][1])
    print(3,student2[1][2])
    speciality = input('请选择您的专业：')
    speciality = int(speciality)
    if speciality < 4:
        print(1,student2[2][0])
        print(2,student2[2][1])
        class1 = input('请选择您的班级：')
        class1 = int(class1)
        if class1 == 1:
            print('您在',student2[0],student2[1][speciality-1],student2[2][0],'班')
        elif class1 == 2:
            print('您在', student2[0], student2[1][speciality-1], student2[2][1], '班')
        else:
            print('输入错误，退出！')
    else:
        print('输入错误，退出！')
else:
    print('输入错误，退出！')
