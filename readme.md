pip3 install -r requirements.txt

T_BOT_ID=977032468:AAFG2VmgKXQa5nX5jBClwguk0Eg7jU1wNTM T_CHAT_ID=311096684 python3 t_bot.py google.com 'date' 'date'


```
---
  - name: Ping host by crone and send massate to telegram channel
    cron:
      # state: absent
      name: Ping host by crone and send massate to telegram channel
      minute: 59
      user: {{ deploy_user }}
      job: T_BOT_ID=977032468:AAFG2VmgKXQa5nX5jBClwguk0Eg7jU1wNTM T_CHAT_ID=311096684 python3 ~/t_bot/t_bot.py google.com 'date' 'date'
    become: yes
    become_user: {{ deploy_user }}

```
