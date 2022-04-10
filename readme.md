### 背景

在构建家庭影院时，一个一个去找电影链接，再拷贝到下载器中下载，实在太麻烦了
这个项目就是将IMDB top 250 电影的全部磁力链接整合，一次整合，一次导入即可下载

![exp](https://raw.githubusercontent.com/L0yy/MagnetLinkGet/main/resource/1.png)

### 如何二次开发

1. 将你要下载电影名保存在`MovicesList.txt`中
2. `pip install tpblite`
3. `python run.py`
4. 将输出`MovicesMagnetlinkList.txt`，将这个文件拿去用下载器读取下载即可

