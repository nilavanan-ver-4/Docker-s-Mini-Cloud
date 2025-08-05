#!/bin/bash
# cd database && docker-compose -f postgres-compose.yml up -d
# docker-compose -f redis-compose.yml up -d
# docker-compose -f mongo-compose.yml up -d
# docker-compose -f cassandra-compose.yml up -d
# docker-compose -f neo4j-compose.yml up -d

# cd ../tools
# docker-compose -f portainer-compose.yml up -d
# docker-compose -f adminer-compose.yml up -d
# docker-compose -f pgadmin-compose.yml up -d



# #chmod +x start-all.sh
# ./start-all.sh


#!/bin/bash

echo "🚀 Starting all databases..."
cd database
for file in *-compose.yml; do
  docker-compose -f "$file" up -d
done
cd ..

echo "🚀 Starting all tools..."
cd tools
for file in *-compose.yml; do
  docker-compose -f "$file" up -d
done
cd ..

echo "✅ All services are up!"
# chmod +x start-all.sh
# ./start-all.sh