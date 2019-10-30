# -*- coding: utf-8 -*-
import yaml


class Yaml(object):
    """读写yaml文件类"""

    def read_yaml(self, path):
        """
        读取yaml配置文件
        :param path: 读取yaml文件路径
        :return:
        """
        with open(path, 'r', encoding="UTF-8") as yamlfile:
            cfg = yaml.load(yamlfile.read(), Loader=yaml.FullLoader)
            return cfg

    def write_yaml(self, path, data):
        """
        写入yaml文件
        :param path: 写入yaml文件路径
        :param data: 写入yaml文件的数据
        :return:
        """
        with open(path, "a") as yaml_write:
            yaml.dump(data, yaml_write)


if __name__ == '__main__':
    # print(Yaml().read_yaml(r'F:\PycharmProjects\classnote\config\data.yaml'))
    print(Yaml().read_yaml(r'F:\PycharmProjects\classnote\config\extract.yaml'))
    # Yaml().write_yaml(r'F:\PycharmProjects\classnote\config\extract.yaml', {"token": "aaab123-fsd-13134"})


