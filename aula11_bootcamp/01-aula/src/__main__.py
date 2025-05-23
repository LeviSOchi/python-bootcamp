import schedule
import time
from lib.classes.CsvSource import CsvSource
from lib.classes.TxtSource import TxtSource

# Função para verificar novos arquivos
def check_for_new_files():
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()

# Ativa a função check_for_new_files a cada segundo
schedule.every(10).seconds.do(check_for_new_files)

# Instância a função com os caminhos do arquivo
csv_source = CsvSource()
txt_source = TxtSource()

while True:
    # .run_pending() - Executa tudo que está agendado com o schedule
    schedule.run_pending() 
    # Faz isso a cada 1 segundo
    time.sleep(1) 





