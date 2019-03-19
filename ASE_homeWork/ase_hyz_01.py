'''
作者：韩育珍
版本：第二周作业
功能：四则运算
'''

#四则运算
class Asmd:

    def __init__(self):
        #self.file = file
        pass

    def subtracting_asmd(self):
        subtracting = input("请选择四则运算：（add/sub/mul/div）") #给用户选择四则运算的权利
        sub1 = float(input('请输入参数1:'))
        sub2 = float(input('请输入参数2:'))
        if (subtracting == 'add'):
            answer = sub1 + sub2
        elif (subtracting == 'sub'):
            answer = sub1 - sub2
        elif (subtracting == 'mul'):
            answer = sub1 * sub2
        elif (subtracting == 'div'):
            if (sub2 == 0):
                print("被除数不能为0，请重新输入")
                #answer = self.subtracting_asmd()
            else:
                answer = float(sub1 / sub2)
        else:
            print('不支持此种四则运算输入格式')
           #answer = self.subtracting_asmd()
        return answer

#主函数
def main():
    is_operation = True
   #file = 'report.txt'
    asmd = Asmd()
    while(is_operation):
        answer = asmd.subtracting_asmd()
        print('答案是：',answer)
        yes_or_no = input('是否继续运算：（y/n）')
        if(yes_or_no == 'n'):
            is_operation = False

if __name__ == '__main__':
    main()