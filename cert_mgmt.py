import json
import pickle
import sys
import os

class CertificationManagement(object):

    def __init__(self, config):
        f = open(config['certFilename'], 'r')
        self.certs = pickle.load(f)
        f.close()
        self.config = config

    def listHostnames(self):
        for hostname in self.certs:
            print(hostname)

    def removeHostname(self):
        del self.certs[hostname.lower()]

    def store(self):
        try:
            os.remove(self.config['certFilename'] + '.bak')
        except Exception:
            pass
        try:
            os.rename(self.config['certFilename'], self.config['certFilename'] + '.bak')
        except Exception:
            pass
        f = open(self.config['certFilename'], 'w')
        try:
            pickle.dump(self.certs, f)
            f.flush()
        finally:
            f.close()
        sys.exit()

    def quit(self):
        sys.stdout.write('Quit without Save? [Y/N]: ')
        if sys.stdin.readline().strip().upper() != 'Y':
            return
        sys.exit()

    def start(self):
        functionMap = {
            1 : self.listHostnames,
            2 : self.removeHostname,
            3 : self.store,
            4 : self.quit,
            }
        while True:
            print('''1. List certifications hostname
2. Remove a hostname from certifications
3. Save and Quit
4. Quit without Save''')
            sys.stdout.write('Select function: ')
            functionMap[int(sys.stdin.readline().strip())]()

if __name__ == '__main__':
    CertificationManagement(json.loads(open(sys.argv[1], 'r').read())).start()
