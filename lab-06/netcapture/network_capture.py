import subprocess
from scapy.all import *

def get_interfaces():
    result = subprocess.run(["netsh", "interface", "show", "interface"],
                            capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = [line.split()[3] for line in output_lines if len(line.split()) >= 4]
    return interfaces

def packet_handler(packet):
    if packet.haslayer(Raw):
        print("Captured Packet:")
        print(str(packet))

# Lấy danh sách các giao diện mạng
interfaces = get_interfaces()

# In danh sách giao diện mạng để người dùng lựa chọn
print("Danh sách các giao diện mạng:")
for i, iface in enumerate(interfaces, start=1):
    print(f"{i}. {iface}")

# Lựa chọn giao diện mạng từ người dùng
choice = int(input("Chọn một giao diện mạng (nhập số): "))
selected_iface = interfaces[choice - 1]

# Bắt gói tin trên giao diện mạng được chọn
sniff(iface=selected_iface, prn=packet_handler, filter="tcp")