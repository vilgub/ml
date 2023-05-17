# загрузка dgs файлов хранящие результаты кластеризации эмбеддингов на сервера
for host in root@37.27.3.31 root@65.109.234.79; do
    echo $host
    rsync -ravzP dgs $host:/root/hardml_mlops_final/dgs
done
