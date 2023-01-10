
# -*- coding: utf-8 -*-
# 2019/1/20
# 淘宝秒杀脚本，扫码登录版
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time


def login(browser):
    # 打开淘宝登录页，并进行扫码登录
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element("link text","亲，请登录"):#出错原因aslenium版本不同 help:https://blog.csdn.net/PatrickYuc/article/details/128430693
        browser.find_element("link text","亲，请登录").click();
        print("请在15秒内完成淘宝扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)

    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(browser, buy_time):
    while True:
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if cur_time > buy_time:
            # 全选购物车
            while True:
                try:
                    if browser.find_element(by=By.ID,value='J_SelectAll1'):#参考：https://blog.csdn.net/weixin_44761824/article/details/124451493?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167256361916800211568909%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=167256361916800211568909&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2-124451493-null-null.142^v68^control,201^v4^add_ask,213^v2^t3_esquery_v3&utm_term=selenium%E6%9B%B4%E6%96%B0&spm=1018.2226.3001.4187
                        browser.find_element(by=By.ID,value='J_SelectAll1').click()
                        print("已全选")
                        break
                except:
                    print("找不到全选按钮")
            # 结算和提交订单
            while True:
                try:  # 疯狂点击<结算>按钮
                    if browser.find_element(by=By.ID,value="J_Go"):
                        browser.find_element(by=By.ID,value="J_Go").click()
                        print("已结算")
                except:  # 界面跳转后，点击<提交订单>按钮
                    try:
                        if browser.find_element("link text",'提交订单'):
                            browser.find_element("link text",'提交订单').click()
                            now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                            print("抢购成功时间：%s" % now1)
                            browser.quit()
                            return 0
                    except:
                        print("再次尝试提交订单")

            time.sleep(0.001)  # 1ms循环

if __name__ == "__main__":
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    set_time = input(f"请输入抢购时间，格式如 {cur_time} :\n")
    # 时间格式："2018-09-06 11:20:00.000000"
    chrome_browser = webdriver.Chrome()  # path形参缺省为环境变量 / 打包为exe后缺省为exe当前目录
    chrome_browser.maximize_window()

    login(chrome_browser)
    buy(chrome_browser, set_time)