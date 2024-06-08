def hitung_huruf_besar(kalimat):
    jumlah_huruf_besar = 0
    for kar in kalimat :
        if kar.isupper():
            jumlah_huruf_besar =+ 1
    return jumlah_huruf_besar
