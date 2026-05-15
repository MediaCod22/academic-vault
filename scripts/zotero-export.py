#!/usr/bin/env python3
"""
Zotero → Obsidian Literature Notes
Экспортирует источники из Zotero SQLite базы в markdown-заметки.

Требования: Python 3.8+
Использование: python3 scripts/zotero-export.py
"""

import sqlite3
import re
import os
from pathlib import Path
from datetime import datetime

# Конфигурация
ZOTERO_DB = os.path.expanduser("~/Zotero/zotero.sqlite")
OUTPUT_DIR = Path(__file__).parent.parent / "01-sources"

# SQL-запрос для извлечения данных
QUERY = """
SELECT 
    i.itemID,
    COALESCE(t.value, 'Без названия') as title,
    COALESCE(d.value, '') as date,
    COALESCE(u.value, '') as url,
    COALESCE(doi.value, '') as doi
FROM items i
LEFT JOIN itemData id_title ON i.itemID = id_title.itemID AND id_title.fieldID = 1
LEFT JOIN itemDataValues t ON id_title.valueID = t.valueID
LEFT JOIN itemData id_date ON i.itemID = id_date.itemID AND id_date.fieldID = 6
LEFT JOIN itemDataValues d ON id_date.valueID = d.valueID
LEFT JOIN itemData id_url ON i.itemID = id_url.itemID AND id_url.fieldID = 8
LEFT JOIN itemDataValues u ON id_url.valueID = u.valueID
LEFT JOIN itemData id_doi ON i.itemID = id_doi.itemID AND id_doi.fieldID = 26
LEFT JOIN itemDataValues doi ON id_doi.valueID = doi.valueID
WHERE i.itemTypeID != 1  -- исключаем заметки Zotero
ORDER BY i.dateAdded DESC
"""

def slugify(text):
    """Создаёт безопасное имя файла из названия."""
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.lower()[:50]

def get_authors(conn, item_id):
    """Получает список авторов для item."""
    cur = conn.execute("""
        SELECT c.firstName, c.lastName
        FROM itemCreators ic
        JOIN creators c ON ic.creatorID = c.creatorID
        WHERE ic.itemID = ?
        ORDER BY ic.orderIndex
    """, (item_id,))
    authors = []
    for first, last in cur.fetchall():
        name = f"{last} {first}".strip()
        if name:
            authors.append(name)
    return ", ".join(authors) if authors else "Не указан"

def create_literature_note(item_id, title, date, url, doi, authors):
    """Создаёт markdown-заметку для источника."""
    
    # Безопасный ключ Zotero (последние 8 символов itemID)
    zotero_key = f"item_{item_id}"
    
    # Год из даты
    year = date[:4] if date and len(date) >= 4 else "n.d."
    
    # Имя файла
    slug = slugify(title)
    filename = f"source-{slug}.md"
    filepath = OUTPUT_DIR / filename
    
    # Содержимое
    content = f"""---
source: {title}
author: {authors}
year: {year}
doi: {doi}
zotero_key: {zotero_key}
tags: [source, literature]
---

# {title}

**Автор:** {authors}  
**Год:** {year}  
**DOI:** {doi or '—'}  
**URL:** {url or '—'}

## Аннотация
(добавить после прочтения)

## Ключевые тезисы
- 

## Цитаты
> 

## Критика / оценка
- 

## Связи
- [[ ]]

## Использовано в статьях
- [[ ]]

## Примечания
"""
    
    filepath.write_text(content, encoding='utf-8')
    return filename

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    if not os.path.exists(ZOTERO_DB):
        print(f"❌ База Zotero не найдена: {ZOTERO_DB}")
        print("Укажи правильный путь в переменной ZOTERO_DB")
        return
    
    conn = sqlite3.connect(ZOTERO_DB)
    conn.row_factory = sqlite3.Row
    
    items = conn.execute(QUERY).fetchall()
    created = 0
    
    for item in items:
        authors = get_authors(conn, item['itemID'])
        filename = create_literature_note(
            item['itemID'],
            item['title'],
            item['date'],
            item['url'],
            item['doi'],
            authors
        )
        created += 1
        print(f"✓ {filename}")
    
    conn.close()
    
    print(f"\n🎉 Экспортировано: {created} источников → {OUTPUT_DIR}")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("\n💡 Следующие шаги:")
    print("   1. git add -A")
    print("   2. git commit -m 'sources: обновление из Zotero'")
    print("   3. git push")

if __name__ == "__main__":
    main()
