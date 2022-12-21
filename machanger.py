import subprocess
import optparse


def change_mac(interface, new_mac):
    print("[+] changing mac for interface " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="specify interface to change mac for, use --help")
    parser.add_option("-m", "--mac", dest="new_mac", help="specify the new mac{0-9, A-F}, use --help for usage")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify interface, use --help for usage")
    elif not options.new_mac:
        parser.error("[-] please specify interface, use --help for usage")
    return options


options = get_argument()
change_mac(options.interface, options.new_mac)
