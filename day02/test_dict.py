#Author:Anliu
#info = {"linux":["quanquan","runrun","yaobin","tianhao"],"java":"xiudu"}
#info["java"] = "lisi"
#print(info)
#info.pop("java")
#info.clear()
#print(info.keys())
#print(info.get("linux"))
#print(info.values())
#print(info.items())
#print(info)

info = {
    "linxu_base":{
        "安全管理":{
            "firewall":["start","stop","restart",],
            "selinux": ["start","stop","restart",]
        },
        "用户管理":{
            "root": ["start","stop","restart",],
            "user": ["start","stop","restart",]
        },

    },
    "linxu_auto": {
        "部署": {
            "ansible": ["start", "stop", "restart", ],
            "jenkin": ["start", "stop", "restart", ]
        },
        "监控": {
            "zabbix": ["start", "stop", "restart", ],
            "pinpoint": ["start", "stop", "restart", ]
        },
    }
}

