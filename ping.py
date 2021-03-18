import os

ip = "https://alkai.herokuapp.com/"
exit_code = os.system(f"ping -c 1 -w2 {ip} > /dev/null 2>&1")
