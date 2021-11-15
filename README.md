## Getting started
****
### Requirements
    - aiohttp==3.8.0
    - pydantic==1.8.2 
    - pandas==1.3.4

### Module App
    view.py: Компонует и отображает данные в консоль.
    model.py: Содержит данные моделей для сбора информации с ресурсов криптобирж.
    setting.py: API криптобирж, Словарь {CryptoModel: URl_API}, Список группирования по валютным парам.
    main.py Запускает и создает задачи.


### How start
1.      Start in docker:
   
        docker build -t test_task .
        docker run -e DIRECTORY='/tmp/test' -v /tmp/:/tmp/ test_task

2.      Start in console:
   
        python app/main.py