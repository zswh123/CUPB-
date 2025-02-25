import os
import sys
import json
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import logging

def setup_logging():
    log_path = os.path.join(os.path.dirname(sys.executable), "app.log") if getattr(sys, 'frozen', False) else "app.log"
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def get_config_path():
    """ 获取配置文件路径（EXE同目录） """
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, "config.json")


def load_config():
    """ 加载配置文件 """
    config_path = get_config_path()
    if not os.path.exists(config_path):
        print(f"该目录不存在配置文件: {config_path}")
        exit(1)
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)



def get_resource_path(relative_path):
    """ 获取资源文件绝对路径 """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def auto_login():
    config = load_config()
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    try:
        # 动态获取驱动路径
        edgedriver_relative = config["edgedriver_path"]
        edgedriver_path = get_resource_path(edgedriver_relative)
        if not os.path.exists(edgedriver_path):
            raise FileNotFoundError(f"Edge驱动未找到: {edgedriver_path}")

        service = Service(executable_path=edgedriver_path)
        driver = webdriver.Edge(service=service, options=options)
        driver.get(config["login_url"])
        time.sleep(2)

        driver.find_element(By.ID, "username").send_keys(config["username"])
        driver.find_element(By.ID, "password").send_keys(config["password"])
        driver.find_element(By.ID, "login").click()

        print("自动登录成功！")
        time.sleep(5)
        driver.quit()
    except Exception as e:
        print(f"[ERROR] 自动登录失败: {str(e)}")


if __name__ == "__main__":
    setup_logging()
    logging.info("程序启动")
    try:
        auto_login()
    except Exception as e:
        logging.error(f"致命错误: {str(e)}", exc_info=True)