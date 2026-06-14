# HW3. Docker, Bash

## Описание

Проект реализует пайплайн обработки данных в Docker:

- генерация CSV-файла `data/data.csv`;
- создание HTML-отчета `data/report.html` на основе CSV;
- запуск веб-сервера `nginx` для просмотра отчета в браузере.

Реализованы контейнеры:

- `csv-generator` — генерирует CSV-файл;
- `csv-reporter` — формирует HTML-отчет;
- `report_server` — раздает HTML-отчет через `nginx`.

## Структура проекта

```text
HW3_TP/
├── .gitignore
├── README.md
└── HW/
    ├── Dockerfile
    ├── Dockerfile.reporter
    ├── HW.ipynb
    ├── docker-compose.yml
    ├── generate.py
    ├── package.json
    ├── report.js
    └── run.sh
```

## Запуск в GitHub Codespaces

Проверяющий может открыть репозиторий в GitHub Codespaces и выполнить:

```bash
cd HW3_TP/HW
chmod +x run.sh
./run.sh build_generator
./run.sh run_generator
./run.sh build_reporter
./run.sh run_reporter
./run.sh report_server
```

После запуска веб-сервера нужно открыть вкладку `Ports`, найти порт `5009` и нажать `Open in Browser`.

После того как открылась главная страница сервера, добавьте к адресу:

```text
/report.html
```

## Автор

```text
ФИО: Лоскутов Александр Михайлович
Группа: ББИ2508
```

## Источники

```text
https://www.opennet.ru/docs/RUS/bash_scripting_guide/x5210.html/
https://docs.docker.com/engine/storage/bind-mounts/
https://docs.docker.com/engine/containers/run/
https://pubs.opengroup.org/onlinepubs/9799919799/utilities/sh.html/
https://docs.python.org/3/library/random.html/
https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-docker/
```
