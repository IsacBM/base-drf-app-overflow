EMAIL_CREATE_ACCOUNT = """
<html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Código P/ Nova Conta</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f4f4f4;
            }
            .email-container {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                border: 1px solid #e0e0e0;
                max-width: 600px;
                margin: 40px auto;
            }
            h2 {
                text-align: center;
                color: #333;
            }
            .code-container {
                background-color: #4CAF50;
                color: white;
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                padding: 15px;
                border-radius: 8px;
                margin: 20px auto;
                max-width: 150px;
            }
            .footer {
                text-align: center;
                margin-top: 20px;
                font-size: 14px;
                color: #666;
            }
            .footer a {
                color: #4CAF50;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <h2>Criação de Conta</h2>
            <p>Olá,</p>
            <p>Recebemos a requisição para criar uma conta com este email. Para validar a criação, use o código abaixo:</p>
            
            <div class="code-container">
            %s
            </div>
            
            <p>Se você não solicitou a criação da conta, por favor, ignore este email.</p>
            
            <div class="footer">
                Sistema de Gestão de Usuários<br>
            </div>
        </div>
    </body>
</html>
"""

EMAIL_PASSWORD_RESET_ACCOUNT = """
<html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Código P/ Redefinição de Senha</title>
        <style>
            :root {
                --color-roxo-background: #13102c;
                --color-roxo-box: #161424;
                --color-roxo-claro: #161530;
                --color-roxo-escuro: #161424;
                --color-roxo-terminal: #0e0c1d;
                --color-roxo-editor: #111023;
                --color-white: #ffffff;
                --color-icones: #6325CE;
                --color-black: #000000;
                --color-text-placeholder: #686868;
                --color-cinza-icon:#7B7B7B;
                --color-botoes: #1FC47A;
                --color-green-black: #19945c;
                --color-equipe-caisTech:#25D366;
                --color-white-secondary: #fff2cc;
                --color-red-icon: #E60019;
                --color-red:#DB4437;
                --color-red-escuro: #7C0000;
                --color-blue: #0099FF;
                --color-pink: #B70089;
                --color-yellow:#FBBC05;
                --color-cian:#17A2B8;
                --color-cian-escuro:#007F93;
                --color-lilas:#738BD7;
                --color-lilas-escuro:#245FAD;
                --first-color: #4723D9;
                --first-color-light: #AFA5D9;
                --white-color: #F7F6FB;
            }
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                background-color: var(--color-roxo-background);
            }
            .email-container {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                border: 3px solid var(--color-icones);
                max-width: 600px;
                margin: 40px auto;
            }
            h2 {
                text-align: center;
                color: #333;
            }
            .code-container {
                background-color: #3a2888;
                color: white;
                font-size: 24px;
                font-weight: bold;
                text-align: center;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 8px 8px 15px rgba(107, 20, 161, 0.2);
                margin: 20px auto;
                max-width: 150px;
            }
            .footer {
                text-align: center;
                margin-top: 20px;
                font-size: 14px;
                color: #666;
                font-weight: bold;
            }
            .footer a {
                color: #3a2888;
                text-decoration: none;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <h2>Redefinição de Senha</h2>
            <p>Olá,</p>
            <p>Recebemos a requisição para redefinir a senha da sua conta. Para validar a solicitação, use o código abaixo:</p>

            <div class="code-container">
            %s
            </div>

            <p>Se você não solicitou a redefinição de senha, por favor, ignore este email.</p>
            
            <div class="footer">
                Overflows &copy; Todos os Direitos Reservados - 2025<br>
            </div>
        </div>
    </body>
</html>
"""