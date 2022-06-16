from pypresence import Presence
import time
import psutil

client_id = '986284838443155508'
RPC = Presence(client_id)
RPC.connect()

start_time = time.time()

while True:

    for proc in psutil.process_iter():
        
        match proc.name().lower():
            
            case "knightonline.exe":
                data = {"large_image": "knight_online","details": "www.nttgame.com","buttons": [{"label": "Play","url": "https://nttgame.com"}],"start": int(start_time)}
                break
                
            case _:
                data = None
            
    if data:
        RPC.update(**data)
    else:
        start_time = time.time()
        RPC.clear()

    time.sleep(10)
