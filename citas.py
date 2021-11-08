import beepy
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    while True:
        print(datetime.now().strftime("%H:%M:%S"))
        r = requests.get("https://sel.migraciones.gob.pe/web-citas-pasaporte/Citas-en-Linea-IngresoDatos")
        if r.status_code == 200:
            s = BeautifulSoup(r.text, "html.parser")
            e = s.find(id="ctl00_bodypage_lblTablaFechasDisponibles")
            fd_text = e.find("tbody").text
            if "Lima" in fd_text:
                while True:
                    beepy.beep()
                    print("HEEEEEEEEEEEEEEEEEEEEY")
            fd_list = [x.text for x in e.find("tbody").find_all("td") if x.text.startswith('L')]
            print('\n'.join(fd_list))
        time.sleep(5 * 60) # 5 minutes

if __name__ == "__main__":
    main()

