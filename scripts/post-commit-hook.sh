#!/bin/bash
# post-commit hook: автоматический push после каждого коммита

# Цвета
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${YELLOW}🚀 Автопуш в GitHub...${NC}"

# Проверяем, есть ли remote
if ! git remote get-url origin &>/dev/null; then
    echo "❌ Remote 'origin' не настроен. Настрой:"
    echo "   git remote add origin https://github.com/USERNAME/academic-vault.git"
    exit 0
fi

# Push
git push origin $(git rev-parse --abbrev-ref HEAD) &>/dev/null

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Отправлено в GitHub${NC}"
else
    echo -e "${YELLOW}⚠️ Push не удался. Попробуй вручную: git push${NC}"
fi
