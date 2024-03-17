from abc import ABC, abstractmethod
from socket import socket


class BaseWriter(ABC):
    @abstractmethod
    def write(self, contents: bytearray):
        pass

class FileWriter(BaseWriter):
    def write(self, contents: bytearray):
        with open("random_file.txt", "w") as output_file:
                output_file.write(contents)

class NetworkWriter(BaseWriter):

    def __init__(self) -> None:
         super().__init__()
         self.socket = object()

    def write(self, contents: bytearray):
        self.socket.write(contents)

file_writer = FileWriter()
file_writer.write(b'hello world')

network_writer = NetworkWriter()
network_writer.write(b'hello world')