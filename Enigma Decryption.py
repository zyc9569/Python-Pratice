#模仿震白花音制作一个破密小游戏
#version 0.0.1
#Wirttern by Snorar
print("正在截取德军情报片段")
print("恩尼格玛的沦陷")
print("游戏玩法：输入你的密码，根据提供的信息进行进一步的推理和猜测")
print("游戏目标：尽量在最短步数内破译出具体密码")
print("你可以输入你猜的密码，然后电脑会向你反馈你猜的密码和正确密码的相似度，即与正确密码相比有几个相同的数字和有几个数字在正确的位置")
print("现在你可以选择破解三位密码、四位密码或五位密码")

import random
number = ["0","1","2","3","4","5","6","7","8","9"] #用来检测输入内容是否为数字
time = 0 #用来记录破密次数

def is_valid_guess(guess):
    """检查输入是否有效的四位不重复数字密码"""
    if len(guess) != 4:
        return False, "请输入四位不重复数字的密码"
    
    for char in guess:
        if char not in number:
            return False, "请输入四位不重复数字的密码"
    
    if guess[0] == guess[1] or guess[0] == guess[2] or guess[0] == guess[3] or guess[1] == guess[2] or guess[1] == guess[3] or guess[2] == guess[3]:
        return False, "请输入四位不重复数字的密码"
    
    return True, ""

try:
    decision = input("请输入3、4或5选择你想破解的密码位数：")

    if decision == "3":
        print("开发中，敬请期待")

    elif decision == "4":
        
        rb = random.randint(1000,9999)
        num = str(rb)
        # 确保生成没有重复数字的密码
        while num[0] == num[1] or num[0] == num[2] or num[0] == num[3] or num[1] == num[2] or num[1] == num[3] or num[2] == num[3]:
            rb = random.randint(1000,9999)
            num = str(rb) 
        key = list(num)

        none = True

        while none:
            time = time + 1
            print("-------------------------------------------")
            print("你已经消耗" + str(time) +"次破密机会")
            
            try:
                guess = input("请输入你的四位不重复数字密码：")
            except KeyboardInterrupt:
                print("\n游戏已退出，感谢游玩！")
                break
            
            # 使用函数验证输入
            valid, error_msg = is_valid_guess(guess)
            if not valid:
                print(error_msg)
                continue  # 跳过后续逻辑，重新输入
            
            # 计算正确数字和正确位置的数量
            guess_list = list(guess)
            correct_position = 0
            correct_number = 0
            
            # 计算正确位置的数量
            for i in range(4):
                if guess_list[i] == key[i]:
                    correct_position += 1
            
            # 计算正确数字的数量（不考虑位置）
            for char in guess:
                if char in key:
                    correct_number += 1
            
            # 显示结果
            print(f"你猜的密码有{correct_number}个数字正确，其中有{correct_position}个数字位置正确")
            
            # 检查是否完全正确
            if correct_position == 4:
                print("恭喜你破译出了正确密码：" + num)
                print("你一共消耗了" + str(time) + "次破密机会")
                none = False
                            
    elif decision == "5":
        print("开发中，敬请期待")
    else:
        print("请输入3、4或5选择你想破解的密码位数")

except KeyboardInterrupt:
    print("\n游戏已退出，感谢游玩！")