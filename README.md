# styletransfer-bot

## Чтобы запустить: 
```bash
git clone https://github.com/Szirx/styletransfer_bot.git
cd styletransfer_bot
docker build -t styletransferbot .
docker run -d styletransferbot
```

Идея проекта заключается в использовании style-transfer нейронной сети https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2 посредством бота в telegram. Для взаимодействия с ботом и получения дальнейших инструкций необходимо ввести команду /start.  
