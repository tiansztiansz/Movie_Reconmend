# 简单电影推荐系统
## 如何使用
1、进入到项目最外层文件夹，在终端中输入如下命令，创建一个虚拟环境
```
py -3 -m venv venv
```

2、输入如下命令，用于激活虚拟环境
```
venv\Scripts\activate
```

3、输入如下命令，用于安装所需依赖
```
pip install -r requirements.txt
```

4、运行本地服务器，输入如下命令，并按照提示打开对应网址
```
python flask_app.py
```

更多资料请参考 [Flask中文网](https://flask.net.cn/installation.html#id4)

## 在线预览
当然，你也可以在网页端直接预览你只需要在上方的 URL 的 `https://` 后面添加 `gitpod.io/#/`

例如：
```
https://github.com/nginx/nginx => https://gitpod.io/#/github.com/nginx/nginx
```

之后你只需要在前面的 “如何使用” 的步骤运行即可

## 问题
由于该算法没有保存模型，所以每次预测都要重新计算，导致程序运行时间长。并且在部署到公共端时，还会报错，错误如下：
```
Internal Server Error
The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application
```
