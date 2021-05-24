.. Banco documentation master file, created by
   sphinx-quickstart on Mon May 24 11:36:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bem-Vindo a Documentação do Banco!
=================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

:Arquivo: main_servidor.py
  
   Arquivo principal do Servidor, responsavel por receber todos os dados
   do Cliente e fazer a conexao com os arquivos do Banco.

   :Logica:
      Recebe um codigo do Cliente, que com esse codigo sera feito a execucao das funcoes 
      expecificas 
   :Mensagem==1: 
      Ira Criar a conta
   :Mensagem==2: 
      Verifica se a conta recebida existe, e envia seus dados para o Cliente
   :Mensagem==3: 
      Faz o deposito
   :Mensagem==4: 
      Envia o Saldo para o Cliente
   :Mensagem==5: 
      Faz o saque da conta
   :Mensagem==6: 
      Faz a transferencia entre contas
   :Mensagem==7: 
      Envia o historico da conta para o Cliente 


:Arquivo: main_cliente.py
   
   Arquivo principal que e responsavel pela exibicao das telas dos do sistema e por mandar os 
   dados recebidos do usuario para o servidor.

   .. py:function:: abrirTelaBanco(self)
      
      Funcao responsavel pela realizacao do login do usuario no sistema
      
      :Condicao 1: 
         Verifica se o numero da conta e o cpf são vazios e envia o código com a opcao para
         o servidor verificar a aconta.
      :Condicao 2: 
         Envia numero da conta e o cpf do cliente para o servidor verificar a aconta.        
      :Condicao 3: 
         Se a conta existir o usuario e direcionado para a tela do banco
  
   .. py:function:: abrirTelaHistorico(self)
        
      Funcao responsavel pela exibicao do historico de movimentacoes na conta do usuario.
        
      :Logica: 
         Utiliza lacos de repeticao para percorrer as listas de: deposito, saque e transferencia
         recebidas do servidor, e exibi-las na tela do historico.

   .. py:function:: abrirTelaCadastro(self)
        
      Funcao responsavel por chamar a tela de cadastro.
   
   .. py:function:: abrirTelaSaldo(self)
        
      Funcao responsavel pela exibicao do saldo da conta do usuario.
        
      :Logica: 
         Envia o codigo para o servidor, com o requerimento do saldo da conta.
   
   .. py:function:: abrirTelaTransferir(self)
        
      Funcao responsavel por chamar a tela de transferencia.
   
   .. py:function:: abrirTelaDeposito(self)
        
      Funcao responsavel por chamar a tela de deposito.

   .. py:function:: abrirTelaSaque(self)
      
      Funcao responsavel por chamar a tela de saque.
    
   .. py:function:: abrirTelaHome(self)
        
      Funcao responsavel por chamar a tela principal.

   .. py:function:: botaoCadastra(self)
      
      Funcao responsavel por ler os dados do usuario para criar a conta que ira ser salva no banco.
      
      :Condicao 1: 
         Verifica se os campos sao vazios.

      :Condicao 2: 
         Envia os dados para o servidor, para serem salvos.

      :Condicao 3: 
         Exibe uma mensagem de erro.

   .. py:function:: botaoDepositar(self)
       
      Funcao responsavel por enviar um valor para depósito em uma conta.
      
      :Logica: 
         Ler o valor de deposito do usuario e enviar para o servidor. 
   
   .. py:function:: botaoSacar(self)
      
      Funcao responsavel por fazer a subtracao do valor de saque na conta do usuario.
      
      :Logica: 
         Ler o valor de saque e compara com o valor do saldo da conta, em seguida envia
         o mesmo para que o servidor faca a alteracao do valor do saldo.
   
   .. py:function:: botaoTransferir(self)
      
      Funcao responsavel por fazer a transferencia de um determinado valor de uma conta para outra.
      
      :Logica: 
         Ler o numero da conta de destina e o valor a ser transferido, faz a verificacao do valor 
         a ser transferido com o valor do saldo, envia-os para que o servidor faca as devidas 
         mudancas.

   .. py:function:: botaoFecharPrograma(self)
        
      Funcao responsavel encerrar a execucao do proggrama.
   
:Arquivo: banco.py
   
   Arquivo que contem funcoes que envolvem o Banco

   .. py:class:: Banco()

      Classe que e responsavel por armazenar os dados das contas

      .. py:function:: criar_conta(self, nome, sobrenome, cpf, numero)
         
         Funcao que cria uma conta e insere na lista de contas do banco 
         
         :param nome: string
            Nome do cliente
         :param sobrenome: string
            Sobrenome do cliente
         :param cpf: string
            Cpf do Cliente
         :param numero: string
            Numero da Conta criada      
      
      .. py:function:: verificar_conta(self, numero, cpf)
      
         Funcao que verifica se uma conta existe
         
         :param numero: string
            Numero da Conta criada
         :param cpf: string
            Cpf do Cliente
         :return:
            Vai retornar True se caso existir a conta, se não, retorna False 

      .. py:function:: buscar_conta(self, numero)
      
         Funcao que busca uma conta
         
         :param numero: string
            Numero da Conta criada
         :return:
            Vai retornar uma conta que tiver o numero passado por parametro  
      
      
Índices e tabelas
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
