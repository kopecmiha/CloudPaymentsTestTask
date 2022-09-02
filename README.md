Отправка запроса осуществляется с помощью метода "client_request" в класса "CloudPaymentsClient" 
Метод принимает в качестве аргуметов: 
- endpoint - конечный маршрут 
- interaction_method - используется как индикатор для сериализатор, и дальнейшей передачи в абстрактный класс 
- kwargs - все остальные поля 

Сериализатор CryptogramSchema включает поля с требованиями аналоичными с требованиями в документации cloudpayments:  
Amount - обязательное, Integer  
Currency  необязательное, String, значение должно входить в список доступных валют https://developers.cloudpayments.ru/#tipy-uvedomleniy  
InvoiceId - необязательное, String  
IpAddress - обязательное, String  
Description - необязательное, String  
AccountId - необязательное, String  
Name - необязательное, String  
CardCryptogramPacket - обязательное, String  
CultureName - необязательное, String, значение должно входить в список доступных кодов https://developers.cloudpayments.ru/#zapusk-sessii-dlya-oplaty-cherez-apple-pay  
Payer - необязательное, объект плательщика  

Сериализатор PayerSchema включает поля с требованиями аналоичными с требованиями в документации cloudpayments:  
FirstName - необязательное, String  
LastName - необязательное, String  
MiddleName - необязательное, String   
Birth - необязательное, String  
Address - необязательное, String   
Street - необязательное, String  
City - необязательное, String  
Country - необязательное, String  
Phone - необязательное, String  
Postcode - необязательное, String  
