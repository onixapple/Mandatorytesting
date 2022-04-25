from generator import Generator


class address:
    def __init__(self) -> None:
        self.street = Generator.genStreet()
        self.number = Generator.genStreetNumber()
        self.floor = Generator.genFloor()
        self.door = Generator.genDoorNumber()
        townAndCode = Generator.genTownAndPostalCode()
        self.town = townAndCode['Town']
        self.zipCode = townAndCode['Zip Code']