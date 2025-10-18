from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy Z", "+79932271060"),
    Smartphone("iPhone", "15 Pro", "+79803330270"),
    Smartphone("Xiaomi", "14 Ultra", "+79603350240"),
    Smartphone("Redmi", "Note 13 Pro", "+79605550220"),
    Smartphone("TECNO", "Sparc 30c", "+79955530210")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
