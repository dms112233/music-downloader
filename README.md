# music-downloader

Утилита для загрузки музыки с сайта https://rus.hitmotop.com/

# Установка

Для Linux:  
 python3 -m venv venv  
 source venv/bin/activate  
 pip install -r requirements.txt

Для Windows:  
 python -m venv venv  
 ./venv/Scripts/activate  
 pip install -r requirements.txt

# Использование

python3 hitmos_downloader.py "https://rus.hitmotop.com/..." "Папка куда будет скачиваться"

Пример:  
python3 hitmos_downloader.py https://rus.hitmotop.com/genre/51 \~/Downloads/
