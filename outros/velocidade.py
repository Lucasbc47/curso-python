# Teste da velocidade da internet
import speedtest

s = speedtest.Speedtest()
print(f'Download Speed: {s.download():2.f}\nUpload Speed: {s.upload():2.f}')