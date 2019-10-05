#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telegram
import os
import sys

bot_id = os.environ['T_BOT_ID']
chat_id = os.environ['T_CHAT_ID']
# bot = telegram.Bot(bot_id)
# print(bot.get_updates()[0].message.chat.id)

host = sys.argv[1]
shell_comand_true = sys.argv[2]
shell_comand_false = sys.argv[3]

server_up = True if os.system("ping -c 1 {}".format(host)) is 0 else False

bot = telegram.Bot(bot_id)

if server_up:
  output = os.popen(shell_comand_true).read()
  bot.send_message(chat_id=chat_id, text=(host + "\n" + "all is ok ... \n" + output))
else:
  output = os.popen(shell_comand_false).read()
  bot.send_message(chat_id=chat_id, text=(host + "\n" + "host not available ... \n" + output))
