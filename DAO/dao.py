# dao/base_dao.py
from abc import ABC, abstractmethod

class BaseDAO(ABC):
    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def read(self, entity_id):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass
