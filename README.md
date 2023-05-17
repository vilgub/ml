# Deploy

сгенерил ssh на машинах, добавил в github
git clone git@github.com:vilgub/ml.git
cd scripts
chmod +x build_all.sh 
./build_all.sh
chmod +x ./docker_registry.sh
./docker_registry.sh - залив докер образов в registry
cd ..
docker swarm init на первом
docker swarm join --token на втором
