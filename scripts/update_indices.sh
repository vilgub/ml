# Обновление индексов на новое поколение
ssh root@37.27.3.31 "cp /root/final/dgs/dg_2/ indices/ -r"
ssh root@65.109.234.79 "cp /root/final/dgs/dg_2/ indices/ -r"

# rolling update сервиса индекса кластера
ssh root@37.27.3.31 "docker service update --force --update-parallelism 1 --update-delay 30s qa_index_service_0"
ssh root@37.27.3.31 "docker service update --force --update-parallelism 1 --update-delay 30s qa_index_service_1"
ssh root@37.27.3.31 "docker service update --force --update-parallelism 1 --update-delay 30s qa_index_service_2"
ssh root@37.27.3.31 "docker service update --force --update-parallelism 1 --update-delay 30s qa_index_service_3"

# rolling update сервиса gateway
ssh root@37.27.3.31 "docker service update --force --update-parallelism 1 --update-delay 30s qa_gateway"