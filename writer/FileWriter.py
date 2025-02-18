from writer.IWriter import IWriter

class FileWriter(IWriter):
    def send_data(self, data: str, machine_name: str) -> None:
        data = machine_name + '\n' + data
        try:
            with open("Data_File.txt", "a") as file:
                file.write(data)
        except FileNotFoundError:
            raise FileNotFoundError("File Not Found")
