English Version  
/render_endpoint (POST)
Description: This endpoint receives JSON data with temperature and humidity values, processes it, and updates the global latest_data dictionary with the latest values.
Request Type: POST
Request Payload: The request should contain a JSON object with the following fields:
temperature: (float or string) The temperature value.
humidity: (float or string) The humidity value.
Success Response:
HTTP Status: 200
Response: {"message": "Data received"}
Failure Response:
HTTP Status: 400
Response: {"message": "No data received"}
/display (GET)
Description: This endpoint renders an HTML page that displays the latest temperature and humidity values, which are updated by the /render_endpoint route.
Request Type: GET
Response: Renders the index.html page with the latest data for temperature and humidity passed as variables to the template.
Ukrainian Version
/render_endpoint (POST)
Опис: Цей маршрут приймає JSON дані з показниками температури та вологості, обробляє їх і оновлює глобальний словник latest_data новими значеннями.
Тип запиту: POST
Тіло запиту: Запит повинен містити JSON об'єкт з наступними полями:
temperature: (float або string) Значення температури.
humidity: (float або string) Значення вологості.
Відповідь при успіху:
HTTP статус: 200
Відповідь: {"message": "Data received"}
Відповідь при помилці:
HTTP статус: 400
Відповідь: {"message": "No data received"}
/display (GET)
Опис: Цей маршрут виводить HTML сторінку, яка відображає останні значення температури та вологості, що оновлюються маршрутом /render_endpoint.
Тип запиту: GET
Відповідь: Відображає сторінку index.html, передаючи їй останні дані про температуру та вологість як змінні шаблону.
