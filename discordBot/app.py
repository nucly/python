import os
import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))


client = MyClient()
client.run('Nzc5NDQyNDQ5MzE1NjU5Nzg3.X7gmWQ.w2WqsutOFbAYn-PYwHo2gEOG__M')

