# 校园网自动登录脚本

🔌 基于Selenium实现的校园网无界面自动登录工具

因为我不知道为什么每次都连不上学校的校园网，一怒之下~~怒了一下~~，写了这个脚本

~~虽然基本上是Deepseek帮我写的🤣~~。挺简单的，就是使用Selenium模拟人操作浏览器去登录。

**目前只支持Windows~~**因为我感觉也不会有人看这个页面😭~~

## 快速开始

我已经将项目打包成了一个exe程序，把**dist文件夹**下载下来，在里面的config.json文件中修改参数，然后双击main.exe就可以运行了

### 前置要求

- Python 3.7+
- Microsoft Edge浏览器（在edge_driver文件夹里面有一个，版本不对可以自己替换一下）
- Edge浏览器驱动 [下载地址](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

### 安装依赖

```bash
pip install selenium==4.*
```

### 参数设置

里面有三个参数：

* username：用户名（我们学校就是学号）
* password：密码
* login_url：学校的登录网站，我们学校是[http://login.cup.edu.cn/](https://)
* edgedriver_path**不要管他**

设置完参数然后运行main.exe文件就可以启动程序了

## 开机自启

设置了开机自启就可以自动登录了。
网上有很多教程这里贴一个[http://blog.csdn.net/qq_41699621/article/details/110630446](https://)

我自己用的是**创建自启动**的方法：

1. 首先给main.exe文件夹创建一个快捷方式
2. 然后按下Win+R键
3. 输入shell:startup打开启动文件夹
4. 把刚刚创建的main.exe的快捷方式放进去就行了

---

# 叠甲

我是个地质类专业的学生，py都是自己学的玩的😭，期待大佬修改指正
