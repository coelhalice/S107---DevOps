from event_monitor import EventMonitor
from logger import ConsoleLogger, FileLogger

def main():
    # Injetando a dependência (logger) no EventMonitor
    logger = ConsoleLogger() # Pode trocar o ConsoleLogger por FileLogger se precisar
    monitor = EventMonitor(logger)

    # Monitorando eventos
    monitor.monitor_event("Falha de autenticação detectada")
    monitor.monitor_event("Tentativa de acesso não autorizado")

if __name__ == "__main__":
    main()
