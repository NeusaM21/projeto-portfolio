![Capa do Projeto](capa_nova.png)

# Bot de E-mails Automáticos com Python

Automatize o envio de e-mails personalizados com Python e planilhas Excel. Ideal para cobranças, notificações e lembretes de forma automatizada.

## Funcionalidades

- 📊 Leitura de planilha com dados dos clientes  
- ✉️ Criação de mensagens personalizadas com nome, valor e vencimento  
- 📬 Envio de e-mails automáticos via Gmail com autenticação segura  
- 🔒 Armazenamento protegido de credenciais com arquivo `.env`  
- 🧩 Código organizado, comentado e fácil de adaptar a outros contextos  

## Requisitos

- Python 3.x  
- Bibliotecas: `pandas`, `openpyxl`, `schedule`, `smtplib`, `email`  

## Como usar

1. Crie um arquivo `.env` com seu e-mail e a senha de aplicativo do Gmail  
2. Preencha a planilha `clientes.xlsx` com os dados dos destinatários  
3. Execute o script `email_bot.py`  

## Exemplo da planilha `clientes.xlsx`:

| Nome  | Email           | Valor | Vencimento  |
|-------|------------------|--------|--------------|
| João  | joao@email.com   | 150.0  | 01/07/2025   |
| Maria | maria@email.com  | 200.0  | 03/07/2025   |
| Pedro | pedro@email.com  | 300.0  | 05/07/2025   |

## Segurança com `.env`

Este projeto usa um arquivo `.env` para armazenar dados sensíveis, como e-mail e senha de aplicativo.  
O arquivo está incluído no `.gitignore`, portanto **não será enviado ao GitHub** por segurança.

### Exemplo de `.env`

```env
EMAIL_REMETENTE=seuemail@gmail.com
SENHA_DO_APP=sua_senha_de_aplicativo
```

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais informações.

## Contato

Feito com 💙 por [MrsM21](https://github.com/MrsM21)
📧 Email: ne2101@hotmail.com

