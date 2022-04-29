

from main_class import BinaryTranslation, DecimalTranslation
from utils import evaluate_ip


user_ip = "123.112.111.111"

ip_type = evaluate_ip(user_ip)

if ip_type == 'decimal':
    ip_info = DecimalTranslation(user_ip).ip_info()
else:
    ip_info = BinaryTranslation(user_ip).ip_info()


print('INFORMACION DE LA IP')
print(ip_info)
