# <center> Проект для Head Hunter </center>
## Оглавление
1. [Описание проекта](#описание-проекта)
2. [О структуре проекта](#о-структуре-проекта)
3. [Зависимости](#Зависимости)
4. [Установка проекта](#установка-проекта)
5. [Использование проекта](#использование-проекта)
6. [Авторы и контрибьютеры](#авторы-и-контрибьютеры)
7. [Выводы](#выводы)

## Описание проекта
**Цель проекта**: построить модель, которая бы выявляла и визуализировала факторы, влияющие на уровень желаемой заработной платы.

Проект состоит из 4-х этапов:
1. **Базовый анализ структуры данных**


>Знакомимся с данными и исследуем их структуру. Нам важно понять, как устроены признаки в данных и какие типы они имеют, чтобы произвести дальнейшие преобразования.
2. **Преобразование данных**
- колонку **«Образование и ВУЗ»** приеобразовываем в новый признак **«Образование»**, который должен иметь 4 категории: *«высшее»*, «*неоконченное высшее»*, *«среднее специальное»* и *«среднее»*.
- столбец **«Пол, возраст»** разобъем на две колонки:
    
    **"Пол"** - со значаниями "М" и "Ж" и...

    **"Возраст"** - в виде целого числа.
- признак **«Опыт работы»** представим в Месяцах (а не в *Годах* и *Месяцах*)
- признак **«Город, переезд, командировки»** разложим на:

    -- **"Город"** с 4-мя категориями: *«Москва»*, «*Санкт_Петербург*", *«Город-миллионник»* и *«Другие»*.
    -- **"Готовность к переезду"** - с булевыми значениями (*True/False*).
    -- **"Готовность к командирокам"** - с булевыми значениями (*True/False*).
- из признака «Занятость» сделаем колонки **"полная занятость"**, **"частичная занятость"**, **"проектная работа"**, **"волонтёрство"**, **"стажировка"** с булевыми значениями (*True/False*).
- из признака  «График» сделаем колонки **"полный день"**, **"сменный график"**, **"гибкий график"**, **"удалённая работа"**, **"вахтовый метод"** с булевыми значениями (*True/False*).
- и финально, расчитываем желаемую зарплату (колонка **"ЗП (руб)"**) в рублях:

    -- из признака **"ЗП"** выделяем размер ЗП и Валюту
    
    -- преобразовываем Валюту к стандарту ISO
    
    -- подтягиваем данные о Курсе на День Обновления резюме

    -- расчитываем размер желаемой зарплаты (*'Курс' * 'ЗП'*)

**N.B:** После преобразования все изначальные колонки <ins>удаляем</ins>!

3. **Разведывательный анализ**...

осуществляется на базе графиков, позволяющих визуализировать данные - см. jupyter-notebook.


4. **Очистка данных**

+ состоит в нахождении полных дубликатов записей
+ в удалении дубликатов
+ в идентифицировании пропусков
+ в удалении и/или заполнении пропусков


## О структуре проекта
* [data](https://drive.google.com/file/d/1vJayOym05eqpUI1x1fca0sme-25DAKeu/view?usp=share_link) - папка с исходными табличными данными.
* [Курсы валют](https://drive.google.com/file/d/1aCm8xEhe9VjTlRm6Kb7loMEORmymY3JV/view?usp=share_link) - файл с курсами валют за соответствующий период времени.
* [Коды валют](./Currency_ISO.xlsx) - информация о ISO кодировке валют.
* [SB_PJ_01.ipynb](./PJ_Folder/SB_PJ_01.ipynb) - jupyter-ноутбук, содержащий основной код проекта.

## Зависимости
* Python (3.9):
    * [numpy (1.20.3)](https://numpy.org)
    * [pandas (1.3.4)](https://pandas.pydata.org)
    * [matplotlib (3.4.3)](https://matplotlib.org)
    * [seaborn (0.11.2)](https://seaborn.pydata.org)
## Установка проекта
```
https://github.com/mrglibly/SBProject_01
```

## Использование проекта
Вся информация о работе представлена в jupyter-ноутбуке SB_PJ_01.ipynb.
## Авторы и контрибьютеры
Работу выполнил Сергей Бойко при содействии Елены Мартыновой, ментора.
## Выводы
В процессе работы были выявлен ряд основных факторов, влияющих заимозависимости на размер желаемой зарплаты.