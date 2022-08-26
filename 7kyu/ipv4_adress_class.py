def ipv4_address_class(ipv4_addr):
    first_octet = int(ipv4_addr.split(".")[0])
    match first_octet:
        case n if n <= 127:
            return 'A'
        case n if n <= 191:
            return 'B'
        case n if n <= 223:
            return 'C'
        case n if n <= 239: 
            return 'D'
        case n if n <= 255:
            return 'E'

print(ipv4_address_class("1.1.1.1"))
print(ipv4_address_class("172.66.43.71"))
print(ipv4_address_class("192.168.0.1"))
print(ipv4_address_class("224.0.0.227"))
print(ipv4_address_class("242.0.0.227"))

       
        
    


ipv4_address_class("192.168.0.1")



