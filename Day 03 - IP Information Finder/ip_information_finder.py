import requests
import ipaddress
import time
def get_ip_information(url):
    try:
        response = requests.get(url, timeout=5).json()
        if response["status"] == "success":
            return f"Ip Address : {response['query']}, Country : {response['country']}, City : {response['city']}, ISP : {response['isp']}"
        else:
            return None
    except requests.exceptions.Timeout:
        print("Error: Timeout occurred while fetching data.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

while True:
    print("""
    IP Address Finder

    1. Get my current IP information
    2. Get another IP information
    0. Exit\n""")

    try:
        choice = int(input("Select an option (1 or 2): "))
    except ValueError:
        print("Invalid input. Please enter a valid option.")
        continue
    
    if choice == 1:
        URL = "http://ip-api.com/json/"
    elif choice == 2:
        ip = input("Enter your IP address : ")
        try:
            ipaddress.ip_address(ip)
            URL = f"http://ip-api.com/json/{ip}"
        except ValueError:
            print("Invalid IP Address")
            continue
    elif choice == 0:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

    ip_information = get_ip_information(URL)
    if ip_information:
        print(ip_information)
        
    time.sleep(2)