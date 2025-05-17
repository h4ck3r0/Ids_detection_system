from scapy.all import sniff, IP

def start_sniffing(callback):
    sniff(prn=callback, filter="ip", store=False)