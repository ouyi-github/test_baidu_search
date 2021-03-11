import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.feature('百度搜索模块测试')
class TestBaiduSearch:
    def get_dir(self):
        """
        获取当前项目地址
        :return:
        """
        now_dir = os.getcwd()
        while True:
            now_dir = os.path.split(now_dir)
            if now_dir[1] == 'test_baidu_search':
                now_dir = os.path.join(now_dir[0], 'test_baidu_search')
                break
            now_dir = now_dir[0]
        return now_dir

    def setup(self):
        """前置动作"""
        # driver_path = os.path.join(self.get_dir(),'plugin/windows/chromedriver.exe') # Windows下使用
        driver_path = os.path.join(self.get_dir(), 'plugin/linux/chromedriver') # linux下使用
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        """后置动作"""
        self.driver.quit()


    @allure.story('百度搜索测试用例')
    @pytest.mark.parametrize("name", [("华为"), ("腾讯"), ("阿里"), ("百度"), ("字节"), ("平安"), ("python"), ("java"), ("c语言"),
                                      ("shell"), ("docker"), ("selenium"), ("pytest"), ("django"), ("flask"), ("四川"),
                                      ("成都"),
                                      ("老虎"), ("猴子"), ("狮子"), ("狗"), ("猫"), ("欧毅")])
    def test_baidu_search(self, name):
        self.driver.get("https://www.baidu.com/")
        time.sleep(5)
        self.driver.find_element(By.ID, "kw").send_keys(f"{name}")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(5)
        r = self.driver.title
        assert r == f"{name}_百度搜索"
