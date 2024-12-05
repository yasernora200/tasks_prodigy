from scapy.all import sniff

# دالة لمعالجة الحزم التي تم التقاطها
def packet_callback(packet):
    print(f"Packet: {packet.summary()}")  # ملخص للحزمة
    if packet.haslayer("IP"):  # إذا كانت الحزمة تحتوي على طبقة IP
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")
    
    if packet.haslayer("TCP"):
        print(f"Protocol: TCP")
        print(f"Source Port: {packet['TCP'].sport} -> Destination Port: {packet['TCP'].dport}")
    
    elif packet.haslayer("UDP"):
        print(f"Protocol: UDP")
        print(f"Source Port: {packet['UDP'].sport} -> Destination Port: {packet['UDP'].dport}")

# التقاط الحزم على الشبكة وتحليلها
def start_sniffing(interface="eth0"):
    print(f"Sniffing packets on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)  # التقاط الحزم ومعالجتها

# تحديد واجهة الشبكة (يمكنك تغييرها حسب النظام، مثل eth0 أو wlan0)
start_sniffing(interface="Wi-Fi")

