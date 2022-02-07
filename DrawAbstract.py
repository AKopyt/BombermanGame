from abc import ABC, abstractmethod
class DrawAbstract:
    @abstractmethod
    def blitme(self):
        pass

    @abstractmethod
    def update(self):
        pass
