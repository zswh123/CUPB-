import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options


# 配置参数
login_url = "http://login.cup.edu.cn/"  # 登录页面URL
username = "123456" # 学号
password = "456789"# 密码
edgedriver_path = "edge_driver/msedgedriver.exe"  # 替换为你的EdgeDriver路径


# 自动登录函数
def auto_login():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    try:
        # 初始化浏览器驱动（适配Selenium 4.x）
        service = Service(executable_path=edgedriver_path)
        driver = webdriver.Edge(service=service)

        driver.get(login_url)
        time.sleep(2)

        # 填写账号密码（根据页面实际元素ID调整）
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login").click()

        print("自动登录成功！")
        time.sleep(5)
        driver.quit()
    except Exception as e:
        print(f"[ERROR] 自动登录失败: {str(e)}")


if __name__ == "__main__":
    auto_login()
