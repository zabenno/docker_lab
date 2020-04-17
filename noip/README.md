# Overview
A contianer that sets a noip domains to point at its public IP address.

Environment variables to be overridden:
REFRESH_INTERVAL - How often a change of IP will be checked.
USERNAME - The username of the noip account. (This can also be a secret with USERNAME_FILE)
PASSWORD - The password for the noip account. (This can also be a secret with PASSWORD_FILE)

# Assumptions
As noip doesn't allow for automated CLI based selection of FQDNs it is assumed that all FQDNs within the account are to be assigned to the clients IP address. This may be changed in the future if I find a way.
