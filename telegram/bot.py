import os
import random
import string
import zipfile
import telebot
from telebot import types
import json
import shutil

# Инициализация бота
TOKEN = '7413979463:AAHn-kTk8J15PLYHJyzNY_l2RbsGE-_U5ac'  # Замените на свой токен
bot = telebot.TeleBot(TOKEN)

# Путь к папке assets
ASSETS_FOLDER = 'assets/'  # Убедитесь, что эта папка существует

# Словарь для хранения паролей
saved_passwords = {}

# Функция для генерации случайного пароля
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Функция для создания package.json для Vue
def create_package_json(folder_name, run_command_name):
    package_json = {
        "name": folder_name,
        "version": "1.0.0",
        "scripts": {
            f"{run_command_name}": "vue-cli-service serve"
        },
        "dependencies": {
            "vue": "^3.0.0",
            "vue-router": "^4.0.0"
        },
        "devDependencies": {
            "@vue/cli-service": "^5.0.0"
        }
    }
    package_path = os.path.join(folder_name, 'package.json')
    with open(package_path, 'w') as f:
        json.dump(package_json, f, indent=2)

# Функция для создания папки src и файлов Vue с учетом выбранных библиотек
def create_vue_files(folder_name, file_types):
    src_folder = os.path.join(folder_name, 'src')
    os.makedirs(src_folder, exist_ok=True)
    
    # Файл main.js
    with open(os.path.join(src_folder, 'main.js'), 'w') as f:
        f.write("""import { createApp } from 'vue';
import App from './App.vue';
import './main.css';

createApp(App).mount('#app');
""")
    
    # Файл App.vue
    with open(os.path.join(src_folder, 'App.vue'), 'w') as f:
        f.write("""<template>
  <div id="app">
    <h1>Hello Vue!</h1>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style scoped>
/* Add your styles here */
</style>
""")
    
    # Файл main.css
    with open(os.path.join(src_folder, 'main.css'), 'w') as f:
        f.write("""/* Add your CSS styles here */\n""")
    
    # Обновление index.html для подключения Vue и выбранных библиотек
    index_path = os.path.join(folder_name, 'public', 'index.html')
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    
    scripts_and_styles = []
    
    if '2' in file_types:
        scripts_and_styles.append('<link rel="stylesheet" type="text/css" href="styles/style.css">')
    if '3' in file_types:
        scripts_and_styles.append('<script src="javaScript/script.js"></script>')
    if '5' in file_types:
        scripts_and_styles.append('<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>')
    if '6' in file_types:
        scripts_and_styles.append('<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>')
    if '7' in file_types:
        scripts_and_styles.append('<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.css"/>')
        scripts_and_styles.append('<script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js"></script>')
    if '9' in file_types:
        # Здесь можно подключить дополнительные ресурсы, если они нужны для Vue
        pass
    
    with open(index_path, 'w') as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{folder_name}</title>
    {''.join(scripts_and_styles)}
</head>
<body>
    <div id="app"></div>
    <script src="/src/main.js"></script>
</body>
</html>
""")

# Функция для создания файлов по типу
def create_files_by_type(folder_name, file_types):
    if '1' in file_types:
        # Создаем index.html и подключаем файлы стилей и скриптов
        public_folder = os.path.join(folder_name, 'public')
        os.makedirs(public_folder, exist_ok=True)
        with open(os.path.join(public_folder, 'index.html'), 'w') as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Test</title>\n")
            if '2' in file_types:
                f.write('<link rel="stylesheet" type="text/css" href="styles/style.css">\n')
            if '3' in file_types:
                f.write('<script src="javaScript/script.js"></script>\n')
            if '5' in file_types:
                f.write('<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>\n')
            if '6' in file_types:
                f.write('<script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>\n')   
            if '7' in file_types:
                f.write('<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.css"/>\n')
                f.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js"></script>\n')
            f.write("</head>\n<body>\n</body>\n</html>")

    if '2' in file_types:
        # Создаем папку styles и файл style.css
        styles_folder = os.path.join(folder_name, 'styles')
        os.makedirs(styles_folder, exist_ok=True)
        with open(os.path.join(styles_folder, 'style.css'), 'w') as f:
            f.write("/* Styles */\n")

    if '3' in file_types:
        # Создаем папку javaScript и файл script.js
        js_folder = os.path.join(folder_name, 'javaScript')
        os.makedirs(js_folder, exist_ok=True)
        with open(os.path.join(js_folder, 'script.js'), 'w') as f:
            f.write("// JavaScript\n")

    if '4' in file_types:
        # Создаем файл python.py
        with open(os.path.join(folder_name, 'python.py'), 'w') as f:
            f.write("# Python script\n")

    if '8' in file_types:
        # Добавляем папку assets из существующего каталога
        assets_dest = os.path.join(folder_name, 'assets')
        if os.path.exists(ASSETS_FOLDER):
            shutil.copytree(ASSETS_FOLDER, assets_dest)

# Функция для создания папки с файлами и упаковки в ZIP
def create_and_zip_folder(folder_name, file_types, run_command_name=None):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    create_files_by_type(folder_name, file_types)

    # Проверяем, если выбран Vue
    if '9' in file_types:
        # Создаем папку src и файлы для Vue
        create_vue_files(folder_name, file_types)
        # Генерируем package.json для Vue
        create_package_json(folder_name, run_command_name)
    
    # Создаем ZIP архив
    zip_name = f"{folder_name}.zip"
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, os.path.join(folder_name, '..')))

    return zip_name

# Функция для удаления папки после создания и отправки архива
def clean_up(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)

# Функция для создания и отправки ZIP файла пользователю
def send_zip_file(chat_id, zip_file, folder_name):
    with open(zip_file, 'rb') as f:
        bot.send_document(chat_id, f, caption=f"Ваш архив {folder_name}")
    os.remove(zip_file)  # Удаляем временный ZIP-файл
    clean_up(folder_name)  # Удаляем временную папку

# Обработка команды /paks для создания архива и отправки
@bot.message_handler(commands=['paks'])
def handle_paks_command(message):
    msg = bot.send_message(message.chat.id, "Введите название папки:")
    bot.register_next_step_handler(msg, process_folder_name)

def process_folder_name(message):
    folder_name = message.text.strip()
    msg = bot.send_message(message.chat.id, "Введите типы файлов (например, '1 2 3 5 6 7 9 8'):")
    bot.register_next_step_handler(msg, lambda msg: process_file_types(msg, folder_name))

def process_file_types(message, folder_name):
    file_types = message.text.strip().split()
    run_command_name = None
    
    if '9' in file_types:
        msg = bot.send_message(message.chat.id, "Введите название команды для npm run:")
        bot.register_next_step_handler(msg, lambda msg: create_zip_with_command(msg, folder_name, file_types))
    else:
        zip_file = create_and_zip_folder(folder_name, file_types)
        send_zip_file(message.chat.id, zip_file, folder_name)

def create_zip_with_command(message, folder_name, file_types):
    run_command_name = message.text.strip()
    zip_file = create_and_zip_folder(folder_name, file_types, run_command_name)
    send_zip_file(message.chat.id, zip_file, folder_name)

# Обработка команды /password для генерации пароля
@bot.message_handler(commands=['password'])
def handle_password_command(message):
    password = generate_password()
    bot.send_message(message.chat.id, f'Ваш случайный пароль: {password}')
    
    # Кнопка для сохранения пароля
    markup = types.InlineKeyboardMarkup()
    save_button = types.InlineKeyboardButton("Сохранить пароль", callback_data=f"save_password:{password}")
    markup.add(save_button)
    
    bot.send_message(message.chat.id, "Хотите сохранить этот пароль?", reply_markup=markup)

# Обработка нажатия кнопки сохранения пароля
@bot.callback_query_handler(func=lambda call: call.data.startswith("save_password"))
def handle_save_password(call):
    password = call.data.split(":")[1]
    msg = bot.send_message(call.message.chat.id, "Введите название для этого пароля:")
    bot.register_next_step_handler(msg, lambda msg: save_password(msg, password))

def save_password(message, password):
    name = message.text.strip()
    saved_passwords[name] = password
    bot.send_message(message.chat.id, f"Пароль '{password}' сохранен под названием '{name}'")

# Обработка команды /room для отображения сохраненных паролей
@bot.message_handler(commands=['room'])
def handle_room_command(message):
    if saved_passwords:
        response = "Сохраненные пароли:\n"
        for name, password in saved_passwords.items():
            response += f"{name} - {password}\n"
        bot.send_message(message.chat.id, response)
    else:
        bot.send_message(message.chat.id, "Нет сохраненных паролей.")

# Обработка команды /start для приветственного сообщения
@bot.message_handler(commands=['start'])
def handle_start_command(message):
    bot.send_message(message.chat.id, "Привет! Используйте /paks для создания архивов, /password для генерации пароля, кнопка save для сохранения пароля, и /room для отображения сохранённых паролей.")

# Запуск бота
bot.polling(none_stop=True)













