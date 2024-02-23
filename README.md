# Тестовое задание выполненное на Python
- Сверстать простой лэнд, где будет форма заказа с полями для ввода имени и номера телефона, и одно скрытое поле со значением test
- Если форма была заполнена, то данные должны передаваться в сторонний сервис POST запросом
- Если ответ успешный, то человека нужно перевести на другую страницу с простым текстом “спасибо за заказ”, иначе с текстом “ошибка”
- Сделать простую валидацию на корректность номера, пример: +7(777)777-77-77
- Сделать невозможным отправку данных второй раз для одного человека. То есть чтобы не было от одного и того же человека нескольких одинаковых заявок.

---

## О проекте:
- _Была создана модель с полями для ввода имени и телефона и скрытым полем со значением по умолчанию "test"._
- _На основе модели написана форма с соответствующими полями для ввода данных_.
- _У полей имеются параметры для валидации данных: уникальность заявок пользователей и корректность номера телефона._
- _Обработку данных, отправку POST-запроса и вставку ответа/информации в шаблон выполняет представление._
- _Также создан простой шаблон для прорисовки формы и сообщения об успехе операции или ошибке введенных данных._

Пользователь заходит на страницу, вводит данные, которые проверяются на валидность и уникальность и отправляются POST-запросом на сторонний сервис. В зависимости от корректности данных, пользователя перенапрявляет на страницу с сообщением об ошибке или успехе.
