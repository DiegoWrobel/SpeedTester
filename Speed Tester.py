# Medidor de Velocidad
# pip install speedtest-cli
import speedtest as st

server = st.Speedtest()
server.get_best_server()        # Mejor servidor

down = server.download()        # Prueba velocidad de bajada
down = down / 1000000
print(f"Bajada : {down} Mb/s")

up = server.upload()
up = up / 1000000
print(f"Subida : {up} Mb/s")     # Velocidad de subida

ping = server.results.ping      # Ping
print(f"Ping : {ping}")