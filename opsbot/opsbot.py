import subprocess
import sys
from slackbot.bot import Bot, respond_to

@respond_to("update")
def update(opts, bot, event):
    proc = subprocess.Popen(["/etc/nixos/update-all.sh"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    if err:
        message.reply("Error: {}".format(err))
    else:
        message.reply(out)

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
