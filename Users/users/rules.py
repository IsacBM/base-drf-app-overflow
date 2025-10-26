# Em: Users/users/rules.py

from AppCore.core.rules.rules import ModelInstanceRules

class UserRule(ModelInstanceRules):
    
    def check_old_password(self, old_password):
        """
        Verifica se a senha antiga fornecida é válida para o usuário (self.object_instance).
        """
        user = self.object_instance
        
        if not user.check_password(old_password):
            # Lança uma exceção que será capturada pela BasicPostAPIView
            self.return_exception("A senha antiga está incorreta.")
            
        return True
    