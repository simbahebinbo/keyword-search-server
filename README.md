查询输入字符串中的敏感词和过滤词。

使用jieba分词、haystack搜索引擎实现。

该程序可以定时更新词库索引。


操作系统: 

ubuntu 16.04

python版本: 3.5

安装相应的包

sudo ./apt-get.sh

创建虚拟环境

virtualenv --python=python3 env3

安装依赖包

source env3/bin/activate

pip3 install -r requirements.txt


创建数据库

python3 manage.py migrate


创建管理员用户

python3 manage.py createsuperuser


启动celery work

./run_develop_worker.sh

启动定时任务

./run_develop_beat.sh

启动服务

./run_develop.sh

使用方式：

method: GET

url: http://localhost:8000/api/search/?text=需要查找的字符串

后台管理：

http://localhost:8000/admin/

1、添加关键词的分类

2、添加关键词，分为敏感词、过滤词


参考资料：

http://celery-haystack.readthedocs.io/en/latest/

http://django-haystack.readthedocs.io/en/latest/toc.html

http://whoosh.readthedocs.io/en/latest/index.html

http://www.weiguda.com/blog/73/
