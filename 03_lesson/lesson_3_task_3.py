from address import Address
from mailing import Mailing

to_address = Address("445025", "Санкт-Петербург", "Пушкина", "55", "7")
from_address = Address("617400", "Москва", "Ленина", "10", "75")

mailing = Mailing("TRK476990", from_address, to_address, "150")
print(
    f"Почтовое отправление номер: {mailing.trak} из {mailing.from_address.postal_code}, {mailing.from_address.city}, "
    f"{mailing.from_address.street} {mailing.from_address.house} - {mailing.from_address.apartment} в "
    f"{mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street} "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимостью {mailing.cost} рублей."
)