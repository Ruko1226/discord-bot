import discord

client = discord.Client()


@client.event
async def on_Ready():
    print(client.user.id)
    await client.change_presence(game=discord.Game(name='봇.명령어', type=1))
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("봇.관리"):
        await message.channel.send("```시스템 on```")
    if message.content.startswith("봇.제작자"):
        await message.channel.send("```관리봇 제작자 : 루코님```")
    if message.content.startswith("봇.징계위 출석체크"):
        await message.channel.send("```피고인 출석하셧나요 ?```")
    if message.content.startswith("봇.징계위 궐석재판"):
        await message.channel.send("```지금부터 징계 위원회 재판을 시작하겠습니다. 본 재판은 궐석 재판으로 진행됩니다. 징계 위원분들은 의견을 내어주시기 바랍니다.```")
    if message.content.startswith("봇.징계위 재판"):
        await message.channel.send("```지금부터 징계 위원회 재판을 시작하겠습니다. 본 재판은 참석 인원분들이 모두 참석 하셧음을 알립니다. 징계 위원분들은 의견을 내어주시기 바랍니다.```")
    if message.content.startswith("봇.명령어"):
        await message.channel.send("```봇.관리 = 시스템을 온라인 시킵니다.``` ```봇.제작자 = 봇 제작자를 확인합니다.``` ```봇.징계위 출석체크 = 징계 위원회  출석을 확인합니다.``` ```봇.징계위 궐석재판 = 징계 위원회 궐석재판으로 재판을 시작합니다.``` ```봇.징계위 재판 = 징계 위원회 일반 재판을 시작합니다.``` ")





client.run("NjYwMzE2MTYwMjg5NjY5MTIx.XgbFvg.e2zJI3obGsc9mq9ZjfVCv2b4jWU")