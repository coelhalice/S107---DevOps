"#S107---DevOps" 
# Projeto de Injeção de Dependência - Monitoramento de Eventos

Este projeto demonstra o uso de injeção de dependência em Python para monitorar eventos de segurança e registrar logs.

## Estrutura

- `logger.py`: Contém a interface `Logger` e implementações concretas como `ConsoleLogger` e `FileLogger`.
- `event_monitor.py`: Serviço de monitoramento que usa o logger injetado para registrar eventos.
- `main.py`: Ponto de entrada que injeta a dependência no `EventMonitor`.

## Executando o projeto

1. Clone este repositório.
2. Execute o arquivo `main.py`:
