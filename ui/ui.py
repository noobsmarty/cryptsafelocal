import tkinter as tk
from tkinter import messagebox, filedialog

# Vigenere Cipher Encryption/Decryption Functions
def to_vigenere(plaintext, key):
    """Encrypt the plaintext using Vigenere cipher."""
    ans = ""
    key = key.lower()
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + ord(key[i % len(key)]) - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + ord(key[i % len(key)]) - 97) % 26 + 97)
    return ans

def from_vigenere(ciphertext, key):
    """Decrypt the ciphertext using Vigenere cipher."""
    ans = ""
    key = key.lower()
    for i in range(len(ciphertext)):
        ch = ciphertext[i]
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) - ord(key[i % len(key)]) - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) - ord(key[i % len(key)]) - 97) % 26 + 97)
    return ans

# Playfair Cipher Encryption/Decryption Functions
def generate_playfair_matrix(key):
    """Generate a 5x5 Playfair matrix based on the key."""
    key = "".join(key.upper().split(' '))
    key = "".join(dict.fromkeys(key))
    key = [*key]
    for i in range(65, 91):
        if chr(i) not in key and chr(i) != "J":  # Exclude "J"
            key.append(chr(i))
    return [key[i:i + 5] for i in range(0, 25, 5)]

def encode_playfair_pair(pair, matrix):
    """Encrypt a pair of characters using the Playfair cipher matrix."""
    x1, y1 = next((i, j) for i, row in enumerate(matrix) for j, ch in enumerate(row) if ch == pair[0])
    x2, y2 = next((i, j) for i, row in enumerate(matrix) for j, ch in enumerate(row) if ch == pair[1])

    if x1 == x2:  # Same row
        return matrix[x1][(y1 + 1) % 5] + matrix[x2][(y2 + 1) % 5]
    elif y1 == y2:  # Same column
        return matrix[(x1 + 1) % 5][y1] + matrix[(x2 + 1) % 5][y2]
    else:  # Rectangle swap
        return matrix[x1][y2] + matrix[x2][y1]

def decode_playfair_pair(pair, matrix):
    """Decrypt a pair of characters using the Playfair cipher matrix."""
    x1, y1 = next((i, j) for i, row in enumerate(matrix) for j, ch in enumerate(row) if ch == pair[0])
    x2, y2 = next((i, j) for i, row in enumerate(matrix) for j, ch in enumerate(row) if ch == pair[1])

    if x1 == x2:  # Same row
        return matrix[x1][(y1 - 1) % 5] + matrix[x2][(y2 - 1) % 5]
    elif y1 == y2:  # Same column
        return matrix[(x1 - 1) % 5][y1] + matrix[(x2 - 1) % 5][y2]
    else:  # Rectangle swap
        return matrix[x1][y2] + matrix[x2][y1]

def to_playfair(plaintext, key):
    """Encrypt plaintext using Playfair cipher."""
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.replace("J", "I").upper()
    digrams = []

    i = 0
    while i < len(plaintext):
        if i + 1 == len(plaintext) or plaintext[i] == plaintext[i + 1]:
            digrams.append(plaintext[i] + "X")
            i += 1
        else:
            digrams.append(plaintext[i] + plaintext[i + 1])
            i += 2

    ciphertext = "".join([encode_playfair_pair(digram, matrix) for digram in digrams])
    return ciphertext

def from_playfair(ciphertext, key):
    """Decrypt ciphertext using Playfair cipher."""
    matrix = generate_playfair_matrix(key)
    digrams = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]
    plaintext = "".join([decode_playfair_pair(digram, matrix) for digram in digrams])
    return plaintext

# GUI setup with password encryption options
class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptsafe Local")
        self.root.geometry("600x500")  # Window size for the app
        self.main_menu()

    def main_menu(self):
        """Main menu with options for password encryption."""
        self.clear_frame()
        tk.Label(self.root, text="Cryptsafe Local", font=("Helvetica", 18, "bold")).pack(pady=30)
        tk.Label(self.root, text="Choose Encryption Method for Passwords:", font=("Helvetica", 14)).pack(pady=20)

        self.method_var = tk.StringVar(value="Vigenere")
        tk.Radiobutton(self.root, text="Vigenere", variable=self.method_var, value="Vigenere", font=("Helvetica", 12)).pack()
        tk.Radiobutton(self.root, text="Playfair", variable=self.method_var, value="Playfair", font=("Helvetica", 12)).pack()

        tk.Button(self.root, text="Proceed", font=("Helvetica", 12), command=self.password_encrypt).pack(pady=20)

    def password_encrypt(self):
        """Function to handle password encryption logic based on selected method."""
        self.clear_frame()
        tk.Label(self.root, text="Enter Text for Encryption/Decryption", font=("Helvetica", 14)).pack(pady=10)
        self.input_text = tk.Text(self.root, width=60, height=10, font=("Helvetica", 12))
        self.input_text.pack(pady=10)

        tk.Label(self.root, text="Enter Key", font=("Helvetica", 12)).pack()
        self.key_entry = tk.Entry(self.root, font=("Helvetica", 12), show="*")
        self.key_entry.pack(pady=5)

        tk.Button(self.root, text="Encrypt", font=("Helvetica", 12), command=self.perform_password_encrypt).pack(pady=10)
        tk.Button(self.root, text="Decrypt", font=("Helvetica", 12), command=self.perform_password_decrypt).pack(pady=10)
        
        tk.Button(self.root, text="Save to File", font=("Helvetica", 12), command=self.save_to_file).pack(pady=10)
        tk.Button(self.root, text="Load from File", font=("Helvetica", 12), command=self.load_from_file).pack(pady=10)

        tk.Button(self.root, text="Back", font=("Helvetica", 12), command=self.main_menu).pack(pady=10)

    def perform_password_encrypt(self):
        """Encrypt the entered text using the selected password method."""
        text = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get()
        if not text or not key:
            messagebox.showwarning("Input Error", "Please enter both text and key.")
            return

        method = self.method_var.get()
        if method == "Vigenere":
            result = to_vigenere(text, key)
        elif method == "Playfair":
            result = to_playfair(text, key)

        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, result)

    def perform_password_decrypt(self):
        """Decrypt the entered text using the selected password method."""
        text = self.input_text.get("1.0", tk.END).strip()
        key = self.key_entry.get()
        if not text or not key:
            messagebox.showwarning("Input Error", "Please enter both text and key.")
            return

        method = self.method_var.get()
        if method == "Vigenere":
            result = from_vigenere(text, key)
        elif method == "Playfair":
            result = from_playfair(text, key)

        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, result)

    def save_to_file(self):
        """Save the current encrypted text to a file."""
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "No text to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        with open(file_path, "w") as f:
            f.write(text)

        messagebox.showinfo("Success", "Text saved to file.")

    def load_from_file(self):
        """Load encrypted text from a file and display it."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        with open(file_path, "r") as f:
            text = f.read()

        self.input_text.delete("1.0", tk.END)
        self.input_text.insert(tk.END, text)

    def clear_frame(self):
        """Clear the current frame before switching menus."""
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
