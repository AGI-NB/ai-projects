action = input("请操控角色动作: ").lower().strip()  # 获取用户输入并转换为小写字母，去除首尾空格

match action:
    case "W"|"w":
        print("角色向上移动")
    case "S"|"s":
        print("角色向下移动")
    case "A"|"a":
        print("角色向左移动")
    case "D"|"d":
        print("角色向右移动")
    case "J"|"j":
        print("角色攻击")
    case " ":
        print("角色跳跃")
    case _:
        print("无效的输入")