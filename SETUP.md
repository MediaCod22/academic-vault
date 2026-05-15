# Настройка Obsidian + Zotero

## 1. Установи Obsidian

Скачай с https://obsidian.md/ (бесплатно для личного использования)

## 2. Открой vault

```bash
git clone https://github.com/MediaCod22/academic-vault.git ~/ObsidianVault
```

В Obsidian: **File → Open folder as vault → выбери ~/ObsidianVault**

## 3. Настрой Git

```bash
cd ~/ObsidianVault
git config user.name "Твое Имя"
git config user.email "email@example.com"
git remote set-url origin https://ТВОЙ_ТОКЕН@github.com/MediaCod22/academic-vault.git
```

## 4. Настрой автопуш (git hook)

```bash
cd ~/ObsidianVault
git config core.hooksPath .githooks
```

Теперь после каждого коммита изменения автоматически отправляются в GitHub.

## 5. Установи плагины Obsidian

### Citations (Zotero интеграция)
1. Настройки → Community plugins → Browse → "Citations"
2. Укажи путь к Zotero SQLite: `~/Zotero/zotero.sqlite`
3. Горячая клавиша: `Ctrl+Shift+E` — вставить цитату

### Git (визуальный интерфейс)
1. Настройки → Community plugins → Browse → "Git"
2. Настрой автокоммит: Settings → Auto backup → Interval: 10 минут
3. Настрой автопуш: Settings → Auto backup → Push: true

### Templater (шаблоны)
1. Настройки → Community plugins → Browse → "Templater"
2. Укажи папку шаблонов: `99-templates`
3. Горячая клавиша: `Alt+E` — вставить шаблон

## 6. Экспортируй источники из Zotero

```bash
cd ~/ObsidianVault
python3 scripts/zotero-export.py
```

Создаст literature notes в папке `01-sources/`.

## 7. Начни писать

1. Создай новую заметку в `02-articles/01-drafts/`
2. Используй шаблон: `Alt+E` → выбери `article-draft`
3. Вставляй цитаты: `Ctrl+Shift+E` → выбери источник
4. Связывай заметки: `[[название-заметки]]`

## 8. Сохраняй и отправляй

```bash
cd ~/ObsidianVault
git add -A
git commit -m "work: прогресс по статье"
# Автопуш сработает через hook
```

Или используй плагин Git — он делает это автоматически.

---

*Настройка завершена. Всё версионировано, всё бэкапится.*