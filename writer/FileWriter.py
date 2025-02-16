
from IWriter import IWriter
class FileWriter(IWriter):
    def send_data(self, data: str) -> None:
        with open("Data_File.txt", "a") as file:
            file.write(data)