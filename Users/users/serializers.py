# Em: Users/users/serializers.py

from rest_framework import serializers
import re

# Importa a validação de senha que já existe no seu projeto de criação de conta
from Users.account.serializers import PasswordConfirmCreateAccountSerializer

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password_confirm = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        # Reutilizando a lógica de validação de senha forte
        # que já existe no seu serializer de criação de conta
        validator = PasswordConfirmCreateAccountSerializer()
        try:
            validator.validate_password(value)
        except serializers.ValidationError as e:
            # Re-lança a exceção para que o DRF a capture
            raise serializers.ValidationError(e.detail)
        return value

    def validate(self, data):
        # Verifica se a nova senha e a confirmação são iguais
        if data['new_password'] != data['new_password_confirm']:    
            raise serializers.ValidationError("As novas senhas não conferem.")

        return data