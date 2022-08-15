from archgame import constants

ASK_QUANTITY = "Сколько будет игроков? "
ASK_NAME = "Введите имя игрока %d "

LEGEND = """A - API: умеет принимать нагрузку от пользователей, может выдержать до {0}к
    нагрузки, для работы нужна DB

D - DB: умеет обрабатывать запросы от API, может поддерживать до {1}х API

L - LoadBalancer: Позволяет масштабировать API, без него максимальная
    производительность всех API не превышает производительности одного API. Может
    обслуживать не больше {2}х API

B - Backup: В случае ошибки DBA позволяет избежать потери пользовательской
    базы, но снимается с игрового поля.""".format(constants.LIM_A, constants.LIM_D, constants.LIM_L)

SPRINTS = "Спринт %d:"

INPUT_ACTION = "Введите действие для игрока %s: "

DESC = """
Вам пришло финансирование, у каждого игрока есть 2 очка, которые он может
потратить либо на привлечение новых пользователей(1), либо на установку новых
сервисов(2):
"""

ENDING = "Поздравляем победителя %s!!!"


#Тексты событий
TEXT_DBA = "DBA: при переносе реплики я потерял таблицу. данных больше нет."
TEXT_DEL_API = "Минус одна апишка №%d"
TEXT_BANKRUPT = "Банкротство - Дает -1 очко"
TEXT_ADD_RANDOM_API = "Дается Дополнительно АПИ"
TEXT_ADD_RANDOM_DB = "Дается Дополнительно БД"
TEXT_ADD_RANDOM_LB = "Дается Дополнительно ЛБ"
TEXT_DROP_CELL = "Упала ячейка №%d"
TEXT_ADMIN_ERROR = "Админы ошиблись в коммутации"
TEXT_ADD_AMOUNT = "Пришло %iк, если не тянешь — потеря %iк"
TEXT_ADD_1K = "Пришло 1к, если не тянешь — потеря 1к"
TEXT_ADD_2K = "Пришло 2к, если не тянешь — потеря 1к"
TEXT_ADD_3K = "Пришло 3к, если не тянешь — потеря 1к"
TEXT_DROP_COMPONENT = "Вынести компонент №%d"
TEXT_LEFT_RIGHT_1K = "По 1к пользователей ушли к конкуренту справа и слева"
TEXT_DROP_RACK = "Вылетела стойка"
TEXT_RIGHT_COMPONENT = "Компонент №%d ушел вправо"
