# Made by DankoOfficial on Github
# Discord: $ky#3788
# Dont skid, I'll catch you I swear. Give credits
# vc = Valid Cookie
# vcr = Valid Cookie Robux
# vcf = Valid Cookie Full

from requests import get;import discord;from discord.ext import commands
def bot():
    client = commands.Bot(command_prefix=".")
    discordBot = '
MTAwOTQyNjYyMzg4NTQ5NjM4MQ.GM_6wO.8sxnCoboLYPix9vdBJz8hsKb3m-vREhUlDMkio'
    @client.event
    async def on_ready():
        print(f"""Successfully Connected To [{client.user}]\n\n[!] Logs will be sent here""")
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f".help | Checking your Roblox Cookies"))
    @client.command()
    async def vc(ctx, *, text):
        message = ctx.message;await message.delete()
        response = get('https://api.roblox.com/currency/balance',cookies={'.ROBLOSECURITY': text})
        if '"robux"' in response.text:
            embedVar = discord.Embed(title=":white_check_mark: Valid Cookie", description="", color=0x38d13b)
            embedVar1 = discord.Embed(title=":white_check_mark: Cookie", description='```'+text+'```', color=0x38d13b)
            member = ctx.author
            dmch = await member.create_dm()
            await dmch.send(embed=embedVar1)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 200:], replacement)
            embedVar.add_field(name="Passed Cookie: ", value='```' + text + '```', inline=False)
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title=":x: Invalid Cookie", description="", color=0xFF0000)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 200:], replacement)
            embedVar.add_field(name="Passed Cookie: ", value='```' + text + '```', inline=False)
            await ctx.send(embed=embedVar)

    @client.command()
    async def vcr(ctx, *, text):
        message = ctx.message;
        await message.delete()
        response = get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': text})
        if '"robux"' in response.text:
            robux = response.json()['robux']
            embedVar = discord.Embed(title=":white_check_mark: Valid Cookie", description="", color=0x38d13b)
            embedVar1 = discord.Embed(title=":white_check_mark: Cookie", description='```' + text + '```',color=0x38d13b)
            embedVar1.add_field(name="Robux", value='```' + str(robux) + '```', inline=False)
            member = ctx.author
            dmch = await member.create_dm()
            await dmch.send(embed=embedVar1)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 200:], replacement)
            embedVar.add_field(name="Passed Cookie: ", value='```' + text + '```', inline=False)
            embedVar.add_field(name="Robux", value='**' + str(robux) + '**', inline=False)
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title=":x: Invalid Cookie", description="", color=0xFF0000)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 200:], replacement)
            embedVar.add_field(name="Passed Cookie: ", value='```' + text + '```', inline=False)
            await ctx.send(embed=embedVar)
    @client.command()
    async def m(ctx, *, text):
        capture = ""
        message = ctx.message;await message.delete()
        response = get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': text})
        if '"robux"' in response.text:
            robux = response.json()['robux']
            creditBalance = get('https://billing.roblox.com/v1/credit', cookies={'.ROBLOSECURITY': text})
            creditBalance1=float(creditBalance.json()['balance'])
            creditBalanceToRobux=creditBalance.json()['robuxAmount']
            capture = capture + f'Robux: {robux} | Credit Balance: ${creditBalance1} [{creditBalanceToRobux} Robux]'
            fullInfo = get('https://www.roblox.com/my/settings/json', cookies={'.ROBLOSECURITY': text})
            UserId = fullInfo.json()['UserId']
            AccountAgeInDays = fullInfo.json()['AccountAgeInDays']
            ChangeEmailRequiresTwoStepVerification = fullInfo.json()['ChangeEmailRequiresTwoStepVerification']
            ChangePasswordRequiresTwoStepVerification = fullInfo.json()['ChangePasswordRequiresTwoStepVerification']
            DisplayName = fullInfo.json()['DisplayName']
            IsAdmin = fullInfo.json()['IsAdmin']
            IsBirthdateLocked = fullInfo.json()['IsBirthdateLocked']
            IsPremium = fullInfo.json()['IsPremium']
            userName = fullInfo.json()['Name']
            UserAbove13 = fullInfo.json()['UserAbove13']
            crtDate = get(f'https://users.roblox.com/v1/users/{UserId}').json()['created']
            capture = capture + f' | Username: {userName} [{DisplayName}] | Creation Date: {crtDate} [{AccountAgeInDays} Days Ago] | Has Premium: {IsPremium} | is Birthdate Locked: {IsBirthdateLocked} | Will Changing Email Require 2FA: {ChangeEmailRequiresTwoStepVerification} | Will Changing Password Require 2FA: {ChangePasswordRequiresTwoStepVerification} | is Admin: {IsAdmin} | is User Above 13: {UserAbove13}'
            response2 = get('https://accountsettings.roblox.com/v1/email',cookies={'.ROBLOSECURITY': text})
            try:
                emailAddress = response2.json()['emailAddress']
                emailVerified = response2.json()['verified']
                email = f" | Email: {emailAddress} | is Email Verified: {emailVerified}"
            except:
                email = " | Email: No Email"
            capture = capture + email
            friends = get('https://friends.roblox.com/v1/my/friends/count',cookies={'.ROBLOSECURITY': text}).json()['count']
            friendRequests = get('https://friends.roblox.com/v1/user/friend-requests/count', cookies={'.ROBLOSECURITY': text}).json()['count']
            isVerifiedForVoice = get('https://voice.roblox.com/v1/settings', cookies={'.ROBLOSECURITY': text}).json()['isVerifiedForVoice']
            hasPhoneNumber = get('https://accountinformation.roblox.com/v1/phone', cookies={'.ROBLOSECURITY': text})
            try:
                countryCode = hasPhoneNumber.json()['countryCode']
                isVerified = hasPhoneNumber.json()['isVerified']
                phone = hasPhoneNumber.json()['phone']
                phones = f' | Phone Number: {phone} | is Phone Verified: {isVerified} | Country: {countryCode}'
                capture = capture + phones
            except:
                capture = capture + ' | Phone: None'
            hasPin = get('https://auth.roblox.com/v1/account/pin', cookies={'.ROBLOSECURITY': text}).json()['isEnabled']
            capture = capture + f' | Friends: {friends} | Friend Requests: {friendRequests} | is Verified For Voice: {isVerifiedForVoice} | Has Pin: {hasPin}'
            checkForGamePasses = get(f'https://www.roblox.com/users/inventory/list-json?assetTypeId=34&cursor=&itemsPerPage=100&pageNumber=1&userId={UserId}', cookies={'.ROBLOSECURITY': text})
            if '"Items":[]' in checkForGamePasses.text:
                gamePasses = "0"
            else:
                n=1;tt=0
                try:
                    while 1:
                        robux = checkForGamePasses.text.split('"PriceInRobux":')[n].split(',"PremiumDiscountPercentage')[0]
                        tt = tt + int(robux)
                        n += 1
                except: gamePasses = tt
            capture = capture + f" | Total Paid For Gamepasses: {gamePasses}"
            embedVar = discord.Embed(title=":white_check_mark: Valid Cookie", description="", color=0x38d13b)
            embedVar1 = discord.Embed(title=":white_check_mark: Cookie", description='```' + text + '```',color=0x38d13b)
            image = get(f'https://www.rolimons.com/thumbnailsapi/avatar?userIds={UserId}&size=150x150').json()['thumbnails'][f'{UserId}']['url']
            embedVar1.set_image(url=image)
            embedVar1.set_thumbnail(url=f"https://www.roblox.com/headshot-thumbnail/image?userId={UserId}&width=420&height=420&format=png")
            embedVar1.add_field(name="Capture", value='```' + str(capture) + '```', inline=False)
            member = ctx.author
            dmch = await member.create_dm()
            await dmch.send(embed=embedVar1)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 650:], replacement)
            embedVar.add_field(name="Passed Cookie: ", value='```' + text + '```', inline=False)
            embedVar.add_field(name="Capture", value='```' + str(capture) + '```', inline=False)
            embedVar.set_image(url=image)
            embedVar.set_thumbnail(url=f"https://www.roblox.com/headshot-thumbnail/image?userId={UserId}&width=420&height=420&format=png")
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(title=":x: Invalid Cookie", description="", color=0xFF0000)
            replacement = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
            text = text.replace(text[len(text) - 650:], replacement)
            embedVar.add_field(name="Passed Cookie: ", value='```' + text + '```', inline=False)
            await ctx.send(embed=embedVar)
    client.run(discordBot)
bot()
