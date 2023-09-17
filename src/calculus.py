import json
from typing import List, Union

class Calculus:
    """Class processing logs and visuzaling results.
    """

    def __init__(self):
        self.__new_data: List[str]  = []
        self.__raw_data: Union(List[str], None)  = None
        self.__processing_rules = {
            0: lambda index, raw_line : "Multiple de 5" if index % 5 == 0 else None,
            1: lambda index, raw_line: raw_line.replace(" ", "_") if raw_line.find("$") != -1 else None,
            2: lambda index, raw_line: raw_line if raw_line.endswith(".") else None,
            3: lambda index, raw_line: self.__manipulate_json(index, raw_line) if raw_line.startswith("{") else None,
            4: lambda index, raw_line: "Rien à afficher",
        }

    def read_lines(self, file_path: str) -> 'Calculus':
        """Reads lines from a log file.

        Args:
            file_path (str): Path to logs.

        Returns:
            Calculus: Reference to the current class object.
        """
        with open(file_path) as f:
            self.__raw_data = [line.rstrip() for line in f.readlines()]

        return self

    def __manipulate_json(self, index: int, raw_line: str) -> str:
        """Deserializes and adds pair key.

        Args:
            index (int): Line index.
            raw_line (str): Raw log contents.

        Returns:
            str: Serialized json with the pair key.
        """
        data = json.loads(raw_line)
        data["pair"] = index % 2 == 0
        serialized = json.dumps(data)
        return serialized


    def __apply_rules(self, index: int, raw_line: str, level: int) -> str:
        """Given the raw line, recursively applies processing rules.

        Args:
            index (int): Line index.
            raw_line (str): Raw log contents.
            level (int): Recursion level. 

        Returns:
            str: Processed log line.
        """
        result = self.__processing_rules[level](index, raw_line)
        
        if result is None:
            return self.__apply_rules(index, raw_line, level + 1)
        
        return result


    def process_logs(self) -> 'Calculus':
        """Iterates over log lines and applies processing rules.

        Returns:
            Calculus: Reference to the current class object.

        
        """
        if self.__raw_data is None:
            raise ValueError("No file has been read!")

        for i, raw_line in enumerate(self.__raw_data):
            self.__new_data.append(self.__apply_rules(i, raw_line, 0))

        return self
        

    def show(self):
        """Visualizes processed log data.
        """
        for line_number, new_data in enumerate(self.__new_data):
            print(f"{line_number} : {new_data}")
