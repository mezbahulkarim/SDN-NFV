from baseFirewall import Firewall


# Here we implement our network firewalls. All network firewalls are inherited from Firewall class.

# Rules parameters are:
# index 0: Determines the hardware port of the incoming packet.
# index 1: Determines the TCP layer protocol. (possible values: TCP, UDP, any)
# index 2: Determine the source IP address of the incoming packet. It should be either "any" or a subnet with "IP/Subnet" format (e.g, 100.0.0.40/32).
# index 3: Determine the TCP layer source port number of the incoming packet. (possible values: any, an integer as the port number)
# index 4: Determine the destination IP address of the incoming packet. Same format as the source IP.
# index 5: Determine the TCP layer destination port number of the incoming packet. Same format as the source port.
# index 6: To allow or block the matched packet. (possible values: allow, block)

# Note that the Firewall trace the rules from 0 to n and make the decision based on first matched rule.

# Hardware ports:
# public-zone --------- 1 FW1 2 ------------ DmZ
# DmZ ----------------- 1 FW2 2 ------------ private-zone

class FW1 (Firewall):

    def __init__(self, connection):

        """
        Initialize Firewall class and set rules!
        The following is just a sample to give you the idea.
        """

        ### COMPLETE THIS PART ###

        Firewall.__init__(self, connection, "FW1")
        self.rules = [
            [1, 'TCP', 'any', 'any', '100.0.0.40/29', '80', 'allow'], # allow Pbz to DMC webserver
            #[1, 'TCP', 'any', 'any', '100.0.0.41/24', '80', 'allow'], # allow Pbz to DMC webserver
            #[1, 'TCP', 'any', 'any', '100.0.0.42/24', '80', 'allow'], # allow Pbz to DMC webserver
            #[1, 'TCP', 'any', 'any', '100.0.0.50/24', '80', 'allow'], # allow Pbz to Prz webserver
            #[1, 'TCP', 'any', 'any', '100.0.0.51/24', '80', 'allow'], # allow Pbz to Prz webserver
            [1, 'any', 'any', 'any', '100.0.0.45/32', 'any', 'allow'], # allow Pbz to virtual IP webserver
            [1, 'any', 'any', 'any', 'any', 'any', 'block'],
            [2, 'any', 'any', 'any', 'any', 'any', 'allow']
        ]


class FW2 (Firewall):
    def __init__(self, connection):

        """
        Initialize Firewall class and set rules!
        The following is just a sample to give you the idea.
        """

        ### COMPLETE THIS PART ###

        Firewall.__init__(self, connection, "FW2")
        self.rules = [
            [2, 'TCP', 'any', 'any', '100.0.0.40/29', '80', 'allow'], # allow Prz to DMC webserver
            #[2, 'TCP', 'any', 'any', '100.0.0.41/24', '80', 'allow'], # allow Prz to DMC webserver
            #[2, 'TCP', 'any', 'any', '100.0.0.42/24', '80', 'allow'], # allow Prz to DMC webserver
            #[2, 'any', 'any', 'any', '100.0.0.40/29', 'any', 'block'], # block Prz to DMC webserver incorrect way
            #[2, 'any', 'any', 'any', '100.0.0.41/24', 'any', 'block'], # block Pbz to DMC webserver incorrect way
            #[2, 'any', 'any', 'any', '100.0.0.42/24', 'any', 'block'], # block Pbz to DMC webserver incorrect way
            [2, 'any', 'any', 'any', '100.0.0.45/32', 'any', 'allow'], # allow Prz to virtual IP webserver
            [1, 'any', 'any', 'any', 'any', 'any', 'block'],
            [2, 'any', 'any', 'any', 'any', 'any', 'allow']
        ]
