#Author:Anliu
info = {
    "资源申购":{
        "亚马逊":{
            "执行主机":["127.0.0.1","127.0.0.2"],
            "主机名称":["DNS01","DNS02"],
            "主机类型":["VMware","KVM"]
        },
        "阿里云":{
            "执行主机": ["128.0.0.1","128.0.0.2"],
            "主机名称": ["NTP01","NTP02"],
            "主机类型": ["VMware","KVM"]
        },
        "腾讯云":{
            "执行主机": ["129.0.0.1","129.0.0.2"],
            "主机名称": ["zabbix","zabbix"],
            "主机类型": ["VMware","KVM"]
        }
    },
    "资产管理":{
        "主机管理":{
            "root":["192.168.1.1","192.168.1.2"],
            "user":["192.168.0.1","192.168.0.2"]
        },
        "DB管理":{
            "mysql":["192.168.2.1","192.168.2.2"],
            "SQL server":["192.168.3.1","192.168.3.2"]
        },
        "IDC管理":{
            "A区":["192.168.4.1","192.168.4.2"],
            "B区":["192.168.5.1","192.168.5.2"]
        }
    }
}
#print(info)
exit_flag = False
while not exit_flag:
    for i1 in info:
        print(i1)
    choice1 = input("b==back|q==quit>>>")
    if choice1 in info:
        while not exit_flag:
            for i2 in info[choice1]:
                print(i2)
            choice2 = input("b==back|q==quit>>>")
            if choice2 in info[choice1]:
                while not exit_flag:
                    for i3 in info[choice1][choice2]:
                        print(i3)
                    choice3 = input("b==back|q==quit>>>")
                    if choice3 in info[choice1][choice2]:
                        while not exit_flag:
                            for i4 in info [choice1][choice2][choice3]:
                                print(i4)
                            choice4 = input("b==back|q==quit>>>")
                            if choice4 == "b":
                                break
                            elif choice4 =="q":
                                exit_flag = True
                                #exit()
                    elif choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flag = True
                        #exit()
            elif choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = True
                #exit()
    elif choice1 == "q":
        exit_flag = True
        #exit()
