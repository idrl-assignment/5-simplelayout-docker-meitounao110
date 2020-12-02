# simplelayout-docker

本次作业将采用 docker 构建开箱即用的 simplelayout。考察 Dockerfile 的编写，并将镜像推送到官方仓库 dockerhub。

## 要求

- 将 `3-simplelayout-package` 作业中完成的 `src` 目录、`setup.py` 复制到本次作业的目录下
- 相关依赖填写 `requirements.txt`
- 注册 [dockerhub](https://hub.docker.com/)，并将用户名填入 `username.py` 中
- 编写 `Dockerfile`
- 构建 docker 镜像
  - 若本机已经安装 `docker`，可以本地 build
  - 若没有安装，可以使用 [play with docker](https://labs.play-with-docker.com/)，相当于一个有网络支持的虚拟环境，把自己的代码 clone 下来，再 build
  - 镜像名称为 `dockerhub 用户名/simplelayout`
- 将镜像 push 到 dockerhub 上 （先 docker login）

## 参考

- [docker quick-start](https://docs.docker.com/get-started/)
- [dockerhub python](https://hub.docker.com/_/python), 特别是其中 `How to use this image` 部分


## 评分标准

本次作业会运行一系列的测试，但仅`测试 1`为得分点，其预测试请在 `Feedback` 中查看结果

1. 测试能否找到上传的镜像仓库（得分点）
2. 测试能否根据编写的 `Dockerfile` 正常构建镜像
3. 测试能否使用镜像创建容器，并执行 `simplelayout` 脚本生成图片



