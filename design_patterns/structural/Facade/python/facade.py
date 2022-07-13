class Subsystem1:
    def operation1(self):
        return 'Subsystem1: Ready!'

    def operationN(self):
        return 'Subsystem1: Go!'

class Subsystem2:
    def operation1(self):
        return 'Subsystem2: Get ready!'

    def operationZ(self):
        return 'Subsystem2: Fire!'

class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2):
        self._subsystem1 = subsystem1 or Subsystem1
        self._subsystem2 = subsystem2 or Subsystem2

    def operation(self):
        results = []
        results.append('Facade initializes subsystems:')
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append('Facade orders subsystems to perform the action:')
        results.append(self._subsystem1.operationN())
        results.append(self._subsystem2.operationZ())
        return '\n'.join(results)

def clientCode(f: Facade):
    print(f.operation())

if __name__ == '__main__':
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()

    f = Facade(subsystem1, subsystem2)
    clientCode(f)