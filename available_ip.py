# TODO - Provide 4 subnet octets either through input or directly
octet_one = 255
octet_two = 224
octet_three = 0
octet_four = 0

# TODO - Perform calculation
available_ip_addresses = ((256 - octet_one) * (256 - octet_two) * (256 - octet_three) * (256 - octet_four))

print("IP Addresses available: ")
print(available_ip_addresses)
# TODO - Return total number of IP addresses



