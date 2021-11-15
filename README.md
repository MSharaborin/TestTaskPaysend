## Getting started
****
### Requirements
    - aiohttp==3.8.0
    - pydantic==1.8.2 
    - pandas==1.3.4

### Module App
`view.py:` Компонует и отображает данные в консоль.

`model.py:` Содержит данные моделей для сбора информации с ресурсов криптобирж.

`setting.py:` API криптобирж, Словарь {CryptoModel: URl_API}, Список группирования по валютным парам, delay=задает время ожидания задачи.

`main.py` Запускает и создает задачи.


### How start
1. Start in docker:
   
        docker build -t test_task .
        docker run -it test_task

2. Start in console:
   
        python app/main.py

### FAQ

1. Если при запуске докер контейнера не отображаются данные:
   
         попробуйте перезапустить контейнер.