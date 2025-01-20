#!/bin/bash

unset KUBECONFIG

cd ..
docker build -f docker/Dockerfile.latest -t hub.intra.mlamp.cn/xiajinyang/chatgpt-on-wechat:v0.0.1 .

docker push hub.intra.mlamp.cn/xiajinyang/chatgpt-on-wechat:v0.0.1

###############################################

#创建数据卷
docker volume create --label project=chatgpt-on-wechat chatgpt-on-wechat-data

docker volume ls

###############################################
docker kill chatgpt-on-wechat

docker container rm chatgpt-on-wechat

docker pull hub.intra.mlamp.cn/xiajinyang/chatgpt-on-wechat:v0.0.1

docker run -d --name chatgpt-on-wechat --restart unless-stopped -p 80:8080 -v chatgpt-on-wechat-data:/app/logs hub.intra.mlamp.cn/xiajinyang/chatgpt-on-wechat:v0.0.1

docker exec -it chatgpt-on-wechat /bin/bash

