# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class KeTang_login():
    hover = (By.XPATH, '//*[@title="分类"]')
    text = (By.XPATH, '//*[@title="分类"]')
    click_login = (By.XPATH, '//*[@id="js-mod-entry-index"]/a')
    click_qq_login = (By.XPATH, "//*[@class='icon-font i-qq']")
    login_frame = (By.XPATH, '//*[@name="login_frame_qq"]')
    username_login = (By.XPATH, '//*[@id="switcher_plogin"]')
