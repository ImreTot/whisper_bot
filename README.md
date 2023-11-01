Whisper Telegram bot

Powered by  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

## Бот переводчик аудио в текст
Разрабатывается на aiogram. Использует модель Whisper от OpenAI (предпочтительно версию на C++, так как она быстрее работает)
Прототип (последовательные шаги)
- Создан бот в Telegram
- Бот реагирует на действия пользователя (кнопка Start)
- Бот позволяет загружать файл 
- Бот отправляет файл в модель для расшифровки
- Бот возвращает ответ пользователю в формате .txt  

В первоначальной версии не подразумеваются настройки распознавания речи.

