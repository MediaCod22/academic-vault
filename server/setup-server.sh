#!/bin/bash
# setup-server.sh — настройка серверной инфраструктуры

SERVER="root@213.171.9.30"
SSH_KEY="/root/.ssh/id_openclaw"

echo "=== Очистка Docker ==="
ssh -i $SSH_KEY -o StrictHostKeyChecking=no $SERVER "docker system prune -af --volumes"

echo "=== Создание Git bare repository ==="
ssh -i $SSH_KEY -o StrictHostKeyChecking=no $SERVER "mkdir -p /srv/git/academic-vault.git && cd /srv/git/academic-vault.git && git init --bare"

echo "=== Копирование Docker Compose ==="
scp -i $SSH_KEY -o StrictHostKeyChecking=no server/docker-compose.hedgedoc.yml $SERVER:/srv/hedgedoc/

echo "=== Запуск HedgeDoc ==="
ssh -i $SSH_KEY -o StrictHostKeyChecking=no $SERVER "cd /srv/hedgedoc && docker-compose up -d"

echo "=== Проверка статуса ==="
ssh -i $SSH_KEY -o StrictHostKeyChecking=no $SERVER "docker ps | grep hedgedoc"

echo "=== Готово ==="
echo "HedgeDoc: http://213.171.9.30:3006"
echo "Git: ssh://root@213.171.9.30/srv/git/academic-vault.git"