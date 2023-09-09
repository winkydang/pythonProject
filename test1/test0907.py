import re

str1 = "601577长沙银行长沙银行关于获得证券投资基金托管资格的公告"
str2 = r'^(.*(?=(.*(?=董监高|高级管理人员|高管|董事长|总经理|总裁|CEO|总监|董事|监事|法人|法定代表人|书记|行长|主任|领导|董秘|财务负责人|总工|非执行董事|非执董|负责人|责任人|官员).*(?=涉嫌|违法|违纪|非法获利|行贿|犯罪|受贿|贪污|患病|意外事故|监管关注|罢免|免职|开除党籍|问责|处罚|处分|双开|限制消费|被执行人|强制措施|撤职|逮捕|通缉|开除|))))'
str3 = r'^(.*(?=(.*(?=董监高|高级管理人员|高管|董事长|总经理|总裁|CEO|总监|董事|监事|法人|法定代表人|书记|行长|主任|领导|董秘|财务负责人|总工|非执行董事|非执董|负责人|责任人|官员).*(?=涉嫌|违法|违纪|非法获利|行贿|犯罪|受贿|贪污|患病|意外事故|监管关注|罢免|免职|开除党籍|问责|处罚|处分|双开|限制消费|被执行人|强制措施|撤职|逮捕|通缉|开除|))))'
match = re.search(str2, str1)
res_1 = re.findall(str2, str1)

if match:
    matched_rule = match.group()
    print(f"匹配到的规则是: {matched_rule}")
else:
    print("未找到匹配的规则")
