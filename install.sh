echo "🔧 Installing Universal OSINT Tool on Kali Linux..."

sudo apt update && sudo apt upgrade -y

sudo apt install -y python3 python3-pip python3-venv git

python3 -m venv osint-env
source osint-env/bin/activate

pip3 install --upgrade pip
pip3 install -r requirements.txt

chmod +x real_osint_tool.py

echo "✅ Installation complete!"
echo "🚀 To run: source osint-env/bin/activate && python3 real_osint_tool.py"