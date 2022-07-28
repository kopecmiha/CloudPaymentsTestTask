from marshmallow import Schema, fields, validate

allowed_currencies = ["RUB", "EUR", "USD", "GBP", "UAH", "BYR", "BYN", "KZT", "AZN", "CHF", "CZK", "CAD", "PLN", "SEK",
                      "TRY", "CNY", "INR", "BRL", "ZAR", "UZS", "BGN", "RON", "AUD", "HKD", "GEL", "KGS", "AMD", "AED"]


class PayerSchema(Schema):
    FirstName = fields.Str()
    LastName = fields.Str()
    MiddleName = fields.Str()
    Birth = fields.Str()
    Address = fields.Str()
    Street = fields.Str()
    City = fields.Str()
    Country = fields.Str()
    Phone = fields.Str()
    Postcode = fields.Str()


class CryptogramSchema(Schema):
    Amount = fields.Int(required=True)
    Currency = fields.Str(validate=validate.OneOf(allowed_currencies))
    InvoiceId = fields.Str()
    IpAddress = fields.Str(required=True)
    Description = fields.Str()
    AccountId = fields.Str()
    Name = fields.Str()
    CardCryptogramPacket = fields.Str(required=True)
    Payer = fields.Nested(PayerSchema())


method_models_dict = {
    "cryptogram": CryptogramSchema()
}
