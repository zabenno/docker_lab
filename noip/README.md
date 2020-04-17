# Overview
A contianer that sets a noip domains to point at its public IP address.

Environment variables to be overridden:
noip_username
noip_password

# Assumptions
As noip doesn't allow for automated CLI based selection of FQDNs it is assumed that all FQDNs within the account are to be assigned to the clients IP address. This may be changed in the future if I find a way.
