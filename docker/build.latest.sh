#!/bin/bash

unset KUBECONFIG

cd ..
docker build -f docker/Dockerfile.latest -t hub.intra.mlamp.cn/mz-bia/chatgpt-on-wechat:v0.0.1 .

docker push hub.intra.mlamp.cn/mz-bia/chatgpt-on-wechat:v0.0.1

docker run -d --name chatgpt-on-wechat --restart unless-stopped -p 80:9891 hub.intra.mlamp.cn/mz-bia/chatgpt-on-wechat:v0.0.1


docker run -d --name chatgpt-on-wechat --restart unless-stopped -p 80:9891 -v /home/xjy/logs:/app/logs hub.intra.mlamp.cn/mz-bia/chatgpt-on-wechat:v0.0.1
