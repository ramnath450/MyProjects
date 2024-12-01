import datetime

end_time = datetime.datetime(2024,11, 14,23, 59, 59)

site_block = ["www.wscubetech.com", "www.codecademy.com"]
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking")
        with open(host_path, "r+") as file:
            content = file.read()
            for site in site_block:
                if site in content:
                   pass
                else:
                    file.write(redirect + " " + site + "\n")
    else:

        with open(host_path, "r+") as file:
           content = file.readlines()
           file.seek(0)
           for line in content:
             if not any(site in line for site in site_block):
                file.write(line)
           file.truncate()
