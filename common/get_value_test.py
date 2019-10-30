# -*- coding: utf-8 -*-
from common.operation_yaml import Yaml

def get_json_value_by_key(in_json, target_key, results=[]):
    if isinstance(in_json, dict):   # 如果输入数据的格式为dict
        for key in in_json.keys():  # 循环获取key
            data = in_json[key]
            get_json_value_by_key(data, target_key, results=results)  # 回归当前对应的value

            if key == target_key:  # 如果当前key与目标key相同就将当前key的value添加到输出列表
                results.append(data)

    elif isinstance(in_json, list) or isinstance(in_json, tuple):  # 如果输入数据格式为list或者tuple
        for data in in_json:  # 循环当前列表
            get_json_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素

    return results

def pop_list(dic, key, results=[]):
    tmp_dict = {}                                                       # 定义一个空字典
    first_value = get_json_value_by_key(dic, key, results=results)      # 提取value的值赋予 first_value
    if len(first_value) >= 1:                                           # 如果赋值的value大于等于1
        target_value = first_value.pop()                                # 删除value值
        tmp_dict[key] = target_value                                    # 将提取的value与需要提取的key组成字典
        return tmp_dict
    else:
        raise ("错误")

if __name__ == "__main__":
    test_dic = {'a': '1', 'b': '2', 'c': {
        'd': [{'e': [{'f': [{'v': [{'g': '6'}, [{'g': '7'}, [{'g': 8}]]]}, 'm']}]}, 'h', {'g': [10, 12]}]}}
    dicts = {'1': 1, '2': 2, '3': 3, '4': {'5': 55, '6': 66, '7': 77}, '7': {'7': 777}}
    data_dic = {"code": 200, "data": {"companyId": 170824133484, "companyName": "\u8d35\u5dde\u516c\u53f8",
                                      "domIds": ["cs_new_admittance_car_dealer", "cs_new_no_admittance_car_dealer",
                                                 "cs_look_car_dealer_details", "cs_edit_car_dealer",
                                                 "cs_car_dealer_enable",
                                                 "cs_admittance_apply", "cs_edit_no_car_dealer",
                                                 "cs_customer_manage_add_customer",
                                                 "cs_customer_manage_customer_details",
                                                 "cs_customer_manage_edit_user_customer"], "geoId": 170824133550,
                                      "id": 170824133727, "loginName": "gz0130", "name": "\u4f55\u6587", "phone": "",
                                      "roleInfoList": [{"enname": "CustomerManager", "id": 170607000698,
                                                        "roleName": "\u5ba2\u6237\u7ecf\u7406", "roleType": "user"},
                                                       {"enname": "CommercialVehicle", "id": 190305539048,
                                                        "roleName": "\u5546\u7528\u8f66\u5bf9\u63a5\u5c97",
                                                        "roleType": "user"},
                                                       {"enname": "CustomerAttache", "id": 170607000716,
                                                        "roleName": "\u5ba2\u6237\u4e13\u5458", "roleType": "user"}],
                                      "roles": ["CUSTOMERMANAGER", "COMMERCIALVEHICLE", "CUSTOMERATTACHE"],
                                      "token": "3B6A7873F5E340BEBFB89CAB8A6F40E5"}, "msg": "OK", "status": "true"}
    ress = get_json_value_by_key(test_dic, 'g')
    print('get_json_value_by_key方法：',ress)
    res = pop_list(data_dic, 'id')
    res1 = pop_list(data_dic, 'name')
    print('pop_list方法：',res)
    print('pop_list方法：',res1)

    # Yaml().write_yaml(r'F:\PycharmProjects\classnote\config\extract.yaml', res1) # 将字典写入yaml文件中

