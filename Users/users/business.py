from AppCore.core.business.business import ModelInstanceBusiness
from .rules import UserRule

class UserBusiness(ModelInstanceBusiness):
    
    def create_manager_profile(self, bio='', avatar=''):
        """
        Cria um perfil de gestor para o usuário.
        
        Args:
            bio: Biografia do perfil
            avatar: Avatar do perfil
            
        Returns:
            Profile: O perfil criado ou None se já existir
        """
        return self.object_instance.helper.add_profile(
            profile_type='manager',
            bio=bio,
            avatar=avatar
        )
    
    def get_active_profiles(self):
        """Retorna apenas os perfis ativos do usuário"""
        return self.object_instance.profiles.filter(status=1)

    # --- ADICIONE ESTE NOVO MÉTODO ---
    def change_password(self, old_password, new_password):
        """
        Orquestra a mudança de senha do usuário (self.object_instance).
        """
        try:
            # 1. Validação (Camada de Rules)
            rule = UserRule(object_instance=self.object_instance)
            rule.check_old_password(old_password)
            
            # 2. Execução (Lógica de Negócio)
            user = self.object_instance
            user.set_password(new_password) # Define a nova senha (criptografada)
            user.save() # Salva o usuário no banco
            
        except self.exceptions_handled as e:
            raise e