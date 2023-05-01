 

<h1 align = "center">
  <img src="https://user-images.githubusercontent.com/96443415/235499885-0bfcf319-1f70-468c-8bbf-85411d078c18.png">
  <p> Programação de Socket
</h1>



## 📓 Descrição:
  **O Projeto consisti em duas aplicações (clinte, servidor), da qual a aplicação cliente se conectará ao servidor.**
  ### 💻 *Cliente:*
  - O programa cliente se conecta ao servidor;
  - Gera um número inteiro de 1 a 30;
  - Envia o número gerado para o servidor;
  - Recebe, imprimi no console e devolve o valor recebido do servidor + "FIM";
  - Fecha a conexão;
  - A aplicação cliente realiazá esse "ciclo" a cada 10 segundos;
  
  ### 🌐 *Servidor:*
  - Espera a conexão do cliente;
  - Recebe o número passado pelo clinte;
  - Se o número recebido tiver mais de 10 casas, gera e envia uma string de mesmo tamanho para o cliente;
  - Se o número recebido for menor que 10, a aplicação servidor verifica se o mesmo é par ou ímpar e envia **PAR** ou **ÍMPAR** para o cliente;
  
## 🔨 Ferramentas:  
- [Python](https://www.python.org/)

## :books: Saiba mais:
  -[O que são e como funcionam os Sockets?](https://www.linuxsolutions.com.br/sockets-o-que-e-e-como-eles-funcionam/)
  
  -[Conexão cliente/servidor.](https://techenter.com.br/o-que-e-o-modelo-cliente-servidor/)

