from address import Address


class Mailing:
    def __init__(self, track: str, from_address: Address,
                 to_address: Address,  cost: float):
        self.track = track
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost

    def __str__(self):
        return f"Почтовое отправление номер {self.track} из {self.from_address} в {self.to_address}. Cтоимостью {self.cost} рублей"
