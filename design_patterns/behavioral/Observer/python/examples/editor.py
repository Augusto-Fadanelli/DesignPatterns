from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def update(self, filename):
        pass


class LoggingListener(EventListener):
    # _log: File
    _message: str

    def __init__(self, log_filename, message):
        # self._log = File(log_filename)
        self._message = message

    def update(self, filename):
        # self._log.write(replace('%s', filename, message))
        pass


class EmailAlertsListener(EventListener):
    def __init__(self, email: str, message: str):
        self._email = email
        self._message = message

    def update(self, filename):
        # system.email(self._email, replace('%s', filename, message))
        pass


class EventManager:
    _listeners = {}

    def subscribe(self, event_type, listener: EventListener):
        if not event_type in self._listeners:
            line = []
            line.append(listener)
            self._listeners.update({event_type: line})
            print('deb 1:')
            self.print_listeners()
        else:
            line = self._listeners[event_type]
            line.append(listener)
            self._listeners.update({event_type: line})
            print('deb 2:')
            self.print_listeners()

    def unsubscribe(self, event_type, listener: EventListener):
        line = self._listeners[event_type]
        line.remove(listener)
        self._listeners.update({event_type: line})

    def notify(self, event_type, data):
        for listener in self._listeners[event_type]:
            listener.update()

    # debug
    def print_listeners(self):
        print(f'\t{self._listeners}')


class Editor:
    # _file: File

    def __init__(self):
        self.events = EventManager()

    def openFile(self, path):
        # self._file = File(path)
        # self.events.notify("open", file.name)
        pass


if __name__ == '__main__':
    a1 = EventManager()
    l1 = LoggingListener('log1.txt', 'Olá Mundo')
    l2 = LoggingListener('log2.txt', 'Hello World')
    l3 = EmailAlertsListener('example1@gmail.com', 'Boa tarde')
    l4 = EmailAlertsListener('example2@hotmail.com', 'Boa noite')

    a1.subscribe('Save file', l1)
    a1.subscribe('Save file', l2)
    a1.subscribe('Open file', l1)
    a1.subscribe('Open file', l3)
    a1.subscribe('Send email', l1)
    a1.subscribe('Send email', l2)
    a1.subscribe('Send email', l3)
    a1.subscribe('Send email', l4)
    a1.unsubscribe('Save file', l2)
    a1.print_listeners()
    a1.unsubscribe('Send email', l3)
    a1.print_listeners()
