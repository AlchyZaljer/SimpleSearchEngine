# **SimpleSearchEngine**

### Консольное приложение, реализующее простой текстовый поисковый движок

## **Функциональность**

1. Индексация документов

2. Поиск с использованием TF-IDF

3. Релевантная сортировка результатов.

## **Принцип работы**
1. **Индексация**:
   - При запуске приложения индексируются указанные текстовые файлы.
   - Для каждого документа создается список слов и их частота *(TF — Term Frequency)*.

2. **Подсчет IDF**:
   - Вычисляется *Inverse Document Frequency (IDF)* для каждого слова: чем реже слово встречается в документах, тем выше его значимость.

3. **Взвешивание релевантности**:
   - Для каждого запроса программа вычисляет TF-IDF для всех слов запроса в каждом документе.
   - Итоговая релевантность документа равна сумме TF-IDF всех слов запроса.

4. **Сортировка результатов**:
   - Документы сортируются по их релевантности и возвращаются в виде списка.

## **Пример использования**

1. **Входные данные**:

  - Файл `docs/a.txt` с содержимым:

    ```
    Central component.
    
    The inverted index data structure is a central component of a typical search engine indexing algorithm.
    ```

  - Файл `docs/b.txt` с содержимым:

    `The speed of finding an entry in a data structure, compared with how quickly it can be updated, is a crucial focus of computer science.`

2. **Запрос**:

   `Inverted index (DATA STRUCTURE).`

3. **Результат** (список отсортированных по релевантности документов):

  `[SearchResult(name='docs/a.txt', score=0.04505167867868493), SearchResult(name='docs/b.txt', score=0.0)]`
