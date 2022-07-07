from abc import ABC, abstractmethod


class Abstract_JSON(ABC):
    @abstractmethod
    def reset_json_by_database(self):
        """Reset the json file in order by clearing the json file"""
        pass

    @abstractmethod
    def print_all_data_by_json(self):
        """Print all data in json file to console."""
        pass
