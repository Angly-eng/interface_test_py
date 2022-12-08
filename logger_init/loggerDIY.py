# -*- coding = utf-8 -*-
import logging

def logger1():
    # 构建日志器
    logger = logging.getLogger()
    # 设置日志器级别
    logger.setLevel('DEBUG')
    # 构建处理器（输出到控制台）
    handdler = logging.StreamHandler()
    # 构建格式器
    fmt1 = '%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
    formatter = logging.Formatter(fmt=fmt1)

    # 组装日志器
    handdler.setFormatter(formatter)
    logger.addHandler(handdler)
    return logger

if __name__ == '__main__':

    def func():
        my_logger = logger1()
        my_logger.info("Info信息")


    func()