from model.Usuario import Usuario
class User(object):

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id
    
    @staticmethod
    def obtener_usuarios():
        listaUsuariosRpta = []
        listaUsuarios = Usuario.obtener_usuarios_jwt()

        for user in listaUsuarios:
            obj = User(user[0], user[1], user[2])
            listaUsuariosRpta.append(obj)
        return listaUsuariosRpta
    
users = User.obtener_usuarios()

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
