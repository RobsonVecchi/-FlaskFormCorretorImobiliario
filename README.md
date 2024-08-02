# Flask Form para um Corretor Imobiliário – Automatizando captação de leads

Uma aplicação web desenvolvida com Flask para um corretor imobiliário. Este projeto fornece um formulário de contato que permite aos clientes enviar consultas e solicitações diretamente para o corretor. O sistema envia notificações por e-mail e redireciona os usuários para uma página de agradecimento após o envio bem-sucedido do formulário.

## Veja o site
O deploy foi feito através do Herokuapp [nesse link](https://mighty-dusk-69443-5cf8552a945b.herokuapp.com/) para você visualizar as funcionalidades descritas abaixo. Não é mais necessário realizar os próximos passos para ver o app funcionando, mas sim para rodá-lo através do terminal.

## Funcionalidades

- **Formulário de Contato**: Coleta informações sobre serviços de interesse, cidade, nome, e-mail e mensagem.
- **Envio de E-mail**: Envia um e-mail com as informações do formulário para um endereço configurado.
- **Página de Agradecimento**: Redireciona o usuário para uma página de agradecimento após o envio do formulário.

## Requisitos

- Python 3.x
- Flask
- Biblioteca `smtplib` para envio de e-mails
- Biblioteca `email` para manipulação de e-mails

## Instalação
1. Clone o Repositório;
2. Crie um Ambiente Virtual (opcional, mas recomendado);
3. Instale as Dependências (Flask);
4. Crie o Arquivo de Configuração (Você precisa criar um arquivo chamado `config.txt` no mesmo diretório do código com as seguintes variáveis:

   EMAIL_USER=seu-email@gmail.com
   EMAIL_PASS=sua-senha)

A entrega do formulário acontecerá para o e-mail apontado aqui!

## Executando o Projeto

Inicie a Aplicação e execute o script Python para iniciar a aplicação Flask (python app.py)
O aplicativo será iniciado e você pode acessá-lo no seu navegador em [http://127.0.0.1:5000](http://127.0.0.1:5000).
Obs.: Essa é a versão pré-entrega, no modo Debug, para que você possa manipular o arquivo com facilidade.
Se você não tem Python, os arquivos "Visual1" e "Visual2" são Prints do site para apreciação.

## Estrutura do Projeto

- **app.py**: Código principal da aplicação Flask.
- **templates/**: Contém os arquivos HTML (`index.html` e `thank_you.html`).
- **static/**: Contém arquivos estáticos como CSS e JavaScript (`styles.css` e `script.js`).
- **config.txt**: Arquivo de configuração para credenciais de e-mail (não incluído no repositório por questões de segurança. Para preenchê-lo, siga as instruções acima.).

## Contato

Se tiver dúvidas ou precisar de ajuda, entre em contato pelo e-mail: robson.t.vecchi@gmail.com.
