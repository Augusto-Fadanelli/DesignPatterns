
from chatRoom import ChatRoom
from person import Person

chat = ChatRoom()

joao = Person("Joao", chat)
maria = Person("Maria", chat)
luan = Person("Luan", chat)
pedro = Person("Pedro", chat)

chat.add(joao)
chat.add(maria)
chat.add(luan)
chat.add(pedro)
#Pedro não foi adicionado ao chat

joao.broadcast("Ola mundo")
maria.broadcast("Ola para todos")
pedro.broadcast("Não fui adicionado ao chat")

#NOTA: MEU DIRECT NÃO FUNCIONAR ;-;
print()
pedro.send_direct('Joao', 'Ola Maria, tudo bem?')
joao.send_direct('Pedro', 'Bem, e você?')

