# 📚 Academic Vault

Шаблон Obsidian vault для научного письма с Zotero интеграцией и Git backup.

**Репозиторий:** https://github.com/MediaCod22/academic-vault

---


## 🌐 Серверная инфраструктура

Для совместной работы развёрнуто на российском сервере (213.171.9.30):

| Сервис | Адрес | Назначение |
|--------|-------|-----------|
| **HedgeDoc** | http://213.171.9.30:3006 | Real-time редактирование через браузер |
| **Git Backup** | ssh://root@213.171.9.30/srv/git/academic-vault.git | Дополнительный backup |

**Полная инструкция по доступам:** [SERVER_ACCESS.md](SERVER_ACCESS.md)

---

## Быстрый старт (3 шага)

### Шаг 1: Склонируй репозиторий

```bash
git clone https://github.com/MediaCod22/academic-vault.git ~/ObsidianVault
```

### Шаг 2: Открой в Obsidian

**File → Open folder as vault → выбери ~/ObsidianVault**

### Шаг 3: Настрой Git (один раз)

```bash
cd ~/ObsidianVault
git config user.name "Твое Имя"
git config user.email "email@example.com"
git config core.hooksPath .githooks
git remote set-url origin https://ТВОЙ_ТОКЕН@github.com/MediaCod22/academic-vault.git
```

**Готово!** Теперь после каждого коммита изменения автоматически отправляются на GitHub.

---

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
│   ├── literature-note.md
│   └── article-draft.md
├── scripts/               # Скрипты автоматизации
│   ├── zotero-export.py   # Экспорт источников из Zotero
│   └── post-commit-hook.sh
└── .githooks/             # Git hooks (автопуш)
    └── post-commit
```

---

## Для редактора

```bash
# 1. Склонируй репозиторий
git clone https://github.com/MediaCod22/academic-vault.git

# 2. Сделай правки в файлах .md (любой редактор: VS Code, Obsidian, vim)

# 3. Отправь изменения
git add -A
git commit -m "ревью: правки по статье X"
git push origin main

# 4. Автор делает git pull и видит твои правки в Obsidian
```

**Инструкция для редактора в README подробная.** Редактору не нужен Obsidian — достаточно любого текстового редактора.

---

## Основные команды

| Команда | Действие |
|---------|----------|
| `git pull` | Получить последние изменения |
| `git status` | Посмотреть, что изменилось |
| `git add -A` | Добавить все изменения |
| `git commit -m "описание"` | Сохранить изменения |
| `git push` | Отправить на сервер |
| `git log --oneline -5` | Последние 5 коммитов |

---

## Интеграция с Zotero

### Экспорт источников

```bash
python3 scripts/zotero-export.py
```

Создаёт literature notes в папке `01-sources/` с:
- Заголовком, автором, годом, DOI
- Пустыми секциями для аннотации и цитат
- Автоматическими wiki-ссылками для связей

Запускай после каждого добавления источников в Zotero.

### Цитирование в Obsidian

Установи плагин **Citations**:
- Горячая клавиша: `Ctrl+Shift+E`
- Вставляет: `[@author2024]` или полную цитату

---

## Автоматизация

### Автопуш в Git

Настроен через git hook `.githooks/post-commit`:
```bash
git config core.hooksPath .githooks
```

После каждого коммита изменения автоматически отправляются на GitHub.

### Автобэкап (опционально)

Установи плагин **Git** в Obsidian:
- Auto backup: каждые 10 минут
- Auto push: включено
- Или используй cron:
```bash
*/10 * * * * cd ~/ObsidianVault && git add -A && git commit -m "auto: $(date +%H:%M)" && git push
```

---

## Плагины Obsidian (рекомендуемые)

| Плагин | Назначение | Установка |
|--------|-----------|-----------|
| **Citations** | Вставка цитат из Zotero | Community plugins → "Citations" |
| **Git** | Визуальный интерфейс для Git | Community plugins → "Git" |
| **Templater** | Шаблоны для новых заметок | Community plugins → "Templater" |
| **Dataview** | Таблицы и списки по метаданным | Community plugins → "Dataview" |

---

## Пример статьи

В папке `02-articles/01-drafts/` лежит пример: `article-01-media-conflict.md`

Показывает структуру:
- YAML frontmatter (title, author, status, tags)
- Разделы: аннотация, введение, литобзор, методология, результаты
- Wiki-ссылки на источники: `[[source-vodopetov-2025]]`
- Чеклист редактора в конце

---

## Чеклист для новой статьи

- [ ] Создать файл в `02-articles/01-drafts/`
- [ ] Использовать шаблон: `Alt+E` → `article-draft`
- [ ] Заполнить YAML frontmatter
- [ ] Добавить wiki-ссылки на источники из `01-sources/`
- [ ] Написать черновик
- [ ] Переместить в `02-articles/02-review/` для редактора
- [ ] После ревью: в `02-articles/03-published/`
- [ ] Закоммитить и запушить

---

## Решение твоих проблем

| Проблема | Решение |
|----------|---------|
| Источники забываются | Экспорт из Zotero → literature notes с wiki-ссылками |
| Тексты статей теряются | Git версионирование + автопуш на GitHub |
| Нет структуры | Шаблоны: article-draft, literature-note |
| Редактор не видит правки | Git pull → редактор правит → git push → ты видишь в Obsidian |
| Нет резервных копий | GitHub хранит всю историю, доступна с любого устройства |

---

*Vault template v1.0 | Создано для академического письма*
