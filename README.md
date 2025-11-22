<p align="center">
  <img src="https://img.shields.io/badge/Speeping-v1.0.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Linux-Terminal--Tool-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Open--Source-Yes-orange?style=for-the-badge" />
</p>

<h1 align="center">🔥 Speeping — Internet Speed CLI Tool 🔥</h1>

<p align="center">
A fast and simple command-line tool to test your internet speed instantly using:
<br/><br/>
<b><code>speeping test</code></b>
</p>

---

# 🚀 About Speeping

**Speeping** is a lightweight and clean CLI tool for Linux that performs a full internet speed test directly from your terminal.

It displays:

- Ping  
- Download Speed  
- Upload Speed  

No virtual environments.  
No complex setup.  
Just install once and run:

speeping test

yaml
Copy code

---

# 🎨 ASCII Banner

███████╗██████╗ ███████╗███████╗██████╗ ██╗██████╗ ███████╗██╗███╗ ██╗ ██████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝██║████╗ ██║██╔════╝
███████╗██████╔╝█████╗ █████╗ ██║ ██║██║██████╔╝█████╗ ██║██╔██╗ ██║██║ ███╗
╚════██║██╔══██╗██╔══╝ ██╔══╝ ██║ ██║██║██╔══██╗██╔══╝ ██║██║╚██╗██║██║ ██║
███████║██║ ██║███████╗███████╗██████╔╝██║██║ ██║███████╗██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝ ╚═╝╚══════╝╚══════╝╚═════╝ ╚═╝╚═╝ ╚═╝╚══════╝╚═╝╚═╝ ╚═══╝ ╚═════╝

yaml
Copy code

---

# 📦 Installation

Clone the tool:

```bash
git clone https://github.com/asrasser/Speeping.git
cd Speeping
Install required package:

bash
Copy code
sudo apt install -y speedtest-cli
Make the tool globally available:

bash
Copy code
chmod +x speeping.py
sudo cp speeping.py /usr/local/bin/speeping
⚡ Usage
Run a full internet speed test:

bash
Copy code
speeping test
Example output:

markdown
Copy code
[+] Running internet speed test...

------ Speeping Results ------
Ping     : 22 ms
Download : 92.34 Mbps
Upload   : 18.44 Mbps
------------------------------
📁 Project Structure
Copy code
Speeping/
│
├── speeping.py
└── README.md
👑 Author
Made with ❤️ by Aser
https://github.com/asrasser

yaml
Copy code
