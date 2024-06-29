from DAOs.Dao import DAO
from entidades.Usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')
    
    def add(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.id, int)):
            super().add(usuario.id, usuario)
    
    def update(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.id, int)):
            super().update(usuario.id, usuario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
        
    
    
