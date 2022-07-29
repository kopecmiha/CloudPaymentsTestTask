import asyncio

from aiohttp import TCPConnector, BasicAuth
from marshmallow import ValidationError

from settings import BASE_URL, PUBLIC_ID, API_SECRET, SERVICE
from abstract import AbstractInteractionClient
from models import method_models_dict


class CloudPaymentsClient(AbstractInteractionClient):
    CONNECTOR = TCPConnector(force_close=True)
    BASE_URL = BASE_URL
    SERVICE = SERVICE

    def __init__(self):
        super().__init__()
        self.public_id = PUBLIC_ID
        self.api_secret = API_SECRET

    async def client_request(self, endpoint, interaction_method, **kwargs):
        auth = BasicAuth(login=self.public_id, password=self.api_secret, encoding='utf-8')
        schema = method_models_dict.get(interaction_method)
        try:
            kwargs = schema.load(kwargs)
        except ValidationError as err:
            raise err
        endpoint_url = self.endpoint_url(endpoint)
        response = await self.post(interaction_method, endpoint_url, auth=auth, json=kwargs)
        await self.close()
        return response


loop = asyncio.get_event_loop()
# пример запроса с оплатой по криптограмме
response = loop.run_until_complete(CloudPaymentsClient().client_request("cards/charge",
                                                                        "cryptogram",
                                                                        Amount=10,
                                                                        Currency="RUB",
                                                                        InvoiceId="1234567",
                                                                        IpAddress="123.123.123.123",
                                                                        Description="Оплата товаров в example.com",
                                                                        AccountId="user_x",
                                                                        Name="CARDHOLDER NAME",
                                                                        CardCryptogramPacket="some_token",
                                                                        CultureName="ru-RUS",
                                                                        Payer={
                                                                            "FirstName": "Тест",
                                                                            "LastName": "Тестов",
                                                                            "MiddleName": "Тестович",
                                                                            "Birth": "1955-02-24",
                                                                            "Address": "тестовый проезд дом тест",
                                                                            "Street": "Lenina",
                                                                            "City": "MO",
                                                                            "Country": "RU",
                                                                            "Phone": "123",
                                                                            "Postcode": "345"
                                                                        },
                                                                        ))
