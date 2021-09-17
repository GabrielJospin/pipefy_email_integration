# Integração de Emails com o pipefy

---
Este projeto tem como objetivo facilitar a geração de emails para os novos membros.

## Iniciando

---
Para executar do projeto você vai precisar: <br>
    <ul>
    <li> [Python 3.8 ou superior][Python3] </li>
    <li> [Acesso ao pypefy][Pipefy] </li>
    <li> [acesso ao Admin do Drive][Admin]</li>
    </ul>
    
## Desenvolvimento

---
Para desenvolvimento, basta criar uma nova branch e clonar o projeto do GitHub num diretório de sua preferência;

## Para rodar

---
Você deve seguir os seguintes passos: <br>
    <ol>
    <li> clonar o projeto em um repositório a sua escolha</li>
    <li> salvar um .xlsx no diretório: 'databases' com o nome 'emailSintese.xlsx'</li>
    <li> pelo terminal ou outro método de sua preferência, rodar o na raiz do projeto main.py </li>
    <li> subir o emailSintese.csv em [Google Admin][Admin] >> Usuários>> Getenciar>>'Atualizar usuários em massa'</li>
    <li> subir o membros@sintesejr.com.br.csv em [Google Admin][Admin] >> Grupos>> Membros>>'Fazer upload em massa'</li>
    </ol>
P.S.: Os novos memros terão que logar com o email escolhido e a senha seu CPF no formato XXX.XXX.XXX-XX e alterar a senha
no primeiro login

## Como deve ser a tabela do Pipefy?

---
A tabela é obtida exportando um dashboard (dentro da pagina de Reports), recomendo fortemente criar um novo dashboard 
filtrando por contem email sintese. Sua tabela deve <b> Obrigatóriamente </b> conter:<br>
    <ol>
    <li> Uma coluna chamada Title com o nome completo do membro</li>
    <li> Uma coluna chamada Email Síntese com o novo Email do membro</li>
    <li> Este email deve ser @Sintesejr.com.br !!! </li>
    <li> Uma Coluna chamada CPF com o cpf dos membros</li>
    </ol>

## Metas para atualização

---
Em atualizações futuras tenho como objetivo adicionar duas novas etapas:<br>
    <ul>
    <li>Transformar em uma API compatível com o Pipefy, já vi que é possível e ajudará a puxar os dados de forma automática</li>
    <li>Integrar com o google cloud e automaticamente adicionar os membros</li>
    </ul>
Embora ambas as etapas sejam possíveis, demandaria longo tempo e recursos ainda não disponíveis para a síntese, mas nada
impede de serem feitos num futuro próximo. Os recursos que falam é basicamente um integração com o Google cloud, o que 
acho que é pago, e um servidor para armazenar estes recursos como API, pois é reqerido pelo pipefy, aleḿ de uma longa leitura
da documentação de API's <br>

Enfim a parte fácil já foi concluida, o que economzaria tempo. Falta uma parte bastante complexa mas que acabaria com esta
atividade para futuros membros de GP

## Criado por:

---
[Gabriel Medeiros Jospin][Git] ou Frodo


[Python3]: https://www.python.org/downloads/release/python-380/
[Pipefy]: https://app.pipefy.com
[Admin]: https://admin.google.com
[Git]: https://github.com/GabrielJospin