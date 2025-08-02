import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = entry_sender.get()
    password = entry_password.get()
    receiver_email = entry_receiver.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END)

    # Basic validation
    if not sender_email or not password or not receiver_email or not subject or not body.strip():
        messagebox.showwarning("Warning", "⚠️ All fields are required.")
        return

    # Compose the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        # Sending email via Gmail SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        messagebox.showinfo("Success", "✅ Email sent successfully!")

        # Clear inputs after sending
        entry_receiver.delete(0, tk.END)
        entry_subject.delete(0, tk.END)
        text_body.delete("1.0", tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"❌ Failed to send email:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("📧 Email Sender")
root.geometry("430x520")
root.configure(bg="#e0f7fa")
root.resizable(False, False)

# Title label
tk.Label(root, text="📧 Simple Email Sender", font=("Helvetica", 16, "bold"), bg="#e0f7fa", fg="#00796B").pack(pady=10)

# Sender Email
tk.Label(root, text="Sender Email:", bg="#e0f7fa").pack(pady=(5, 2))
entry_sender = tk.Entry(root, width=45)
entry_sender.pack()

# Password
tk.Label(root, text="App Password:", bg="#e0f7fa").pack(pady=(10, 2))
entry_password = tk.Entry(root, show="*", width=45)
entry_password.pack()

# Recipient Email
tk.Label(root, text="Recipient Email:", bg="#e0f7fa").pack(pady=(10, 2))
entry_receiver = tk.Entry(root, width=45)
entry_receiver.pack()

# Subject
tk.Label(root, text="Subject:", bg="#e0f7fa").pack(pady=(10, 2))
entry_subject = tk.Entry(root, width=45)
entry_subject.pack()

# Message Body
tk.Label(root, text="Message Body:", bg="#e0f7fa").pack(pady=(10, 2))
text_body = tk.Text(root, width=45, height=10)
text_body.pack()

# Send Button
tk.Button(root, text="Send Email", command=send_email, bg="#00796B", fg="white", font=("Helvetica", 11), width=20).pack(pady=20)

root.mainloop()
