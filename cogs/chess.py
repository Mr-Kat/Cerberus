import chess
from discord.ext import commands

class Chess(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.board = chess.Board()

def setup(client):
    client.add_cog(Chess(client))