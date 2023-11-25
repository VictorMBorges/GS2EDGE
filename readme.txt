Hoje em dia, estamos lidando com desafios consideráveis no que diz respeito ao acesso à saúde, particularmente para aqueles que vivem em regiões distantes 
ou que possuem mobilidade limitada. A identificação precoce de questões de saúde é frequentemente restrita, resultando em diagnósticos atrasados e custos 
hospitalares altos que poderiam ser prevenidos. Essa deficiência no acompanhamento constante dos sinais vitais impede uma administração proativa das condições 
de saúde, afetando diretamente a qualidade de vida dos pacientes.

A nossa solução para o problema proposto foi desenvolver um sistema de monitoramento de sinais vitais. Este sistema é capaz de coletar e analisar dados vitais 
dos pacientes em tempo real, fornecendo informações cruciais para a equipe médica. As informações coletadas são disponibilizadas em uma tabela no tago.io, uma 
plataforma de análise de dados em nuvem. Esta tabela permite que os profissionais de saúde visualizem e monitorem os sinais vitais dos pacientes de maneira 
eficiente e organizada.
Além disso, implementamos um recurso de alerta para notificar a equipe sempre que um novo paciente for cadastrado no sistema. Este alerta é acionado pelo ESP32, 
um microcontrolador de alto desempenho com capacidades de rede integradas.

Para executar a aplicação, devemos:

1 - Abrir o arquivo flows no NODE-RED, para realizar o tratamento dos dados enviados;
2 - Abrir o Wokwi, para receber os alertas de pacientes cadastrados;
3 - Abrir o Dashboard no TAGO.IO, para conseguir visualizar a tabela de pacientes cadastrados;
4 - Cadastrar novos pacientes no código em Python.

INFORMAÇÕES:

Repositório GitHub: https://github.com/VictorMBorges/GS2EDGE

Vídeo demonstrativo: https://youtu.be/d7tC3Vvt6VE

Circuito do Wokwi: https://wokwi.com/projects/382322286816971777

Dashboard do TAGO.IO: https://650394df1e31b40009fcb981.tago.run/dashboards/info/655e95182446c200091718eb?anonymousToken=00000000-6503-94df-1e31-b40009fcb981

Arquivos .json e .py anexados ao envio, e também disponíveis no repositório do GitHub.

Código do ESP32 disponível no arquivo ESP32.txt

Integrantes:

Pedro Guerra de Souza Freitas - RM: 99526 
Victor Montenegro Borges - RM: 98708

