import discord
import os
import re
import subprocess

command_char = '$'
help_docs = ""
with open("/var/cache/help.txt") as help_file:
    help_docs = help_file.read()

def get_env_value(env_key):
    env_file_name = "{}_FILE".format(env_key)
    env_file_path = os.getenv(env_file_name)
    if env_file_path:
        if os.path.isfile(env_file_path):
            with open(env_file_path) as env_file:
                env_value = env_file.read().rstrip()
        else:
            print("Error: environment file does not exist but was specified. {}".format(env_file_path))
    else:
        env_value = os.getenv(env_key)
    return env_value

bot_token = get_env_value('BOT_TOKEN')
t_server = get_env_value('T_SERVER')
t_port = get_env_value('T_PORT')
t_username = get_env_value('T_USERNAME')
t_pass = get_env_value('T_PASS')

class transmissionClient():
        def __init__(self, trans_server="localhost", trans_server_port="9091", trans_client_user="username", trans_client_pass="password"):
            self.trans_base_client_cmd = ["transmission-remote", "{}:{}".format(trans_server, trans_server_port), "--auth={}:{}".format(trans_client_user, trans_client_pass)]

        def get_all_torrents(self):
            query = self.trans_base_client_cmd + ["-l"]
            return self.run_query(query)

        def add_torrent(self, torrent):
            query = self.trans_base_client_cmd + ["-a ", torrent]
            return self.run_query(query)

        def remove_torrent(self, torrent_id):
            query = self.trans_base_client_cmd + ["-t", torrent_id, "-r"]
            result = self.run_query(query)
            return result.split("responded: ")[1].replace("\"", "")

        def purge_torrent(self, torrent_id):
            query = self.trans_base_client_cmd + ["-t", torrent_id, "-rad"]
            result = self.run_query(query)
            return result.split("responded: ")[1].replace("\"", "")

        def pause_torrent(self, torrent_id):
            query = self.trans_base_client_cmd + ["-t", torrent_id, "-S"]
            result = self.run_query(query)
            return result.split("responded: ")[1].replace("\"", "")

        def resume_torrent(self, torrent_id):
            query = self.trans_base_client_cmd + ["-t", torrent_id, "-s"]
            result = self.run_query(query)
            return result.split("responded: ")[1].replace("\"", "")

        def run_query(self, query):
            query_process = subprocess.run(query, capture_output=True)
            response = query_process.stdout.decode("utf-8")
            return response


class MyClient(discord.Client):
        def __init__(self, transmission_server, transmission_port, transmission_username, transmission_pass):
            discord.Client.__init__(self)
            self.transmission = transmissionClient(transmission_server, transmission_port, transmission_username, transmission_pass)

        async def on_ready(self):
            print('Logged on as', self.user)
        
        def was_i_messaged(self, message):
            #Don't reply to own message
            if message.author == self.user:
                return False
            
            #Reply if @{{my_user_id}}
            for mention in message.mentions:
                if mention.id == self.user.id:
                    return True

            #Instruction charater option
            if message.content[0] == command_char:
                return True

            #Default to not being mentioned.
            return False

        async def on_message(self, message):
            if self.was_i_messaged(message):
                await self.perform_action(message)
                return
            
        async def perform_action(self, message):
            command = self.get_command_text(message.content)

            top_command = command.split(' ')[0]
            if top_command == "help":
                await self.print_help_docs(message)
            elif top_command == "torrent":
                await self.run_torrent_command(command, message)

        def get_command_text(self, message_text):
            if message_text[0] == command_char:
                message_text = message_text[1:]
            
            elif message_text[0:3] == '<@!':
                message_text = re.sub(r'<@![0-9]+>', '', message_text, count=1)
            
            command_text = message_text.lstrip().rstrip()
            return command_text

        async def print_help_docs(self, message):
            await message.channel.send(help_docs)

        async def run_torrent_command(self, command, message):
            subcommand = command.split()[1]
            if subcommand == "list":
                result = self.transmission.get_all_torrents()
            elif subcommand == "add":
                result = "Functionality coming soon."
            elif subcommand == "remove":
                result = self.transmission.remove_torrent(command.split()[2])
            elif subcommand == "purge":
                result = self.transmission.purge_torrent(command.split()[2])
            elif subcommand == "pause":
                result = self.transmission.pause_torrent(command.split()[2])
            elif subcommand == "resume":
                result = self.transmission.resume_torrent(command.split()[2])
            else:
                result = "{} is not a valid command. For help type help.".format(command.split()[1])
            await message.channel.send("```\n" + result + "\n```")

client = MyClient(t_server, t_port, t_username, t_pass)
client.run(bot_token)
