# Древовидное меню
Необходимо сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
- Меню реализовано через template tag;
- Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут;
- Хранится в БД;
- Редактируется в стандартной админке Django
- Активный пункт меню определяется исходя из URL текущей страницы;
- Меню на одной страницы может быть несоколько, они определяются по названию;
- При клике на меню происходит переход по заданному в нем URL. Он может быть задан как явным образом, так и через named URL;
- На отрисовку каждого меню требуется ровно 1 запрос к БД.

Нужен django-app который ползволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию. {% draw_menu 'main_menu' %}

## Быстрый старт

###  Клонируйте репозиторий, включая зависимости:
`git clone https://github.com/AdelaYa/tree_menu`

###  Запустите команды:
`docker-compose build`

`docker-compose up`

###  Вы можете просматривать пользовательский интерфейс  в своем  браузере по этому URL-адресу:
` http://0.0.0.0:8000/`


###  Для остановки работы контейнера запустите в каталоге где он был запущен команду:
`docker-compose down `

### Для авторизации в админке:
логин - admin, пароль - 12345678