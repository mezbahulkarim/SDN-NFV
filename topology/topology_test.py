
from mininet.topo import Topo

from mininet.net import Mininet

from mininet.node import Switch

from mininet.cli import CLI

from mininet.node import RemoteController

from mininet.node import OVSSwitch

from topology import *

import testing


topos = {'mytopo': (lambda: MyTopo())}

"""

def run_tests(net):

    # You can automate some tests here

    # TODO: How to get the hosts from the net??

    hosts =net.hosts

    for host in hosts:

      if host.IP() == '100.0.0.10' :

         #print("HOST IP MATCHED")

         a = host

      elif host.IP() == '100.0.0.11':

         #print("HOST IP MATCHED")

         b = host

    print("a =",a.name, a.IP())

    print("b =",b.name, b.IP())

    # Launch some tests
    
    testing.ping(a,b, True)

    #testing.curl(h1, h2, expected=False)

"""

def run_tests(net):

    # You can automate some tests here
    # TODO: How to get the hosts from the net??

    h1 = net.get('h1')
    
    h2 = net.get('h2')
    
    h3 = net.get('h3')

    h4 = net.get('h4')

    ws1 = net.get('ws1')

    ws2 = net.get('ws2')

    ws3 = net.get('ws3')

    insp = net.get('insp')

    lb1 = net.get('lb')

    ids = net.get('ids')

    napt = net.get('napt')

    #input()
# Launch some tests

    testing.ping(h1, h2, True)

    testing.ping(h3, h1, True)

    testing.ping(h1, h3, False)

    testing.ping(h3, h2, True)

    testing.ping(h2, h3, False)

    testing.ping(h1, ws1, False)

    testing.ping(h3, ws1, False)

    #testing.curl(h1, ws1, expected=True)

    #testing.curl(h3, ws1, expected=True)

    print("----------- Virtual Address Ping Test-----------")

    testing.ping_virtual(h1, True)

    testing.ping_virtual(h2, True)

    testing.ping_virtual(h3, True)

    testing.ping_virtual(h4, True)

    print("----------- HTTP method Test-----------")

    testing.http_test(h1, "GET", "/get", False)

    testing.http_test(h1, "POST", "/post", True)

    testing.http_test(h1, "HEAD", "/head", False)

    testing.http_test(h1, "OPTIONS", "/options", False)

    testing.http_test(h1, "TRACE", "/trace", False)

    testing.http_test(h1, "PUT", "/put", True)

    testing.http_test(h1, "DELETE", "/delete", False)

    testing.http_test(h1, "CONNECT", "/connect", False)

    print("-----------Linux and SQL code injection Test-----------")

    testing.http_test_input(h1, "cat /etc/passwd ", False)

    testing.http_test_input(h1, "cat /var/log/ ", False)

    testing.http_test_input(h1, "INSERT", False)

    testing.http_test_input(h1, "UPDATE", False)

    testing.http_test_input(h1, "DELETE", False)

if __name__ == "__main__":

    # Create topology

    topo = MyTopo()

    ctrl = RemoteController("c0", ip="127.0.0.1", port=6633)

    # Create the network

    net = Mininet(topo=topo,

                  switch=OVSSwitch,

                  controller=ctrl,

                  autoSetMacs=True,

                  autoStaticArp=True,

                  build=True,

                  cleanup=True)

    # Start the network

    startup_services(net)

    net.get("h3").cmd("ip route add default via 10.0.0.1")

    net.get("h4").cmd("ip route add default via 10.0.0.1")
    
    net.start()
    
    run_tests(net)

    # Start the CLI

    CLI(net)

    # You may need some commands before stopping the network! If you don't, leave it empty

    ### COMPLETE THIS PART ###

    # Delete all links

    for link in net.links:
        net.delLink(link)
    net.stop()
