from speedtest import *
s = Speedtest()
print("Internet speed is testing. Please wait...")
try:
 upload_speed = s.upload()/10**6
 download_speed = s.download()/10**6
 ping = s.results.ping
 print(f"Download Speed : {download_speed:.2f} Mbps")
 print(f"Upload Speed   : {upload_speed:.2f} Mbps")
 print(f"Ping           : {ping:.2f} ms")
except Exception as e:
        print("An error occurred while testing speed.")
        print("Error:", e)
