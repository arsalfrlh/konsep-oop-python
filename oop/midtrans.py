import requests
import json
from base64 import b64encode
import time

class Midtrans:
    order_id = f"Order-{int(time.time())}"
    baseUrl = "https://api.sandbox.midtrans.com/v2/charge"
    serverKey = b64encode(f"SB-Mid-server-6GJKV_t1Uh5PpGxjx-JZkPk_:".encode()).decode()
    def __init__(self, nama, email, jumlah, harga, payment_type, payment_chanel):
        self.nama = nama
        self.email = email
        self.jumlah = jumlah
        self.harga = harga
        self.payment_type = payment_type
        self.payment_chanel = payment_chanel
        
    def payment(self):
        total = self.jumlah * self.harga
        if(self.payment_type == 1):
            body = {
                "payment_type": "bank_transfer",
                "transaction_details": {
                    "order_id": self.order_id,
                    "gross_amount": total
                },
                "bank_transfer": {
                    "bank": self.payment_chanel
                },
                "customer_details": {
                    "first_name": self.nama,
                    "email": self.email
                }
            }
        elif(self.payment_type == 2):
            body = {
                "payment_type": "bank_transfer",
                "transaction_details": {
                    "order_id": self.order_id,
                    "gross_amount": total
                },
                "cstore": {
                    "store": self.payment_chanel
                },
                "customer_details": {
                    "first_name": self.nama,
                    "email": self.email
                }
            }
        else:
            body = {
                "payment_type": "gopay",
                "transaction_details": {
                    "order_id": self.order_id,
                    "gross_amount": total
                },
                "customer_details": {
                    "first_name": self.nama,
                    "email": self.email
                }
            }
        
        response = requests.post(
            url=self.baseUrl,
            headers={
                "Accept": "application/json",
                "Authorization": f"Basic {self.serverKey}",
                "Content-Type": "application/json"
            },
            # data=json.dumps(body) #data body di encode
            json=body #atau bisa data body bisa di encode langsung seperti ini
        )
        
        print(response.json())
        
nama = input("Masukan Nama: ")
email = input("Masukan Email: ")
jumlah = int(input("Masukan Jumlah: "))
harga = int(input("Masukan Harga: "))
print("=====>Payment Type<====")
print("1. Transfer Bank")
print("2. Conversi Store")
print("3. QRIS")
payment_type = int(input("Pilih Metode Pembayaran: "))

if(payment_type == 1):
    print("=====>Bank Pembayaran<====")
    print("bca = Bank Central Asia")
    print("bni = Bank Negara Indonesia")
    print("bri = Bank Rakyat Indonesia")
    print("cimb = Bank CIMB Niaga")
    payment_chanel = input("Pilih Bank: ")
elif(payment_type == 2):
    print("=====>Store Pembayaran<====")
    print("alfamart = Alfamart")
    print("indomaret = Indomaret")
    payment_chanel = input("Pilih Store: ")
else:
    payment_chanel = 3
    
midtrans = Midtrans(nama, email, jumlah, harga, payment_type, payment_chanel)
midtrans.payment()