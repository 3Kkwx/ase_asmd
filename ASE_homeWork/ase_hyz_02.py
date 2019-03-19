'''
作者：韩育珍
版本：第三周作业
新增功能1：四则运算
新增功能2：由系统自动生成四则运算
'''
import random

#判断用户输入的答案是否正确
def true_or_false(answer,userAnswer):

    if (userAnswer == answer):
        print('回答正确')
    else:
        print('回答错误，正确答案是：{},还需要多加练习哦~'.format(answer))

#四则运算
def subtracting_asmd():

    # 给用户选择四则运算的权利
    subtracting = input("请选择四则运算：（add/sub/mul/div）")

    #定义两个变量名，userAnswer为用户输入的答案，answer为正确答案
    userAnswer = 0
    answer = 0

    #random随机产生四则运算的两个参数
    sub1 = random.randint(1, 100)  # 产生 1 到 10 的一个整数型随机数
    sub2 = random.randint(1, 100)

    #接收用户输入的答案，且系统计算正确答案
    if (subtracting == 'add'):
        userAnswer = int(input('{}+{}='.format(sub1, sub2)))
        answer = sub1 + sub2
        true_or_false(answer,userAnswer)
    elif (subtracting == 'sub'):
        userAnswer = int(input('{}-{}='.format(sub1, sub2)))
        answer = sub1 - sub2
        true_or_false(answer,userAnswer)
    elif (subtracting == 'mul'):
        userAnswer = int(input('{}*{}='.format(sub1, sub2)))
        answer = sub1 * sub2
        true_or_false(answer,userAnswer)
    elif (subtracting == 'div'):
        userAnswer = int(input('{}/{}='.format(sub1, sub2)))
        if (sub2 == 0):
            print("被除数不能为0，请重新输入")
            answer = subtracting_asmd()
        else:
            answer = float(sub1 / sub2)
        true_or_false(answer,userAnswer)
    else:
        print('不支持此种四则运算输入格式')
        answer = subtracting_asmd()

#主函数
def main():
    is_operation = True
    while(is_operation):
        subtracting_asmd()
        yes_or_no = input('是否继续运算：（y/n）')
        if(yes_or_no == 'n'or yes_or_no !='y'):
            is_operation = False

#主函数入口
if __name__ == '__main__':
    main()