from abc import ABCMeta, abstractstaticmethod


class ObjetoInterface(ABCMeta):
    @abstractstaticmethod
    def interface():
        """Interface do meu sistema"""
