import pexpect
from pexpect import pxssh
import getpass

devices = {'device-1': {'prompt':'<R1>', 'ip':'192.168.75.133'},
           'device-2': {'prompt':'<R2>', 'ip':'192.168.75.131'},
           'device-3': {'prompt':'<R3>', 'ip':'192.168.75.132'}}
commands = ['disp ver','disp int desc','disp ip int br']

username = input('Username: ')
password = getpass.getpass('Password: ')
def main():
    for device in devices.keys():
        outputFileName = device + '_output.txt'
        device_prompt = devices[device]['prompt']
        child = pxssh.pxssh()
        # child = pexpect.spawn('telnet ' + devices[device]['ip'])
        # child.logfile = open('debug', 'wb') для записи вывод в файл
        child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
        with open(outputFileName, 'wb') as f:
            # child.interact() - позволяет вводить команду
            for command in commands:
                child.sendline(command)
                child.expect(device_prompt)
                f.write(child.before)

        child.logout()

if __name__ == '__main__':
    main()