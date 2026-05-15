# 📚 Academic Vault

Шаблон Obsidian vault для научного письма с Zotero интеграцией и Git backup.

## Быстрый старт

```bash
# 1. Склонируй репозиторий
git clone https://github.com/voodoo2serg/academic-vault.git ~/ObsidianVault

# 2. Открой в Obsidian
# File → Open folder as vault → выбери ~/ObsidianVault

# 3. Настрой Git (один раз)
cd ~/ObsidianVault
git config user.name "Твое Имя"
git config user.email "email@example.com"

# 4. Экспортируй источники из Zotero
python3 scripts/zotero-export.py

# 5. Начни писать!
# Всё автосохраняется и автопушится в Git
```

## Структура vault

```
academic-vault/
├── 00-inbox/              # Идеи, заметки, наброски (без структуры)
├── 01-sources/            # Источники из Zotero (автогенерация)
│   └── source-{key}.md
├── 02-articles/
│   ├── 01-drafts/         # Черновики статей
│   ├── 02-review/         # На проверке у редактора
│   └── 03-published/      # Опубликованные / готовые
├── 03-projects/           # Проектные заметки (диссертация, гранты)
├── 99-templates/          # Шаблоны для Obsidian
└── scripts/               # Скрипты автоматизации
```

## Для редактора

```bash
# 1. Склонируй репозиторий
git clone https://github.com/voodoo2serg/academic-vault.git

# 2. Сделай правки в файлах .md (любой редактор: VS Code, Obsidian, vim)

# 3. Отправь изменения
git add -A
git commit -m "ревью: правки по статье X"
git push origin main

# 4. Автор делает git pull и видит твои правки в Obsidian
```

## Команды Git (шпаргалка)

| Команда | Действие |
|---------|----------|
| `git pull` | Получить последние изменения |
| `git status` | Посмотреть, что изменилось |
| `git add -A` | Добавить все изменения |
| `git commit -m "описание"` | Сохранить изменения |
| `git push` | Отправить на сервер |
| `git log --oneline -5` | Последние 5 коммитов |

## Интеграция с Zotero

Скрипт `scripts/zotero-export.py` создаёт literature notes из Zotero базы:
- Заголовок, автор, год, DOI
- Пустые секции для аннотации и цитат
- Автоматические wiki-ссылки для связей

Запускай после каждого добавления источников в Zotero.

## Автопуш в Git

После каждого коммита изменения автоматически отправляются на GitHub.
Настраивается через git hook `post-commit`.

## Плагины Obsidian (рекомендуемые)

| Плагин | Назначение |
|--------|-----------|
| **Citations** | Вставка цитат из Zotero |
| **Git** | Визуальный интерфейс для Git |
| **Templater** | Шаблоны для новых заметок |
| **Dataview** | Таблицы и списки по метаданным |

---

*Vault template v1.0 | Создано для академического письма*