# coding=utf-8
#用例：abaabbabba>=1;abbabb=1;abbc;abbababb==1;
def idtf(str1):
    try:
        # str1=input("请输入一段字符串：")
        str_list=list(str1)
        # 去除空格
        while ' 'in str_list:
            str_list.remove(' ')
        str_list.reverse()
        # print(str_list)
        # 初始化
        state=0
        flag=1
        # 开始了
        while flag==1:
            while state==0:
                while str_list:
                    str_pop=str_list.pop()
                    if str_pop=='a':
                        state=0
                    elif str_pop=='b':
                        if str_list[-1]=='b':
                            state=2
                            break
                        else:
                            state=0
                    else:
                        # print("不通过")
                        flag=0
                        state=-1
                        break
            # while state==2:
            #     str_list.pop()
            #     while str_list:
            #         str_pop = str_list.pop()
            #         if str_pop == 'a':
            #             state = 2
            #         elif str_pop == 'b':
            #             if str_list[-1] == 'b':
            #                 state = 4
            #                 flag=0
            #                 break
            #             else:
            #                 state = 2
            #         else:
            #             # print("不通过")
            #             flag = 0
            #             state = -1
            #             break
            while state==2:
                str_list.pop()
                while str_list:
                    str_pop=str_list.pop()
                    if str_pop=='a':
                        state=0
                    elif str_pop=='b':
                        state=2
                    elif str_pop=='>'or str_pop=='<' or str_pop=='=' or str_pop=='!':
                        if str_list[-1]=='=':
                            state=6
                            break
                        elif str_list[-1]=='1' and (str_pop=='>'or str_pop=='<'or str_pop=='!'):
                            state=7
                            break
                        else:
                            # print("不通过")
                            flag = 0
                            state = -1
                            break
            while state==6:
                str_list.pop()
                if str_list[-1]=='1':
                    state=7
                else:
                    # print("不通过")
                    flag = 0
                    state = -1
                    break
            while state==7:
                str_list.pop()
                if len(str_list)==0:
                    flag=0
                    state=-2
                    break
                else:
                    # print("不通过")
                    flag = 0
                    state = -1
                    break
            while state==-1:
                # print("不通过")
                return "不合法"
                break
            while state==-2:
                return "合法"
                # print("合格")
                break
    except Exception:
        return "不合法"
        # print("不通过")
# print("state="+str(state))
str1=input("请输入：")
result_list=[]
input_list=str1.split(";")
if input_list[-1]=='':
    input_list.pop()
# 字符串列表
# print(input_list)
for il in input_list:
    result_list.append(idtf(il))
# 结果列表
# print(result_list)
for i in range(0,len(input_list)):
    print(input_list[i]+"    "+result_list[i])
