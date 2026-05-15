# 📋 Адреса и доступы — Academic Vault

## Инфраструктура на российском сервере (213.171.9.30)

### HedgeDoc — Совместное редактирование
- **URL:** http://213.171.9.30:3006
- **Назначение:** Real-time совместное редактирование markdown через браузер
- **Доступ:** Открытый (без регистрации)
- **Особенности:**
  - Работает в любом браузере
  - Не требует установки
  - Идеально для быстрой правки с редактором
  - Файлы можно экспортировать в markdown и перенести в Obsidian

### Git Bare Repository — Backup
- **SSH:** `ssh://root@213.171.9.30/srv/git/academic-vault.git`
- **Назначение:** Дополнительный backup помимо GitHub
- **Доступ:** SSH ключ `id_openclaw`

---

## GitHub (основной репозиторий)

- **URL:** https://github.com/MediaCod22/academic-vault
- **Назначение:** Основное хранилище, версионирование, совместная работа
- **Доступ:** *см. credentials.env*

---

## Рекомендуемый workflow

### Сценарий 1: Работа через Obsidian (основной)

```bash
# 1. Клонируй репозиторий
git clone https://github.com/MediaCod22/academic-vault.git ~/ObsidianVault

# 2. Открой в Obsidian
# File → Open folder as vault

# 3. Настрой Git hook (автопуш)
cd ~/ObsidianVault
git config core.hooksPath .githooks

# 4. Пиши статьи в 02-articles/01-drafts/
# Все изменения автоматически отправляются на GitHub
```

### Сценарий 2: Быстрая правка через HedgeDoc (с редактором)

1. Открой http://213.171.9.30:3006 в браузере
2. Создай новую заметку или открой существующую
3. Редактор вносит правки в реальном времени
4. Экспортируй результат в markdown
5. Скопируй в Obsidian vault → git push

### Сценарий 3: Редактор через Git (продвинутый)

```bash
# Редактор:
git clone https://github.com/MediaCod22/academic-vault.git
cd academic-vault
# Правит файлы в 02-articles/02-review/
git add -A
git commit -m "ревью: правки"
git push origin main

# Автор:
cd ~/ObsidianVault
git pull
# Видит правки в Obsidian
```

---

## Таблица доступов

| Сервис | Адрес | Логин | Пароль/Ключ | Назначение |
|--------|-------|-------|-------------|------------|
| **HedgeDoc** | http://213.171.9.30:3006 | — | Открытый | Быстрое редактирование |
| **GitHub** | https://github.com/MediaCod22/academic-vault | MediaCod22 | *см. credentials.env* | Основной Git |
| **Git (SSH)** | ssh://root@213.171.9.30/srv/git/academic-vault.git | root | SSH ключ `id_openclaw` | Backup |
| **Российский сервер** | 213.171.9.30 | root | SSH ключ id_openclaw | Инфраструктура |

---

## Быстрые команды

```bash
# Проверить HedgeDoc
curl -s http://213.171.9.30:3006 | head -5

# Проверить Git bare repo
ssh root@213.171.9.30 "ls /srv/git/academic-vault.git"

# Push на оба remote
git push origin main  # GitHub
git push server main  # Российский сервер
```

---

*Последнее обновление: 2026-05-15*
