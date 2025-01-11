import tkinter as tk
from tkinter import messagebox
import requests
import threading

# Discord: Ech0blade

def send_webhook():
    webhook_url = webhook_entry.get()
    message_content = message_entry.get("1.0", tk.END).strip()
    count = count_entry.get()
    sender_name = name_entry.get().strip()
    sender_avatar = avatar_entry.get().strip()

    if not webhook_url or not message_content or not count.isdigit():
        messagebox.showerror("Hata", "Tüm alanları doğru bir şekilde doldurunuz!")
        return
    
    count = int(count)
    if count <= 0:
        messagebox.showerror("Hata", "Mesaj sayısı en az 1 olmalıdır!")
        return


    def send_requests():
        headers = {"Content-Type": "application/json"}
        payload = {
            "content": message_content,
            "username": sender_name if sender_name else None,
            "avatar_url": sender_avatar if sender_avatar else None
        }
        for i in range(count):
            response = requests.post(webhook_url, json=payload, headers=headers)
            if response.status_code == 204:
                status_label.config(text=f"{i+1}/{count} Mesaj gönderildi.")
            else:
                messagebox.showerror("Hata", f"Mesaj gönderilemedi! Hata: {response.status_code}")
                break
        status_label.config(text="Gönderim tamamlandı.")


    threading.Thread(target=send_requests).start()


root = tk.Tk()
root.title("Webhook Gönderici")
root.geometry("400x500")
root.resizable(False, False)


tk.Label(root, text="Webhook URL:", font=("Arial", 12)).pack(pady=10)
webhook_entry = tk.Entry(root, width=50, font=("Arial", 10))
webhook_entry.pack(pady=5)

tk.Label(root, text="Mesaj İçeriği:", font=("Arial", 12)).pack(pady=10)
message_entry = tk.Text(root, width=45, height=5, font=("Arial", 10))
message_entry.pack(pady=5)

tk.Label(root, text="Mesaj Sayısı:", font=("Arial", 12)).pack(pady=10)
count_entry = tk.Entry(root, width=10, font=("Arial", 10))
count_entry.pack(pady=5)

tk.Label(root, text="Gönderici Adı (İsteğe Bağlı):", font=("Arial", 12)).pack(pady=10)
name_entry = tk.Entry(root, width=50, font=("Arial", 10))
name_entry.pack(pady=5)

tk.Label(root, text="Gönderici Profil Resmi URL (İsteğe Bağlı):", font=("Arial", 12)).pack(pady=10)
avatar_entry = tk.Entry(root, width=50, font=("Arial", 10))
avatar_entry.pack(pady=5)

send_button = tk.Button(root, text="Gönder", font=("Arial", 12), bg="lightgreen", command=send_webhook)
send_button.pack(pady=20)


status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=10)


root.mainloop()
