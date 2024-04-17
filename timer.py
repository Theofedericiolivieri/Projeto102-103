# importe os módulos time 
import time
  
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60) # Usando divmod para obter minutos e segundos
        timer = '{:02d}:{:02d}'.format(mins, secs) # Formatando a string do temporizador com dois dígitos para minutos e segundos
        print(timer)
        time.sleep(1) # Espera 1 segundo antes de atualizar o temporizador
        seconds -= 1
    print('Tempo Esgotado!')

seconds = int(input("Digite o tempo em segundos: "))
countdown_timer(seconds)