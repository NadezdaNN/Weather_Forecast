# Тема проекта. Прогноз погоды

## Оглавление  
[1. Описание проекта](./README.md#Описание-проекта)   
[2. Как установить и запустить проект](./README.md#Как-установить-и-запустить-проект)  
[3. Реализация и используемые технологии](./README.md#Реализация-и-используемые-технологии)

### Описание проекта 
Проект представляет из себя web приложение, оно же сайт, где пользователь вводит название города, и получает прогноз погоды в этом городе на ближайшее время. В приложении для получения прогноза используется API https://open-meteo.com/ 

Дополнительно реализовано:
- тесты
- докер контейнер
- сделано автодополнение (подсказки) при вводе города
- при повторном посещении сайта предложено посмотреть погоду в городе, в котором пользователь смотрел ранее
- сохраняется история поиска для пользователя, и реализовано API, показывающее сколько раз он смотрел прогноз в конкретном городе

### Как установить и запустить проект
Выполнить следующие команды в терминале (у меня Ubuntu / VS Code):
1. git clone https://github.com/NadezdaNN/Weather_Forecast.git
2. Перейти в папку: cd ./Weather_Forecast
3. Создать виртуальное окружение: python3 -m venv .venv
4. Активировать его: source .venv/bin/activate
5. Установить зависимости: pip install -r requirements.txt
6. При необходимости установить необходимые модули через pip install 
7. Для запуска проекта выполнить команду в терминале: python3 ./main.py
8. Для проверки работы API приложения, в соседнем терминале выполняем: python3 ./api.py Moscou Москва Тверь
9. Образ для запуска приложения в контейнере: https://hub.docker.com/repository/docker/nadezdann/weather_image/general
10. Запуск теста осуществляется командой: pytest -s -v test_main.py - по умолчанию тестирование приложения происходит в Chrome. Команда pytest -s -v --browser_name=firefox test_main.py - тестирование в Firefox  

### Реализация и используемые технологии
Приложение написано с использованием фреймворка **Flask**, а так же инструментов **HTML** и **CSS**. Для определения координат города был использован сторонний файл russian_towns.tsv содержащий названия городов (и их альтернативные/возможные имена) и их координаты. Для его обработки была использована библиотека **Pandas**. Автодополнения и обновление части html-страницы реализованы с помощью **jQuery**. Для сохранения истории пользователя (города, который пользователь смотрел ранее) использована библиотека **QSettings**. API реализовано с помощью POST-метода в главном файле проекта, а обращение к нему возможно через библиотеку **Requests**, данные передаются в формате **JSON**. Для написания теста использованы фреймворки **Pytest** и **Selenium**. Так же, были использованы: **параметризация** для тестирования приложения с разными входными параметрами (три города - "Moscou", "Москва", "Тула") и **фикстуры** для тестирования приложения в различных браузерах. 
