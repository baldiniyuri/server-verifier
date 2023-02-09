from Functions.server import ServerAnalysis

IP_LIST = ['186.202.153.153', 'www.google.com.br', 'minhacasa.edu.br']

def main():
    print("Running...")
    for ip in IP_LIST:
        server = ServerAnalysis(ip)
        response = server.ping_server()
        print(response)
        response = server.ports_verifier_nmap()
        print(response)
        response = server.server_verifier()
        print(response)
if __name__ == '__main__':
    main()