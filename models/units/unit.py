from abc import ABC, abstractmethod


class Unit(ABC):

    @abstractmethod
    def check_active(self):
        pass

    @abstractmethod
    def tick(self):
        pass

    @property
    @abstractmethod
    def cause_damage(self):
        pass

    @property
    @abstractmethod
    def attack_success(self):
        pass

    @property
    @abstractmethod
    def take_damage(self, damage):
        pass

    @classmethod
    def register(cls, name):
        pass

    @classmethod
    def new(cls, name):
        pass
