from address import Address


class Mailing:
    def __init__(self, track: str, from_address: Address,
                 to_address: Address,  cost: float):
        self.trak = track
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost

    def __str__(self):
        return f"Почтовое отправление номер {self.trak} из "
        return f"{self.from_address} в {self.to_address}."
        return f"Cтоимостью {self.cost} рублей"
