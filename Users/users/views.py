# Em: Users/users/views.py

from drf_spectacular.utils import extend_schema
from AppCore.basics.views.basic_views import BasicPostAPIView
from .serializers import ChangePasswordSerializer
from .business import UserBusiness

@extend_schema(tags=["Users.Management"])
class ChangePasswordPostView(BasicPostAPIView):
    """
    Endpoint para o usuário logado alterar a própria senha.
    """
    serializer_class = ChangePasswordSerializer
    success_message = "Senha alterada com sucesso."
    
    # IMPORTANTE: Não adicionamos o 'AllowAnyMixin'.
    # Isso faz com que a view use a permissão padrão do projeto,
    # que é 'IsAuthenticated', 
    # garantindo que apenas usuários logados possam acessá-la.
    
    def do_action_post(self, serializer, request):
        # O 'serializer' aqui já contém os dados validados
        old_password = serializer.get('old_password')
        new_password = serializer.get('new_password')
        
        # Pegamos o usuário que está fazendo a requisição
        current_user = request.user
        
        # Instanciamos a classe de negócio passando o usuário como 'object_instance'
        user_business = UserBusiness(object_instance=current_user)
        
        # Chamamos a lógica de negócio
        user_business.change_password(old_password, new_password)