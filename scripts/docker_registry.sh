# если уже запущен не надо
# создание регистра
docker run -d -p 5000:5000 --restart=always --name registry registry:2

# загрузка gateway
docker tag gateway 37.27.3.31:5000/gateway
docker push 37.27.3.31:5000/gateway

# загрузка index_service
docker tag index_service 37.27.3.31:5000/index_service
docker push 37.27.3.31:5000/index_service

# загрузка tf_random
docker tag tf_random 37.27.3.31:5000/tf_random
docker push 37.27.3.31:5000/tf_random