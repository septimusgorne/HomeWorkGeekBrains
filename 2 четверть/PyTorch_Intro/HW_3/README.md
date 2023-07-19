# Урок 3. Dataset, Dataloader, BatchNorm, Dropout, Оптимизация

- Создать Dataset для загрузки данных (sklearn.datasets.fetch_california_housing)
- Обернуть его в Dataloader
- Написать архитектуру сети, которая предсказывает стоимость недвижимости. Сеть должна включать BatchNorm слои и Dropout (или НЕ включать, но нужно обосновать)
- Сравните сходимость Adam, RMSProp и SGD, сделайте вывод по качеству работы модели train-test разделение нужно сделать с помощью sklearn random_state=13, test_size = 0.25
