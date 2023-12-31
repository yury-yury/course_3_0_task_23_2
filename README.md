## Условия домашки

Всё больше пользователей веб-сервиса, над которым вы работаете, пользуется реализованной платформой, 
и администраторы начинают замечать проблемы со скоростью. Проведенное нагрузочное тестирование выявило проблемы, 
с которыми необходимо разобраться.

#### Контекст: зачем решать подобные задачи?
Такая задача встречается разработчику на проектах любого уровня: от простого сайта до сложного личного кабинета 
государственной структуры. Именно поэтому важно научиться распределять права доступа пользователей 
по их ролям в веб-сервисе.

### Задание 1
Продолжаем работать с проектом. Установите брокер для кеширования Redis. Внесите необходимые настройки 
и проверьте работоспособность проекта с новыми настройками.

### Задание 2
Настройте кеширование всего контроллера отображения данных относительно одного продукта.

Помните, что кеширование можно подключать не только в файле views.py, но и в файле маршрутизации urls.py. 
Важно делать всё в одном месте, чтобы достичь единообразия в коде проекта и не запутаться впоследствии.

### Задание 3
Создайте сервисную функцию, которая будет отвечать за выборку категорий и которую можно переиспользовать 
в любом месте системы. Добавьте низкоуровневое кеширование для списка категорий.

### Задание 4
Вынесите необходимые настройки в переменные окружения и настройте проект для работы с ними.

* ### Дополнительное задание
Добавьте кеширование всего сайта целиком, при этом отключите от кеширования определенные контроллеры, 
которые отвечают за работу по заполнению продуктов и блога.


**********************************************************************************************************************

### NOTE:
для функционирования приложения необходимо создать в корне проекта файл .env в котором указать значения
переменных окружения:
- SECRET_KEY=
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME=
- DB_USER=
- DB_PASSWORD=
- DB_HOST=
- DB_PORT=
- EMAIL_HOST=
- EMAIL_PORT=
- EMAIL_HOST_USER=
- EMAIL_HOST_PASSWORD=