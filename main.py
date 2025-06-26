import pywifi
from pywifi import const
def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    print("Scanning for Wifi Networks")
    import time
    time.sleep(3)
    results = iface.scan_results()

    unique_networks ={}

    

    for network in results:
        if not network.ssid:
            continue
        if network.ssid not in unique_networks:
            unique_networks[network.ssid] = network
        else:
            if network.signal > unique_networks[network.ssid].signal:
                unique_networks[network.ssid] = network

    print(f"{'SSID':<30}{'Singnal':<10}{'Security'}")
    print("-"*60)

    for ssid,network in unique_networks.items():
        security = "OPEN" if len (network.akm) == 0 else "SECURED"
        print(f"{ssid:<30}{network.signal:<10}{security}")
    
    if unique_networks:
        best_network = max(unique_networks.values(), key=lambda x: x.signal)
        print(f"\n Recommended Network: {best_network.ssid} (Signal: {best_network.signal})")

    else:
        print("\n No network found")


if __name__ =="__main__":
    scan_networks()