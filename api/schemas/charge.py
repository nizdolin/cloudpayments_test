from dataclasses import dataclass, field
from typing import Optional

from marshmallow import validate
from marshmallow_dataclass import class_schema, NewType
from marshmallow_dataclass.typing import Email, Url

from api.constants import CULTURE_NAMES, CURRENCIES


IPv4 = NewType(
    "IPv4", str, validate=validate.Regexp(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
)

Name = NewType(
    'Name', str, validate=validate.Regexp(r'^[a-zA-Z\s]*$')
)


@dataclass
class Payer:
    FirstName: Optional[str]
    LastName: Optional[str]
    MiddleName: Optional[str]
    Birth: Optional[str]
    Street: Optional[str]
    Address: Optional[str]
    City: Optional[str]
    Country: Optional[str]
    Phone: Optional[str]
    Postcode: Optional[str]


@dataclass
class Charge:
    Amount: float = field(metadata=dict(validate=validate.Range(min=0.01)))
    Currency: Optional[str] = field(metadata=dict(validate=validate.OneOf(CURRENCIES)))
    IpAddress: IPv4
    Token: str  # Yandex Pay Token (Base64)
    Name: Optional[Name]
    PaymentUrl: Optional[Url]
    InvoiceId: Optional[str]
    Description: Optional[str]
    CultureName: Optional[str] = field(metadata=dict(validate=validate.OneOf(CULTURE_NAMES)))
    AccountId: str
    Email: Optional[Email]
    Payer: Optional[Payer]


ChargeSchema = class_schema(Charge)
