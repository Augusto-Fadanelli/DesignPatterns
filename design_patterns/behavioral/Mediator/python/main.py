
from chatRoom import ChatRoom
from person import Person

chat = ChatRoom()

joao = Person("Joao", chat)
maria = Person("Maria", chat)
luan = Person("Luan", chat)
pedro = Person("Pedro", chat)
#pedro = Person("Pedro", chat)

chat.add(joao)
chat.add(maria)
chat.add(luan)
chat.add(pedro)
#chat.add(pedro)

joao.broadcast("Ola mundo")
maria.broadcast("Sai disso de 'Ola mundo' kkkk")
pedro.broadcast("Fui adicionado ao chat")
luan.broadcast("Estou no broadcast")

#NOTA: 
print()
#pedro.send_direct('Joao', 'Ola Maria, tudo bem?')
#joao.send_direct('Pedro', 'Bem, e você?')

