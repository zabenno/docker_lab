# Overview
The purpose of this discord bot is to allow a user to manage a torrent client through the discord.

## Intention of use
For when multiple user want may use the same torrent and have access to the same NFS share but are not comfortable  using the command line or want to be able to manage torrents while away from their home network.

## Status
Alpha - Expect bugs and levels of functionality to change drastically.

# Parameters
1. BOT_TOKEN - The authentication token for discord. (MUST)
2. T_SERVER - The DNS name of the remote transmission server. (OPTIONAL default=localhost)
3. T_PORT - The port the remote transmission server is listening on. (OPTIONAL default=9091)
4. T_USERNAME - The username to authenticate with the remote transmission server with. (SHOULD default=username)
5. T_PASS - The password to authenticate with the remote transmission server with. (SHOULD default=password)
