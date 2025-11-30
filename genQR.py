import qrcode

couples = {
    "c1_p1": "https://shauryanoobb.github.io/luggage-scanner/couples/c1_p1/",
    "c1_p2": "https://shauryanoobb.github.io/luggage-scanner/couples/c1_p2/",
    # ... up to couple12
}

for name, url in couples.items():
    img = qrcode.make(url)
    img.save(f"qrcodes/{name}.png")
