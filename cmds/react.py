import discord
<<<<<<< HEAD
=======
import select_data
import mysql.connector
>>>>>>> 089c665 (data record before 20240227)
from discord.ext import commands
from core.classes import Cog_Extension
import json
from discord.utils import get
from typing import Optional
from easy_pil import Editor, load_image_async, Font

<<<<<<< HEAD
with open('/DiscordBot/BotProject01/setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def picture(self, ctx):
       pic = discord.File(jdata['pic'])
       await ctx.send(file = pic)

#團體戰        
    @commands.command()
    async def dialga_raid(self, ctx, number):
        raidemoji = ["🖐️", "❌"]
        embed=discord.Embed(title=ctx.message.author.name+'的團戰房（打'+str(number)+"場）", color=0xdc0909)
        embed.set_thumbnail(url="https://media.52poke.com/wiki/thumb/8/8a/483Dialga.png/600px-483Dialga.png")
        embed.add_field(name="頭目資訊", value="🔸帝牙盧卡\n🔸屬性：鋼＋龍\n🔸五星團體戰\n🔸極限兩人、建議四到五人開打", inline=False)
        embed.add_field(name="參加或取消團體戰", value="非主持人：\n🖐我要+1\n主持人：\n❌取消主持\n🖐即刻開團", inline=False)
        message = await ctx.send(embed=embed)
    
        for emoji in raidemoji:
          await message.add_reaction(emoji)

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.message.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, id=998750831002255430)
        room = await ctx.guild.create_text_channel(name=ctx.message.author.name+'的團戰房', overwrites=overwrites, category=category)
        room_id=room.id
        role = await ctx.guild.create_role(name = str(room_id))
        await room.set_permissions(role, read_messages=True)

        room_embed=discord.Embed(title=ctx.message.author.name+'的團戰房（打'+str(number)+"場）", color=0x885dfd)
        room_embed.set_thumbnail(url="https://media.52poke.com/wiki/thumb/8/8a/483Dialga.png/600px-483Dialga.png")
        room_embed.add_field(name="頭目資訊",value="🔸帝牙盧卡\n🔸屬性：鋼＋龍\n🔸20/25等最大CP2307/2884\n🔸可用格鬥、地面系寶可夢應戰\n🔸推薦打手：路卡利歐、修建老將、龍頭地鼠、固拉多、怪力、土地雲", inline=False)
        room_embed.add_field(name="結束團體戰",value="群組內任一人輸入""[deletechannel""即可關閉此群組")
        await room.send(embed=room_embed)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["🖐️", "❌"]

        count = 5

        try:
            while count>0:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if str(reaction.emoji) == "🖐️":
                    count-=1
                    guild = self.bot.get_guild(ctx.guild.id)
                    rolee = guild.get_role(role.id)
                    users = await reaction.users().flatten()
                    for use in users:
                        await use.add_roles(rolee)

                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}主持成功")

                elif str(reaction.emoji) == "❌":
                    count-=5
                    await room.delete()
                    await role.delete()
                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}取消了團體戰")

            if count == 0:
                guild = self.bot.get_guild(ctx.guild.id)
                rolee = guild.get_role(role.id)
                users = await reaction.users().flatten()
                for use in users:
                    await use.add_roles(rolee)

                await message.delete()
                await ctx.message.delete()
                await ctx.send(f"{user}主持成功")
               
        except:
            pass

#經驗團
    @commands.command()
    async def EXP(self, ctx, number):
        raidemoji = ["🖐️", "❌"]
        embed=discord.Embed(title=ctx.message.author.name+'的'+str(number)+'人經驗團', color=0x4dff00)
        embed.set_thumbnail(url="https://media.52poke.com/wiki/b/bb/870Falinks.png")
        embed.add_field(name="參加或取消經驗團", value="非主持人：\n🖐我要+1\n主持人：\n❌取消主持\n🖐即刻開團", inline=False)
        message = await ctx.send(embed=embed)
    
        for emoji in raidemoji:
          await message.add_reaction(emoji)

        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.message.author: discord.PermissionOverwrite(read_messages=True)
        }
        category = discord.utils.get(ctx.guild.categories, id=998750831002255430)
        room = await ctx.guild.create_text_channel(name=ctx.message.author.name+'的'+str(number)+'人經驗團', overwrites=overwrites, category=category)
        room_id=room.id
        role = await ctx.guild.create_role(name = str(room_id))
        await room.set_permissions(role, read_messages=True)

        room_embed=discord.Embed(title=ctx.message.author.name+'的'+str(number)+'人經驗團', color=0x4dff00)
        room_embed.set_thumbnail(url="https://media.52poke.com/wiki/b/bb/870Falinks.png")
        room_embed.add_field(name="結束經驗團",value="群組內任一人輸入""[deletechannel""即可關閉此群組")
        await room.send(embed=room_embed)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["🖐️", "❌"]

        count = 30

        try:
            while count>0:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)

                if str(reaction.emoji) == "🖐️":
                    count-=1
                    guild = self.bot.get_guild(ctx.guild.id)
                    rolee = guild.get_role(role.id)
                    users = await reaction.users().flatten()
                    for use in users:
                        await use.add_roles(rolee)

                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}主持成功")

                elif str(reaction.emoji) == "❌":
                    count-=30
                    await room.delete()
                    await role.delete()
                    await message.delete()
                    await ctx.message.delete()
                    await ctx.send(f"{user}取消了經驗團")

            if count == 0:
                guild = self.bot.get_guild(ctx.guild.id)
                rolee = guild.get_role(role.id)
                users = await reaction.users().flatten()
                for use in users:
                    await use.add_roles(rolee)

                await message.delete()
                await ctx.message.delete()
                await ctx.send(f"{user}主持成功")
               
        except:
            pass

    @commands.command()
    async def deletechannel(self, ctx):
        await ctx.channel.delete()
        role = ctx.channel.id
        for del_role in ctx.guild.roles:
            if del_role.name == f'{role}':
               await del_role.delete()

    @commands.command()
    async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
        userr = user or ctx.author

        print('123')

        with open("/DiscordBot/BotProject01/setting.json", "r") as f:
          data = json.load(f)

        print('45')

        xp = data[str(userr.id)]["experience"]
        lvl = data[str(userr.id)]["level"]
        print('67')
        next_level_xp = 22 * ((lvl) ** 2) + 5
        xp_need = next_level_xp
        xp_have = data[str(userr.id)]["experience"]

        percentage = int(((xp_have * 100)/ xp_need))

        if percentage < 1:
          percentage = 0
        print('89')
        ## Rank card
        background = Editor(data['zIMAGE02'])
        profile = await load_image_async(str(userr.display_avatar.url))
        print('45')
        profile = Editor(profile).resize((200, 200)).circle_image()
        print('46')
        poppins = Font.poppins(size=40)
        poppins_small = Font.poppins(size=45)
        print('10')
        #you can skip this part, I'm adding this because the text is difficult to read in my selected image
        ima = Editor(data['zBLACK'])
        background.blend(image=ima, alpha=.5, on_top=False)

        background.paste(profile.image, (20, 50))

        background.rectangle((250, 175), width=590, height=40, fill="#fff", radius=20)
        background.bar(
            (245, 175),
            max_width=590,
            height=40,
            percentage=percentage,
            fill="#ff9933",
            radius=20,
        )
       # background.text((200, 40), f'{userr.name}', font=poppins, color="#ff9933")
        print('11')
        #background.rectangle((200, 100), width=350, height=2, fill="#ff9933")
        background.text(
            (250, 75),
            f"Level : {lvl}   "
            + f" XP : {xp} / {22 * ((lvl) ** 2) + 5}",
            font=poppins_small,
            color="#ff9933",
        )

        card = discord.File(fp=background.image_bytes, filename=data['zCARD'])
        await ctx.send(f'訓練家{userr.mention}的經驗值：')
        await ctx.send(file=card)
        print('4567')
        

async def setup(bot):
    await bot.add_cog(React(bot))
=======
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def rank(self, ctx: commands.Context, user: Optional[discord.Member]):
        if str(ctx.channel.id) == '998750570309505054' or str(ctx.channel.id) == '998829730931413023':
            userr = user or ctx.author
            profile = await load_image_async(str(userr.display_avatar.url))
            with open("setting.json", "r") as f:
                data = json.load(f)

            xp = data[str(userr.id)]["experience"]
            lvl = data[str(userr.id)]["level"]

            next_level_xp = 22 * ((lvl)**2) + 5
            xp_need = next_level_xp
            xp_have = data[str(userr.id)]["experience"]

            percentage = int(((xp_have * 100) / xp_need))

            if percentage < 1:
                percentage = 0
            ## Rank card
            background = Editor(data['zIMAGE02'])

            profile = Editor(profile).resize((200, 200)).circle_image()

            poppins = Font.poppins(size=40)
            poppins_small = Font.poppins(size=50)

            #you can skip this part, I'm adding this because the text is difficult to read in my selected image
            ima = Editor(data['zBLACK'])
            background.blend(image=ima, alpha=.5, on_top=False)

            background.paste(profile.image, (20, 50))

            background.rectangle((250, 185),
                                width=590,
                                height=40,
                                fill="#fff",
                                radius=20)
            background.bar(
                (245, 185),
                max_width=590,
                height=40,
                percentage=percentage,
                fill="#ff9933",
                radius=20,
            )
            # background.text((200, 40), f'{userr.name}', font=poppins, color="#ff9933")
            #background.rectangle((200, 100), width=350, height=2, fill="#ff9933")
            background.text(
                (250, 55),
                f" Level : {lvl}",
                font=poppins_small,
                color="#ff9933",
            )
            background.text(
                (250, 110),
                f" XP : {xp} / {22 * ((lvl) ** 2) + 5}",
                font=poppins_small,
                color="#ff9933",
            )
            await ctx.send(f'訓練家{userr.mention}的經驗值：')
            card = discord.File(fp=background.image_bytes, filename=data['zCARD'])
            await ctx.send(file=card)

#對戰資格查詢
    @commands.command()
    async def battle_qual(self, ctx: commands.Context,
                          user: Optional[discord.Member]):
        if str(ctx.channel.id) == '998750570309505054' or str(ctx.channel.id) == '998829730931413023':
            userr = user or ctx.author
            with open("setting.json", "r") as f:
                data = json.load(f)

            xp = data[str(userr.id)]["experience"]
            lvl = data[str(userr.id)]["level"]
            num_of_played_battle = data[str(userr.id)]["num_of_played_battle"]
            available_xp = xp - 7950 - 6000 * num_of_played_battle

            if lvl < 20:
                await ctx.send(f'{userr.mention}尚未成為烈空座，無對戰資格。')
            elif lvl >= 20 and available_xp < 6000:
                await ctx.send(f'{userr.mention}剩餘經驗 {available_xp} 點，點數不足以申請對戰。')
            elif lvl >= 20 and available_xp >= 6000:
                N = int(available_xp / 6000)
                await ctx.send(
                    f'{userr.mention}剩餘經驗 {available_xp} 點，可以申請 {N} 場對戰。')
#對戰申請
    @commands.command()
    async def battle_apply(self, ctx: commands.Context,
                           user: Optional[discord.Member]):
        if str(ctx.channel.id) == '998750570309505054' or str(ctx.channel.id) == '998829730931413023':
            if str(ctx.author.id) == '632189993334341634':
                userr = user
                with open("setting.json", "r") as f:
                    data = json.load(f)

                xp = data[str(userr.id)]["experience"]
                lvl = data[str(userr.id)]["level"]
                num_of_played_battle = data[str(userr.id)]["num_of_played_battle"]
                available_xp = xp - 7950 - 6000 * num_of_played_battle
                if lvl >= 20 and available_xp >= 6000:
                    num_of_played_battle += 1
                    data[str(
                        userr.id)]["num_of_played_battle"] = num_of_played_battle
                    await ctx.message.delete()
                    await ctx.send(f'{userr.mention} 申請了 1 場對戰。')
                else:
                    await ctx.send(f'經驗點不足或尚未成為烈空座。')

                with open('setting.json', 'w') as f:
                    json.dump(data, f)
            else:
                await ctx.send(f'只有傻豆才能使用這個指令哦～')


#初始化使用者資料（已對戰次數）
    @commands.command()
    async def battle_initial(self, ctx: commands.Context):
        if str(ctx.channel.id) == '998750570309505054' or str(ctx.channel.id) == '998829730931413023':
            if str(ctx.author.id) == '632189993334341634':
                with open('setting.json', 'r') as f:
                    users = json.load(f)

                for i in users:
                    print(i)
                    if i == 'TOKEN':
                        print(0)
                    elif i == 'welcome_channel':
                        print(1)
                    elif i == 'pic':
                        print(2)
                    elif i == 'zIMAGE02':
                        print(3)
                    elif i == 'zBLACK':
                        print(4)
                    elif i == 'zCARD':
                        print(5)
                    else:
                        users[i]['num_of_played_battle'] = 0
                        #print(users[i]['num_of_played_battle'])

                with open('setting.json', 'w') as f:
                    json.dump(users, f)
            else:
                await ctx.send(f'只有傻豆才能使用這個指令哦～')

    @commands.command()
    async def EXP_add(self, ctx: commands.Context):
        if str(ctx.channel.id) == '998750570309505054' or str(ctx.channel.id) == '998829730931413023':
            if str(ctx.author.id) == '632189993334341634':
                with open('setting.json', 'r') as f:
                    users = json.load(f)

                for i in users:
                    print(i)
                    if i == 'TOKEN':
                        print(0)
                    elif i == 'welcome_channel':
                        print(1)
                    elif i == 'pic':
                        print(2)
                    elif i == 'zIMAGE02':
                        print(3)
                    elif i == 'zBLACK':
                        print(4)
                    elif i == 'zCARD':
                        print(5)
                    else:
                        exp_before = users[i]['experience']
                        exp_after = exp_before + 1000
                        users[i]['experience'] = exp_after

                with open('setting.json', 'w') as f:
                    json.dump(users, f)
            else:
                await ctx.send(f'只有傻豆才能使用這個指令哦～')

    @commands.command()
    async def game_history_leader(self, ctx: commands.Context):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            
            records = select_data.historywinhighest()
            text = '🎊練武室歷史戰績勝率排行榜🎊\n'
        
            for i in range(1, len(records)+1):
                if i == len(records):
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}'
                else:
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}\n'
             
            await ctx.send(text)

    @commands.command()
    async def game_history_loser(self, ctx: commands.Context):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            
            records = select_data.historywinlowest()
            text = '🎊練武室歷史戰績倒數勝率排行榜🎊\n'
            for i in range(1, len(records)+1):
                if i == len(records):
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.-{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}'
                else:
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.-{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}\n'
             
            await ctx.send(text)
    
    @commands.command()
    async def game_month_leader(self, ctx: commands.Context):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            
            records = select_data.monthlywinhighest()
            text = '🎊練武室單月戰績勝率排行榜🎊\n'
            for i in range(1, len(records)+1):
                if i == len(records):
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}'
                else:
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}\n'
             
            await ctx.send(text)

    @commands.command()
    async def game_month_loser(self, ctx: commands.Context):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            
            records = select_data.monthlywinlowest()
            text = '🎊練武室單月戰績倒數勝率排行榜🎊\n'
            for i in range(1, len(records)+1):
                if i == len(records):
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.-{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}'
                else:
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.-{i}  {ue_name.name}  |  勝場：{records[i-1][1]}  敗場：{records[i-1][2]}  勝率：{records[i-1][3]}\n'
             
            await ctx.send(text)

    @commands.command()
    async def game_history_num(self, ctx: commands.Context):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            
            records = select_data.historynumhighest()
            text = '🎊練武室歷史對戰總場次排行榜🎊\n'
            for i in range(1, len(records)+1):
                if i == len(records):
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  對戰總場次：{records[i-1][4]}  勝率：{records[i-1][3]}'
                else:
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  對戰總場次：{records[i-1][4]}  勝率：{records[i-1][3]}\n'
             
            await ctx.send(text)

    @commands.command()
    async def game_month_num(self, ctx: commands.Context):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            
            records = select_data.monthlynumhighest()
            text = '🎊練武室單月對戰總場次排行榜🎊\n'
            for i in range(1, len(records)+1):
                if i == len(records):
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  對戰總場次：{records[i-1][4]}  勝率：{records[i-1][3]}'
                else:
                    ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                    text += f'No.{i}  {ue_name.name}  |  對戰總場次：{records[i-1][4]}  勝率：{records[i-1][3]}\n'
             
            await ctx.send(text)

    @commands.command()
    async def game_personal(self, ctx: commands.Context,user: Optional[discord.Member]):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            userr = user or ctx.author
            
            history_records = select_data.historyper(str(userr.id))
            month_records = select_data.monthlyper(str(userr.id))
            text = f'{userr.mention} 的練武室對戰成績👇\n'
            text += f'歷史對戰成績  |  勝場：{history_records[0][1]}  敗場：{history_records[0][2]}  勝率：{history_records[0][3]}  對戰總場次：{history_records[0][4]}\n'
            text += f'單月對戰成績  |  勝場：{month_records[0][1]}  敗場：{month_records[0][2]}  勝率：{month_records[0][3]}  對戰總場次：{month_records[0][4]}'

             
            await ctx.send(text)

    @commands.command()
    async def game_wl(self, ctx: commands.Context,user1: Optional[discord.Member], user2: Optional[discord.Member]):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            connection = mysql.connector.connect(host='localhost',port='3306',user='root',password='Zxyc397125',database='dc_martial_arts')
            print('successfully connect')
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO `history_table`(`user_id`) VALUES({user1.id}) ON DUPLICATE KEY UPDATE `user_id` = {user1.id};', multi=True)
            cursor.execute(f'INSERT INTO `history_table`(`user_id`) VALUES({user2.id}) ON DUPLICATE KEY UPDATE `user_id` = {user2.id};', multi=True)
            cursor.execute(f'INSERT INTO `monthly_table`(`user_id`) VALUES({user1.id}) ON DUPLICATE KEY UPDATE `user_id` = {user1.id};', multi=True)
            cursor.execute(f'INSERT INTO `monthly_table`(`user_id`) VALUES({user2.id}) ON DUPLICATE KEY UPDATE `user_id` = {user2.id};', multi=True)
            connection.commit()

            #select_data.winer_history_update(user1.id)
            #select_data.winer_monthly_update(user1.id)
            #select_data.loser_history_update(user2.id)
            #select_data.loser_monthly_update(user2.id)

            #贏家歷史
            cursor.execute(f'SELECT * FROM `history_table` WHERE `user_id` = {user1.id};', multi=True)

            records = cursor.fetchall()
            history_win_num = records[0][1]
            history_win_num +=1
            cursor.execute(f'UPDATE `history_table` SET `history_win_game` = {history_win_num} WHERE `user_id` = {user1.id};', multi=True)
            history_total_num = records[0][4]
            history_total_num += 1

            new_history_win_percentage = round(history_win_num/history_total_num, 2)
            print(new_history_win_percentage)
            cursor.execute(f'UPDATE `history_table` SET `winning_percentage` = {new_history_win_percentage} WHERE `user_id` = {user1.id};', multi=True)
            cursor.execute(f'UPDATE `history_table` SET `history_total_game` = {history_total_num} WHERE `user_id` = {user1.id};', multi=True)
            connection.commit()
            

            #贏家單月
            cursor.execute(f'SELECT * FROM `monthly_table` WHERE `user_id` = {user1.id};', multi=True)

            records = cursor.fetchall()
            month_win_num = records[0][1]
            month_win_num +=1
            cursor.execute(f'UPDATE `monthly_table` SET `monthly_win_game` = {month_win_num} WHERE  `user_id` = {user1.id};', multi=True)
            month_total_num = records[0][4]
            month_total_num += 1
            new_month_win_percentage = round(month_win_num/month_total_num, 2)
            cursor.execute(f'UPDATE `monthly_table` SET `monthly_percentage` = {new_month_win_percentage} WHERE  `user_id` = {user1.id};', multi=True)
            cursor.execute(f'UPDATE `monthly_table` SET `monthly_total_game` = {month_total_num} WHERE  `user_id` = {user1.id};', multi=True)
            connection.commit()
            await ctx.send(f'贏家 {user1.mention} 戰績紀錄成功😏')

            #輸家歷史
            cursor.execute(f'SELECT * FROM `history_table` WHERE `user_id` = {user2.id};', multi=True)

            records = cursor.fetchall()
            history_los_num = records[0][2]
            history_los_num +=1
            cursor.execute(f'UPDATE `history_table` SET `history_lose_game` = {history_los_num} WHERE  `user_id` = {user2.id};', multi=True)
            history_total_num = records[0][4]
            history_total_num += 1
            new_history_win_percentage = round(1-(history_los_num)/history_total_num, 2)
            cursor.execute(f'UPDATE `history_table` SET `winning_percentage` = {new_history_win_percentage} WHERE  `user_id` = {user2.id};', multi=True)
            cursor.execute(f'UPDATE `history_table` SET `history_total_game` = {history_total_num} WHERE  `user_id` = {user2.id};', multi=True)
            connection.commit()
           

            #輸家單月
            cursor.execute(f'SELECT * FROM `monthly_table` WHERE `user_id` = {user2.id};', multi=True)

            records = cursor.fetchall()
            month_los_num = records[0][2]
            month_los_num +=1
            cursor.execute(f'UPDATE `monthly_table` SET `monthly_lose_game` = {month_los_num} WHERE  `user_id` = {user2.id};', multi=True)
            month_total_num = records[0][4]
            month_total_num += 1
            new_month_win_percentage = round(1-(month_los_num)/month_total_num, 2)
            cursor.execute(f'UPDATE `monthly_table` SET `monthly_percentage` = {new_month_win_percentage} WHERE  `user_id` = {user2.id};', multi=True)
            cursor.execute(f'UPDATE `monthly_table` SET `monthly_total_game` = {month_total_num} WHERE  `user_id` = {user2.id};', multi=True)
            connection.commit()
            await ctx.send(f'輸家 {user2.mention} 戰績紀錄成功😢')
            
            cursor.close()
            connection.close()

    @commands.command()
    async def game_month_settlement(self, ctx: commands.Context):
        if str(ctx.channel.id) == '1067819709954793553' or str(ctx.channel.id) == '998829730931413023':
            if str(ctx.author.id) == '632189993334341634':
                with open('setting.json', 'r') as f:
                    users = json.load(f)
                
                records=select_data.monthlywinhighest()
                text = '🎊練武室單月戰績結算🎊\n'

                for i in range(1, len(records)+1):
                    if i == 1:
                        ue_id= str(records[i-1][0])
                        ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                        text += f'武王/武后： {ue_name.name} | 勝率：{records[i-1][3]}\n'
                        exp_before = users[ue_id]['experience']
                        exp_after = exp_before + 5000
                        users[ue_id]['experience'] = exp_after
                    
                    if i == 2:
                        ue_id= str(records[i-1][0])
                        ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                        text += f'武林高手： {ue_name.name} | 勝率：{records[i-1][3]}\n'
                        exp_before = users[ue_id]['experience']
                        exp_after = exp_before + 3000
                        users[ue_id]['experience'] = exp_after

                    if i == 6:
                        ue_id= str(records[i-1][0])
                        ue_name = await ctx.message.guild.fetch_member(int(records[i-1][0]))
                        text += f'武道高牆： {ue_name.name} | 勝率：{records[i-1][3]}\n'
                        exp_before = users[ue_id]['experience']
                        exp_after = exp_before + 500
                        users[ue_id]['experience'] = exp_after

                records01 = select_data.monthlynumhighest()
                    
                for i in range(1, len(records)+1):
                    if i == 1:
                        ue_id= str(records01[i-1][0])
                        ue_name = await ctx.message.guild.fetch_member(int(records01[i-1][0]))
                        text += f'武癡： {ue_name.name} | 對戰總場次：{records01[i-1][4]} \n'
                        exp_before = users[ue_id]['experience']
                        exp_after = exp_before + 1500
                        users[ue_id]['experience'] = exp_after


                records02 = select_data.monthlywinlowest()
                    
                for i in range(1, len(records)+1):
                    if i == 1:
                        ue_id= str(records02[i-1][0])
                        ue_name = await ctx.message.guild.fetch_member(int(records02[i-1][0]))
                        text += f'武法獲勝： {ue_name.name} | 勝率：{records02[i-1][3]}'
                        exp_before = users[ue_id]['experience']
                        exp_after = exp_before + 50
                        users[ue_id]['experience'] = exp_after
                await ctx.message.delete()
                await ctx.send(text)
                await ctx.send('經驗值獎勵已發放，月排行榜已重置')

                with open('setting.json', 'w') as f:
                    json.dump(users, f)
            else:
                await ctx.send(f'只有傻豆才能使用這個指令哦～')

async def setup(bot):
    await bot.add_cog(React(bot))
>>>>>>> 089c665 (data record before 20240227)
