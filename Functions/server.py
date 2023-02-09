from Functions.messenger import Messenger
from socket import *
from datetime import datetime
from ping3 import verbose_ping
import nmap3


class ServerAnalysis:
  def __init__(self, ip: str):
    self.ip_server = ip
    self.scanner = nmap3.Nmap()
    

  def storage_result(self, file, result):
     with open(file, 'a+') as f:
        f.write(result + "\n")
        f.close()


  def server_verifier(self):

    for port in range(79, 80):
        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.connect_ex((self.ip_server, port))
            self.storage_result("server_verifier_result.txt",f'Domain: {self.ip_server}, Port {port}: Open at {datetime.now()}')
        except Exception as err:
            message = Messenger(err, "Server Verifier")
            message.send_mail()
            continue
        finally:
            s.close()

    return f"Server verifier for {self.ip_server} done."


  def ping_server(self):
    response = verbose_ping(self.ip_server)

    if not response:
        message = Messenger(f"Ip {self.ip_server}, failed with response: {response} at {datetime.now()}", "Server Verifier")
        message.send_mail()
        return f'Server error for {self.ip_server}.'
    
    self.storage_result("ping_server_result.txt", f'Server {self.ip_server} ping in {response}')
    return f'Server {self.ip_server} ping complete.'


  def ports_verifier_nmap(self):

    response = self.scanner.scan_top_ports(self.ip_server) 
    if not response:
       self.storage_result("port_nmap_result.txt", f"Execution at: {datetime.now()}, response:{response}")
       return f"Port namp for domain {self.ip_server} was not possible."

    self.storage_result("port_nmap_result.txt", f"Execution time: {datetime.now()}, response:{response}")
    return f"Port namp service complete for domain {self.ip_server}."