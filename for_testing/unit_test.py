import io

buf = io.BytesIO()
img.save(buf, format='PNG')
buf.seek(0)

rs = requests.post(url, files={'file': ('image.png', buf, 'image/png')})