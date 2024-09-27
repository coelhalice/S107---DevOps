class EventMonitor:
    def __init__(self, logger):
        # O logger é injetado via construtor
        self.logger = logger

    def monitor_event(self, event):
        # Simulação de monitoramento de evento
        self.logger.log(f"Evento monitorado: {event}")
