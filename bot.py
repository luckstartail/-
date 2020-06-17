import discord
from discord.ext import commands
import asyncio
import datetime
import calendar
import requests
from bs4 import BeautifulSoup
import random
serverid=None
warning=False
def _http(URL):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    _http=requests.get(URL,headers=headers)
    if _http.status_code==200:
        http=_http.text
    return http
def _http_(URL):
    _http=requests.get(URL)
    if _http.status_code==200:
        http=_http.text
    return http

client = commands.Bot(command_prefix='/')

@client.event
async def on_member_ban(guild,user):
    k=0
    serverid=guild.id
    author=client.get_user(int(user.id))
    f2=open("./경고.txt","r",encoding="UTF-8")
    data=f2.readlines()
    for i in range(0,len(data)):
        author2=data[i].split('=')[0].split('-')
        author3=author2[-1]
        ids=author2[0]
        if str(author)==author3 and int(serverid)==int(ids):
            num3=int(data[i].split('=')[1].replace('\n',''))+1
            data[i]=f"{serverid}-{author}=5\n"
            f1=open("./경고.txt","w",encoding="UTF-8")
            f3=open("./경고.txt","a",encoding="UTF-8")
            k=1
            for i in range(0,len(data)):
                f3.write(data[i])
    if k==0:
        f4=open("./경고.txt","a",encoding="UTF-8")
        f4.write(f"{serverid}-{author}=5\n")
        f4.close()
    

@client.event
async def on_member_unban(guild,user):
    k=0
    serverid=int(guild.id)
    author=client.get_user(int(user.id))
    f2=open("./경고.txt","r",encoding="UTF-8")
    data=f2.readlines()
    for i in range(0,len(data)):
        author2=data[i].split('=')[0].split('-')
        author3=author2[-1]
        ids=author2[0]
        if str(author)==author3 and serverid==int(ids):
            data[i]=f"{serverid}-{author}=0\n"
            f1=open("./경고.txt","w",encoding="UTF-8")
            f3=open("./경고.txt","a",encoding="UTF-8")
            k=1
            for i in range(0,len(data)):
                f3.write(data[i])
    if k==0:
        f4=open("./경고.txt","a",encoding="UTF-8")
        f4.write(f"{serverid}-{author}=0\n")
        f4.close()
    
    
    
    
        

@client.event
async def on_ready():
    print("디코봇스타트")
    game = discord.Game("영웅이 따까리")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.command(name="경고주기")
@commands.has_permissions(ban_members=True)
async def 경고주기(ctx):
    global warning, serverid
    warning=True
    serverid=ctx.guild.id

@client.command(name="경고차감")
@commands.has_permissions(ban_members=True)
async def 경고차감(ctx):
    global warning, serverid
    warning=True
    serverid=ctx.guild.id

@client.command(name="경고리스트")
@commands.has_permissions(ban_members=True)
async def 경고리스트(ctx):
    global warning, serverid
    warning=True
    serverid=ctx.guild.id


@client.event
async def on_message(message):
    global warning
    if message.content.startswith('펠퀴'):
        await message.channel.send('벌레')
    if message.content.startswith('따까리'):
        await message.channel.send('나 불러써?')
    if message.content.startswith('대가리박아'):
        if "뀨탑정" in message.author.name:
            await message.channel.send('ㅈㄲ 니말은 안들어')
        else:
            await message.channel.send('네 대가리 박겠습니다.')
    if message.content.startswith('"야 넣을게"'):
        await message.channel.send('으.....응')

    if message.content.startswith("/장지환랜덤짤"):
        i=random.randint(0,8)
        if i==0:
            await message.channel.send('https://tenor.com/view/%ea%b4%b4%eb%ac%bc%ec%a5%90-%ec%9e%a5%ec%a7%80%ed%99%98-monsrat-monsterrat-%eb%8f%84%eb%a7%9d%ea%b0%80-gif-16033044')
        if i==1:
            await message.channel.send('https://tenor.com/view/%ec%9e%a5%ec%a7%80%ed%99%98-%ea%b4%b4%eb%ac%bc%ec%a5%90-%ec%a0%84%ec%9e%90%eb%8b%b4%eb%b0%b0-%ec%a0%84%eb%8b%b4-%ec%9b%94%ed%81%b4-gif-16033038')
        if i==2:
            await message.channel.send('https://tenor.com/view/%ec%9e%a5%ec%a7%80%ed%99%98-%ea%b4%b4%eb%ac%bc%ec%a5%90-monsterrat-monsrat-%ed%97%ac%ec%8a%a4-gif-16032922')
        if i==3:
            await message.channel.send('https://tenor.com/view/ggot-that-%ea%b8%b0%eb%aa%a8%eb%a7%81-%ec%9e%89%ea%b8%b0%eb%aa%a8%eb%a7%81-%ec%9d%b4%ec%9e%89%ea%b8%b0%eb%aa%a8%eb%a7%81-%ea%b4%b4%eb%ac%bc%ec%a5%90-gif-15823429')
        if i==4:
            await message.channel.send('https://tenor.com/view/%ea%b4%b4%eb%ac%bc%ec%a5%90-%ec%9e%a5%ec%a7%80%ed%99%98-%ea%b8%b0%eb%aa%a8%eb%a7%81-%ea%b8%b0%eb%aa%a8%eb%a4%bc-%ec%9d%b4%ec%9e%89-gif-14987174')
        if i==5:
            await message.channel.send('https://tenor.com/view/%ec%a7%80%ea%b1%b4-%ea%b4%b4%eb%ac%bc%ec%a5%90-%ec%84%a4%ec%82%ac-laughing-happy-gif-17500030')
        if i==6:
            await message.channel.send('https://tenor.com/view/%ea%b4%b4%eb%ac%bc%ec%a5%90-%eb%a7%90%eb%8c%80%ea%be%b8%ed%95%98%ec%a7%80%eb%a7%88-streamer-mad-angry-gif-16583846')
        if i==7:
            await message.channel.send('https://tenor.com/view/%ea%b4%b4%eb%ac%bc%ec%a5%90-happy-smile-laugh-gif-15933334')
    if message.content.startswith("/경고확인"):
        k=0
        author=message.guild.get_member(int(message.author.id))
        f2=open("./경고.txt","r",encoding="UTF-8")
        data=f2.readlines()
        for i in range(0,len(data)):
            author2=data[i].split('=')[0].split('-')
            author3=author2[-1]
            ids=author2[0]
            if str(author)==str(author3) and int(message.guild.id)==int(ids):
                mes="{}:{}회".format(author,int(data[i].split('=')[1].replace('\n','')))
                await message.channel.send(mes)
                k=1
                

        if k==0:
            await message.channel.send("{}:0회".format(author))



    if message.content.startswith("/네이버실검순위"):
        html=_http("https://datalab.naver.com/keyword/realtimeList.naver?where=main")
        soup=BeautifulSoup(html,'html.parser')
        soup=str(soup.find_all("span","item_title"))
        soup=soup.replace('</span>','')
        soup=soup.replace('<span class="item_title"','')
        soup=soup.replace('>','')
        soup=soup.replace('[','')
        soup=soup.replace(']','')
        lis1=soup.split(",")
        text=""
        for i in range(0,20):
            text+=f"{i+1}위: {lis1[i]}\n"
        embed=discord.Embed(color=0x00ff00)
        embed.add_field(name="네이버실시간검색순위",value=text,inline=False)
        await message.channel.send(embed=embed)
    if message.content.startswith("나비보벳따우"):
        await message.channel.send("https://www.youtube.com/watch?v=60KVywlhwEM")
    #경고주기
    if message.content.startswith("/경고주기"):
        warning=False
        await client.process_commands(message)
        if warning==True:
            k=0
            author=message.guild.get_member(int(message.content[6:24]))
            if author!=None:
                f2=open("./경고.txt","r",encoding="UTF-8")
                data=f2.readlines()
                for i in range(0,len(data)):
                    author2=data[i].split('=')[0].split('-')
                    author3=author2[-1]
                    ids=author2[0]
                    if str(author)==author3 and int(message.guild.id)==int(ids):
                        num3=int(data[i].split('=')[1].replace('\n',''))+1
                        data[i]=f"{serverid}-{author}={num3}\n"
                        f1=open("./경고.txt","w",encoding="UTF-8")
                        f3=open("./경고.txt","a",encoding="UTF-8")
                        for i in range(0,len(data)):
                            f3.write(data[i])
                        k=1
                        f1.close()
                        f3.close()
                        if num3>=5:
                            await message.guild.ban(author)
                            await message.channel.send(f"{author}님은 경고 5회를 받았기 때문에 서버에서 추방됩니다.")
                        else:
                            await message.channel.send(f"{author}님의 경고누적횟수는{num3}회입니다")

                if k==0:
                    f4=open("./경고.txt","a",encoding="UTF-8")
                    f4.write(f"{serverid}-{author}=1\n")
                    f4.close()
                    await message.channel.send(f"{author}님의 경고누적횟수는1회입니다")
            else:
                await message.channel.send(f"이서버에없거나 추방당했습니다.")

    #경고리스트
    if message.content.startswith("/경고리스트"):
        warning=False
        text=""
        await client.process_commands(message)
        if warning==True:
            f2=open("./경고.txt","r",encoding="UTF-8")
            data=f2.readlines()
            for i in range(0,len(data)):
                author2=data[i].split('=')[0].split('-')
                ids=author2[0]
                if int(message.guild.id)==int(ids):
                    a=str(data[i].replace(f'{ids}-',''))
                    if int(data[i].split('=')[1])>=5:
                        text+="{}\n".format(a)
                    else:
                        text+="{}\n".format(a)
        if text != '':
            embed1=discord.Embed(color=0x00ff00)
            embed1.add_field(name="경고리스트",value=str(text),inline=False)
            await message.channel.send(embed=embed1)
        else:  
            embed1=discord.Embed(color=0x00ff00)
            embed1.add_field(name="경고리스트",value="아무도 경고를 받은적없거나\n받은사람이 없습니다.",inline=False)
            await message.channel.send(embed=embed1)
   
    #롤랭크
    if message.content.startswith("/롤랭크"):
        typing=message.content[5:20]
        html=_http(f"https://www.op.gg/summoner/userName={typing}")
        soup=BeautifulSoup(html,"html.parser")
        #솔랭
        tier = str(soup.find("div",{"class":"TierRank"}))
        tier=tier.replace('<div class="TierRank">',"솔랭: ")
        tier=tier.replace('</div>',"")
        tier=tier.replace('\n',"")
        tier=tier.replace(' ',"")
        tier=tier.replace('<divclass="TierRankunranked">',"솔랭: ")
        tier=tier.replace(' ',"")
        tier=tier.replace('\t',"")
        #솔랭(win)
        win = str(soup.find("span",{"class":"wins"}))
        win=win.replace('<span class="wins">','')
        win=win.replace('</span>','')
        #솔랭(loss)
        loss = str(soup.find("span",{"class":"losses"}))
        loss=loss.replace('<span class="losses">','')
        loss=loss.replace('</span>','')

        #솔랭lp 추출
        lp = soup.find("span",{"class":"LeaguePoints"})
        if lp !=None:
            lp = lp.text.strip()

        #자랭
        tier1 = str(soup.find("div",{"class":"sub-tier__rank-tier"}))
        tier1 = tier1.replace('\n','')
        tier1 = tier1.replace(' ','')
        tier1 = tier1.replace('</div>','')
        tier1 = tier1.replace('<divclass="sub-tier__rank-tier">','자랭: ')
        tier1 = tier1.replace('\n','')
        tier1 = tier1.replace(' ','')
        tier1 = tier1.replace('<divclass="sub-tier__rank-tierunranked">','자랭: ')
        
        #자랭lp 추출
        lp1 = soup.find("div",{"class":"sub-tier__league-point"})
        if not lp1==None:
            lp1 = lp1.text.strip()
        tex=f"\n{tier}({lp}/{win} {loss})\n{tier1}({lp1})"
        embed=discord.Embed(color=0x00ff00)
        embed.add_field(name=f"{typing}",value=tex,inline=False)
        await message.channel.send(embed=embed)
        



    #경고차감
    if message.content.startswith("/경고차감"):
        warning=False
        await client.process_commands(message)
        if warning==True:
            k=0
            author=message.guild.get_member(int(message.content[6:24]))
            if author!=None:
                f2=open("./경고.txt","r",encoding="UTF-8")
                data=f2.readlines()
                for i in range(0,len(data)):
                    author2=data[i].split('=')[0].split('-')
                    author3=author2[-1]
                    ids=author2[0]
                    if str(author)==author3 and int(ids)==int(message.guild.id):
                        num3=int(data[i].split('=')[1].replace('\n',''))-1
                        if num3<0:
                            num3=0
                        data[i]=f"{serverid}-{author}={num3}\n"
                        f1=open("./경고.txt","w",encoding="UTF-8")
                        f3=open("./경고.txt","a",encoding="UTF-8")
                        for i in range(0,len(data)):
                            f3.write(data[i])
                        k=1
                        f1.close()
                        f3.close()
                        if num3>=5:
                            await message.channel.send(f"{author}님은 경고 5회라서 이미 밴당했습니다")
                        elif num3<=0:
                            await message.channel.send(f"{author}님의 경고누적횟수는{num3}회입니다")
                        else:
                            await message.channel.send(f"{author}님의 경고누적횟수는{num3}회입니다")

                if k==0:
                    await message.channel.send(f"{author}님의 경고누적횟수는0회입니다")
               
            else:
                await message.channel.send(f"이서버에없거나 추방당했습니다.")
    
        
            

#디코봇가동
client.run('NjkxMjE0NTE3ODA3NjExOTQ0.XuoV0g.vcnbR-B0K2SVSTNNq5sI3DBspz4')
