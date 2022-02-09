"""
CODE DU BOT FRANCOIS. Bienvenue, bonne lecture !
Si jamais il y a un manque de clareté quelque part, un conseil à donner, n'hésite pas à me le dire !
"""

import json
import os
import random
import asyncio
import youtube_dl

import discord.ext
from discord.ext.commands import CommandOnCooldown
from discord_components import DiscordComponents
from discord_slash import SlashCommand
from discord_slash.utils.manage_components import *

from param import *

slash = SlashCommand(bot, sync_commands=True)

os.chdir('C:\\Users\\sav\\PycharmProjects\\pythonProject')

bot = discord.ext.commands.Bot(command_prefix="!", description="Prefix : !")


@bot.event
async def on_ready():
    """
    renvoie "françois is ready !" dans le terminal au lancement du bot.
    attribue l'activité "[terminal]" à Francois.
    """
    print("françois is ready !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='[terminal]'))
    DiscordComponents(bot)


@bot.command()
async def stop(ctx):
    """
    provoque l'extinction de François.
    """
    if ctx.author.id == 299591668045185025:
        await ctx.send("Extinction de François en cours...")
        await asyncio.sleep(5)
        await ctx.send("François **OFF**.")
        return await bot.logout()
    else:
        await ctx.send("Vous n'avez pas l'autorisation de provoquer l'extinction de François.")
        return


@bot.command()
async def francois(ctx):
    """
    donne des informations sur François.
    """
    await ctx.message.delete()
    await ctx.send(
        "François est un personnage emblématique du manga Shonen 'Dr. STONE'. Il fait partie du royaume de la science "
        "et apparait pour la première fois dans le __tome 11__, au __chapitre 92__ __'Désirs = Justice'__ (l'animé "
        "n'y est pas encore rendu).\n\nIl est noté 5 étoiles en __cuisine__ et en __secrétariat__, et 3 étoiles en "
        "__endurance__.\nSecrétaire de la famille Nanami, son nom réel, son âge et son sexe sont inconnus (en "
        "réalité, ils ne le sont pas, mais son maître (Ryusui Nanami) n'en a rien à faire).\nD'allure plutôt frêle, "
        "du haut de son 1m60, il ne montre jamais la moindre trace de fatigue. Il donne donc l'impression d'avoir "
        "beaucoup d'endurance. C'est parce qu'à l'abri des regards, quand vient l'heure de se reposer, il le fait "
        "vraiment. Cela fait partie de son travail. Savoir gérer son énergie est un devoir de la plus haute "
        "importance pour un secrétaire !\n\n**Compétences de François :** Paperasse, réception, cuisine, "
        "baby-sitting, jardinage, ménage, soins médicaux, parle français, japonais, anglais, espagnol. C'est aussi le "
        "personnage préféré d'Antoine, tout manga confondu.")


@bot.command()
async def debug(ctx):
    """
    vérifie le bon fonctionnement de François.
    """
    await ctx.send("François vous reçoit parfaitement depuis la borne radio de la famille Nanami, prêt à vous servir !")


@bot.command()
async def mt(ctx):
    """
    supprime le message 'ctx' et souhaite une bonne journée dans le salon 'ctx.channel' à @everyone.
    """
    await ctx.message.delete()
    await ctx.send("François vous souhaite une excellente journée et plein de bonnes choses ! @everyone !")


@bot.command()
async def poll(ctx, text, *, message):
    """
    crée un sondage dans le salon 'ctx.channel' qui mentionne le rôle 'text' et qui prend en objet 'message'.
    """
    await ctx.message.delete()
    role = text
    await ctx.send(role)
    emb = discord.Embed(title=" SONDAGE", description=f"{message}")
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    await msg.add_reaction('✋')


@bot.command()
async def say(ctx, *text):
    """
    Si l'utilisateur est l'administrateur de Francois, fait écrire à François dans 'ctx.channel' le message 'text'
    """
    if ctx.author.id == 299591668045185025:
        await ctx.message.delete()
        await ctx.send(" ".join(text))
    else:
        await ctx.send("François n'écoute que son maître Ryusui et son maître Antoine.")


@bot.command()
async def nr(ctx):
    """
    renvoie dans 'ctx.channel' un nombre aléatoire entre 1 et 100.
    """
    await ctx.message.delete()
    await ctx.send(
        f"François a choisi un numéro aléatoire entre 1 et 100, comme vous lui avez demandé : {random.randint(1, 100)}")
    return


@bot.command()
async def eude(ctx):
    """
    renvoie la théorie du Eudisme dans le salon 'ctx.channel'
    """
    await ctx.message.delete()
    await ctx.send(
        "Selon la théorie du Eudisme, nous nous appelons tous Eude et devons tous respect envers Eude Le Magnifique. "
        "Or, nous nous appelons tous Eude, donc nous nous devons tous du respect.")
    return


@bot.command()
async def jap(ctx, *text):
    """
    renvoie le 'text' envoyé dans le salon 'ctx.channel', dans une version parodiée du japonais.
    """
    await ctx.message.delete()
    japt = '丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙'
    japtext = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char.lower()) - ord('a')
                nv = japt[index]
                japtext.append(nv)
            else:
                japtext.append(char)
        japtext.append("   ")
    await ctx.send("".join(japtext))


@bot.command()
async def insult(ctx, user: discord.Member):
    """
    fait insulter 'user' à François dans le salon 'ctx.channel'
    """
    await ctx.message.delete()
    await ctx.send(
        f"Et bien malheureusement, il est fort aisé de dire que {user.mention} n'est pas une personne très "
        f"recommandable...")


@bot.command()
async def question(ctx):
    """
    François répond à une question fermée une réponse aléatoire parmis la variable 'reponses'.
    """
    nbrep = random.randint(1, 100)
    if nbrep <= 30:
        await ctx.send("Oui")
        return
    elif nbrep <= 60:
        await ctx.send("Non")
        return
    else:
        reponses = ["C'est une possibilité...", "Peut-être...", "En considérant que les astres s'alignent....",
                    "Possiblement....", "Si Denis le veut bien.",
                    "François le sait mais ne vous en informera pas, sur ordre de Maître Ryusui.",
                    "François ne souhaite pas répondre à cette interrogation maléfique.",
                    "François pense que vous devriez interroger votre mère.", "Si Anne Lavalaye a vu la vierge.",
                    "La réponse se trouve dans votre question.", "C'est impossible.",
                    "Mais enfin, comme vous le savez, 1 et 1 font 2.",
                    "François n'a pas encore pu croiser les sources pour faire une méta analyse.",
                    "François va contacter un expert en la matière.", "https://tenor.com/view/non-mario-gif-10899016",
                    "Le pape devrait pouvoir vous répondre.",
                    "Les évènements A et B forment une partition de l'univers.\nD'après la formule des probabilités "
                    "totales : oui.",
                    "D'après le théorème de Cardilès, oui."]
        rep = reponses[random.randint(0, len(reponses) - 1)]
        await ctx.send(rep)
        return


@bot.command()
async def mineur(ctx):
    """
    Private joke
    """
    await ctx.send(f"Arrière chevalier {ctx.author.mention} !")
    return


@bot.command()
async def club(ctx):
    """
    attribue un club de football au hasard parmis 'cl' à l'utilisateur ctx.author.
    """
    cl = ['Paris Saint-Germain', 'Olympique de Marseille', 'Stade Rennais', 'Bayern Munich', 'Chelsea FC',
          'Manchester United FC', 'FC Copenhague', 'FC Barcelone', 'Real Madrid', 'Olympique Lyonnais', 'Juventus FC',
          'AC Milan', 'Ajax Amsterdam', 'Borussia Dortmund', 'Arsenal', 'Liverpool', 'Manchester City',
          'Tottenham Hotspur', 'Atlético Madrid', 'Nottingham Forest', 'Benfica Lisbonne', 'FC Club', 'Calv FC',
          'FC Silmi', 'FC Lorient', 'Blue Lock Eleven', 'Clermont Foot 63', 'VfL Wolfsburg', 'Paris FC',
          'Inazuma Japon', 'Karasuno', 'Juvisy FC']
    cb = random.choice(cl)
    await ctx.send(f"Le club qui vous est attribué est le club : {cb} !")
    return


@bot.event
async def on_command_error(ctx, exc):
    """
    si l'utilisateur est soumis a un cooldown sur une commande, alors em est renvoyé.
    """
    if isinstance(exc, CommandOnCooldown):
        em = discord.Embed(title=f"Arrière malotru !", description=f"Réessayez dans {exc.retry_after:.2f} secondes !")
        await ctx.send(embed=em)


@bot.command()
async def ttd(ctx):
    """
    Renvoie l'approximative future date de mort.
    """
    member = ctx.author
    s0 = random.randint(1, 50000000)
    m, h, j, a = 0, 0, 0, 0
    if s0 >= 60:
        m = s0 // 60
    s = s0 % 60
    if m >= 60:
        h = m // 60
        m = m % 60
    if h >= 24:
        j = h // 24
        h = h % 24
    if j >= 365:
        a = j // 365
        j = j % 365
    if m == 0 and h == 0 and j == 0 and a == 0:
        await ctx.send(f"{member.mention} n'a plus que {str(s)} secondes à vivre ! Une dernière parole ? ")
    elif h == 0 and j == 0 and a == 0:
        await ctx.send(
            f"{member.mention} n'a plus que {str(m)} minutes et {str(s)} secondes à vivre ! Une dernière danse éventuellement ?")
    elif j == 0 and a == 0:
        await ctx.send(
            f"{member.mention} n'a plus que {str(h)} heures, {str(m)} minutes et {str(s)} secondes à vivre ! N'oubliez pas de fermer la porte à clé avant de partir !")
    elif a == 0:
        await ctx.send(
            f"{member.mention} n'a plus que {str(j)} jours, {str(h)} heures, {str(m)} minutes et {str(s)} secondes à vivre ! Un petit dernier test PCR avant le repos éternel ?")
    elif a != 0:
        await ctx.send \
            (f"{member.mention} en a encore pour {str(a)} années, {str(j)} jours, {str(h)} heures, {str(m)} minutes "
             f"et {str(s)} secondes avant de mourir ! N'oubliez pas de relire intégralement au moins"
             f" {random.randint(1000, 5000)} fois Berserk avant de monter au ciel !")
    return


@bot.command()
async def covid(ctx):
    """
    Renvoie le résultat d'un test PCR.
    """
    cov = random.randint(1, 100)
    res = False
    if cov < 26:
        res = True
    if res:
        await ctx.send \
            ("Vous êtes **positif** au virus de la COVID-19.\nVeuillez prévenir les personnes avec qui vous avez été "
             "en contact durant ces 72 dernières heures :\nil est possible que vous les ayez contaminé.\nVous devez "
             "aussi restez chez vous pendant au moins 7 jours. Merci de votre coopération.")
    else:
        await ctx.send \
            ("Vous êtes **négatif** au virus de la COVID-19.\nun pass sanitaire d'une durée de 24 heures (à compter "
             "de la réception de ce message) vous sera automatiquement envoyé par mail sous 48 heures.")


@bot.command()
async def manga(ctx, role: discord.role.Role = None, num: int = None):
    """
    Renvoie un embed d'annonce de sortie du tome 'int' du manga 'role'.
    """
    await ctx.message.delete()
    if ctx.author.id != 299591668045185025:
        await ctx.send("Vous n'êtes pas autorisé à faire d'annonce de sortie de manga.")
        return
    else:
        if role == None and num == None:
            await ctx.send("Vous devez citer un manga ainsi qu'un numéro de tome.")
            return
        else:
            if role == None and num != None:
                await ctx.send("Vous devez citer un manga.")
                return
            elif num == None and role != None:
                await ctx.send("Vous devez citer un numéro de tome.")
                return
            else:
                buttons = [
                    create_button(
                        style=ButtonStyle.blue,
                        label="FRANCE",
                        custom_id="fr"
                    ),
                    create_button(
                        style=ButtonStyle.blue,
                        label="JAPON",
                        custom_id="jp"
                    )
                ]
                actionsraw = create_actionrow(*buttons)
                fait_choix = await ctx.send("Pays de sortie :", components=[actionsraw])

                def check(m):
                    return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

                button_ctx = await wait_for_component(bot, components=actionsraw, check=check)
                if button_ctx.custom_id == "jp":
                    await ctx.send(content=f"||{role.mention}||")
                    em = discord.Embed(title="SORTIE DE TOME AU JAPON !", color=role.color)
                    em.add_field(name="MANGA :", value=role.mention)
                    em.add_field(name="TOME :", value=num)
                    await ctx.send(embed=em)
                else:
                    await ctx.send(content=f"||{role.mention}||")
                    em = discord.Embed(title="SORTIE DE TOME !", color=role.color)
                    em.add_field(name="MANGA :", value=role.mention)
                    em.add_field(name="TOME :", value=num)
                    await ctx.send(embed=em)


@bot.command()
async def chap(ctx, role: discord.role.Role = None, num: int = None):
    """
    Renvoie un embed d'annonce de sortie du chapitre 'int' du manga 'role'.
    """
    await ctx.message.delete()
    if ctx.author.id != 299591668045185025:
        await ctx.send("Vous n'êtes pas autorisé à faire d'annonce de chapitre.")
        return
    else:
        if role == None and num == None:
            await ctx.send("Vous devez citer un manga ainsi qu'un numéro de chapitre.")
            return
        else:
            if role == None and num != None:
                await ctx.send("Vous devez citer un manga.")
                return
            elif num == None and role != None:
                await ctx.send("Vous devez citer un numéro de chapitre.")
                return
            else:
                await ctx.send(f"||{role.mention}||")
                em = discord.Embed(title="SORTIE DE CHAPITRE !", color=role.color)
                em.add_field(name="MANGA :", value=role.mention)
                em.add_field(name="CHAPITRE :", value=num)
                await ctx.send(embed=em)
    return


##################################### JEU DE CARTES-PERSONNAGES ###################################

"""
Jeu de cartes-personnages : JCP (Jean-Christophe-Paul lolilolxdptdr)
"""

# Ici, on définit les prix des différents niveaux de prestige des cartes.
rar = [0, 2500, 4500, 10000, 25000, 50000, 100000, 1000000]

# Ici, tous les réglages de toutes les cartes.
# Cela se présente de la manière suivante:
# {prenom, nom, manga, lien d'image, prestige, prix correspondant, indice, points d'attaque, points de défense, points d'intelligence}
# Il est nécessaire de suivre ce système tout en veillant à vérifier ses informations et à les présenter correctement.
# Présenter correctement les informations permet de gagner un temps monstrueux dans le code de François.

cards = [{'prenom': 'Eren', 'nom': 'JAEGER', 'manga': 'Shingeki no Kyojin',
          'url': 'https://images-ext-2.discordapp.net/external/gj-JhfgMkGpJYfm916Picy5xYhf9pNZhGGIuzZlln-o/https/imgur.com/vk8yfPv.png',
          'rarete': 6, 'prix': rar[6], 'num': 1, 'attack': 306, 'defense': 100, 'intelligence': 354},
         {'prenom': 'Mikasa', 'nom': 'ACKERMAN', 'manga': 'Shingeki no Kyojin',
          'url': 'https://cdn.shopify.com/s/files/1/0502/5506/9351/products/product-image-660195173_600x600.jpg',
          'rarete': 4, 'prix': rar[4], 'num': 2, 'attack': 200, 'defense': 88, 'intelligence': 50},
         {'prenom': 'Armin', 'nom': 'ARLELT', 'manga': 'Shingeki no Kyojin',
          'url': 'https://pbs.twimg.com/media/EWPRWRuWsAAQ9q2.jpg', 'rarete': 4, 'prix': rar[4], 'num': 3, 'attack': 66,
          'defense': 22, 'intelligence': 250},
         {'prenom': 'Livaï', 'nom': 'ACKERMAN', 'manga': 'Shingeki no Kyojin',
          'url': 'http://pm1.narvii.com/7104/33d48653fdd074188feb7205769b3e5fcf996558r1-500-616v2_00.jpg', 'rarete': 4,
          'prix': rar[4], 'num': 4, 'attack': 200, 'defense': 68, 'intelligence': 70},
         {'prenom': 'Hange', 'nom': 'ZOE', 'manga': 'Shingeki no Kyojin',
          'url': 'https://pbs.twimg.com/media/En7Q7sTXUAEVjWy.png', 'rarete': 3, 'prix': rar[3], 'num': 5, 'attack': 42,
          'defense': 42, 'intelligence': 141},
         {'prenom': 'Erwin', 'nom': 'SMITH', 'manga': 'Shingeki no Kyojin',
          'url': 'https://i.pinimg.com/736x/3e/cf/1a/3ecf1a996c96947f1644f95a3b51dec1.jpg', 'rarete': 4, 'prix': rar[4],
          'num': 6, 'attack': 144, 'defense': 50, 'intelligence': 144},
         {'prenom': 'Reiner', 'nom': 'BRAUN', 'manga': 'Shingeki no Kyojin',
          'url': 'https://cdn.myanimelist.net/images/characters/2/434573.jpg', 'rarete': 5, 'prix': rar[5], 'num': 7,
          'attack': 200, 'defense': 200, 'intelligence': 107},
         {'prenom': 'Guts', 'nom': '-', 'manga': 'Berserk',
          'url': 'https://u.livelib.ru/character/1000005924/o/6rieok69/o-o.jpeg', 'rarete': 6, 'prix': rar[6], 'num': 8,
          'attack': 400, 'defense': 200, 'intelligence': 160},
         {'prenom': 'Griffith', 'nom': '-', 'manga': 'Berserk',
          'url': 'https://www.myutaku.com/media/personnage/424.jpg', 'rarete': 6, 'prix': rar[6], 'num': 9,
          'attack': 400, 'defense': 100, 'intelligence': 260},
         {'prenom': 'Zodd', 'nom': "L'IMMORTEL", 'manga': 'Berserk',
          'url': 'https://i.pinimg.com/originals/6b/1a/6a/6b1a6a72ead402776666d859cc06a746.jpg', 'rarete': 5,
          'prix': rar[5], 'num': 10, 'attack': 300, 'defense': 150, 'intelligence': 57},
         {'prenom': 'Isidro', 'nom': '-', 'manga': 'Berserk',
          'url': 'https://cdn.myanimelist.net/images/characters/9/101956.jpg', 'rarete': 3, 'prix': rar[3], 'num': 11,
          'attack': 100, 'defense': 75, 'intelligence': 50},
         {'prenom': 'Puck', 'nom': '-', 'manga': 'Berserk',
          'url': 'https://i.pinimg.com/564x/e5/66/f4/e566f4faa677250e9667ad918307d34a.jpg', 'rarete': 5, 'prix': rar[5],
          'num': 12, 'attack': 25, 'defense': 300, 'intelligence': 182},
         {'prenom': 'Overhaul', 'nom': '-', 'manga': 'My Hero Academia',
          'url': 'https://images-ext-1.discordapp.net/external/1F9mZUCNn8eS7hBKWoD-xjSUF8nDvLA3fFqJ3sE_g78/https/media.discordapp.net/attachments/472313197836107780/650847985407885346/GYK4tuY.png',
          'rarete': 5, 'prix': rar[5], 'num': 13, 'attack': 175, 'defense': 150, 'intelligence': 182},
         {'prenom': 'Casca', 'nom': '-', 'manga': 'Berserk',
          'url': 'https://i.pinimg.com/550x/38/ce/52/38ce52501d5d0fa6753822e42d178b5c.jpg', 'rarete': 5, 'prix': rar[5],
          'num': 14, 'attack': 300, 'defense': 100, 'intelligence': 107},
         {'prenom': 'Izuku', 'nom': 'MIDORIYA', 'manga': 'My Hero Academia', 'url': 'https://i.imgur.com/9ZVqwMR.png',
          'rarete': 6, 'prix': rar[6], 'num': 15, 'attack': 300, 'defense': 300, 'intelligence': 160},
         {'prenom': 'Shoto', 'nom': 'TODOROKI', 'manga': 'My Hero Academia', 'url': 'https://i.imgur.com/r20r8cP.png',
          'rarete': 4, 'prix': rar[4], 'num': 16, 'attack': 200, 'defense': 38, 'intelligence': 100},
         {'prenom': 'Katsuki', 'nom': 'BAKUGO', 'manga': 'Berserk',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/607374138184826901/LCDja3Z.png',
          'rarete': 4, 'prix': rar[4], 'num': 17, 'attack': 300, 'defense': 30, 'intelligence': 8},
         {'prenom': 'All', 'nom': 'MIGHT', 'manga': 'My Hero Academia',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/548387244830883863/J4Aytmy.png',
          'rarete': 5, 'prix': rar[5], 'num': 18, 'attack': 400, 'defense': 57, 'intelligence': 50},
         {'prenom': 'Tomura', 'nom': 'SHIGARAKI', 'manga': 'My Hero Academia',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/607441132779077633/VH0ie55.png',
          'rarete': 5, 'prix': rar[5], 'num': 19, 'attack': 300, 'defense': 50, 'intelligence': 57},
         {'prenom': 'Senku', 'nom': 'ISHIGAMI', 'manga': 'Dr.STONE',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/683811788818612310/f3EQrEK.png',
          'rarete': 6, 'prix': rar[6], 'num': 20, 'attack': 30, 'defense': 30, 'intelligence': 700},
         {'prenom': 'Gen', 'nom': 'ASAGIRI', 'manga': 'Dr.STONE',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/700555854247755816/HsP3XZZ.png',
          'rarete': 5, 'prix': rar[5], 'num': 21, 'attack': 25, 'defense': 32, 'intelligence': 450},
         {'prenom': 'Momo', 'nom': 'YAOYOROZU', 'manga': 'My Hero Academia',
          'url': 'https://media.discordapp.net/attachments/872026548692209738/872046426371264553/gLJOLqv.png',
          'rarete': 3, 'prix': rar[3], 'num': 22, 'attack': 100, 'defense': 25, 'intelligence': 100},
         {'prenom': 'Francois', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://media.discordapp.net/attachments/872026548692209738/872090371113500702/WHqdN2Y.png',
          'rarete': 7, 'prix': rar[7], 'num': 23, 'attack': 380, 'defense': 380, 'intelligence': 380},
         {'prenom': 'Tsuyu', 'nom': 'ASUI', 'manga': 'My Hero Academia',
          'url': 'https://media.discordapp.net/attachments/872026548692209738/872046479857045554/b8ylcnY.png',
          'rarete': 2, 'prix': rar[2], 'num': 24, 'attack': 50, 'defense': 50, 'intelligence': 50},
         {'prenom': 'Ochako', 'nom': 'URARAKA', 'manga': 'My Hero Academia',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/748703664712974386/05lWtiW.png',
          'rarete': 3, 'prix': rar[3], 'num': 25, 'attack': 25, 'defense': 150, 'intelligence': 50},
         {'prenom': 'Eijiro', 'nom': 'KIRISHIMA', 'manga': 'My Hero Academia', 'url': 'https://i.imgur.com/LzkdIQe.png',
          'rarete': 2, 'prix': rar[2], 'num': 26, 'attack': 50, 'defense': 75, 'intelligence': 25},
         {'prenom': 'Eren', 'nom': 'JAEGER', 'manga': 'Shingeki no Kyojin',
          'url': 'https://images-ext-2.discordapp.net/external/IdHhaW_g3TsNlbtZ9GJ7k0O62X2VQANc4rns0l4DaTw/https/imgur.com/evOZYlZ.png',
          'rarete': 0, 'prix': rar[0], 'num': 27, 'attack': 0, 'defense': 0, 'intelligence': 0},
         {'prenom': 'Izuku', 'nom': 'MIDORIYA', 'manga': 'My Hero Academia',
          'url': 'https://media.discordapp.net/attachments/914892398918787174/939865053065265202/crop.png?width=325&height=558',
          'rarete': 0, 'prix': rar[0], 'num': 28, 'attack': 0, 'defense': 0, 'intelligence': 0},
         {'prenom': 'Guts', 'nom': '-', 'manga': 'Berserk',
          'url': 'https://images-ext-1.discordapp.net/external/vckvsf2Q94Gmbw3DAcO1NVjKzGOl8iGeDPR04PZFIqg/https/imgur.com/dTfwXmX.png',
          'rarete': 0, 'prix': rar[0], 'num': 29, 'attack': 0, 'defense': 0, 'intelligence': 0},
         {'prenom': 'Senku', 'nom': 'ISHIGAMI', 'manga': 'Dr.STONE',
          'url': 'https://media.discordapp.net/attachments/914892398918787174/939865653081423902/unknown.png?width=442&height=559',
          'rarete': 0, 'prix': rar[0], 'num': 30, 'attack': 0, 'defense': 0, 'intelligence': 0},
         {'prenom': 'Xeno', 'nom': 'HOUSTON WINGFIELD', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/PEmEibfW08iCUUdoE24o_CNDuCU259fdAH0gXZCUod8/https/imgur.com/AbrsLGE.png',
          'rarete': 5, 'prix': rar[5], 'num': 31, 'attack': 27, 'defense': 25, 'intelligence': 450},
         {'prenom': 'Stanley', 'nom': 'SNYDER', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/1Klz32Y47gTa16s1Ov2QScJ1bAui4hoUtyELR8piark/https/media.discordapp.net/attachments/472313197836107780/748766733363576882/9GY3K2u.png',
          'rarete': 5, 'prix': rar[5], 'num': 32, 'attack': 327, 'defense': 125, 'intelligence': 50},
         {'prenom': 'Byakuya', 'nom': 'ISHIGAMI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/gZyTGIYYOgULGz4XPz5sTgdY1Sd2k9zk6uoNOKgnWdY/https/media.discordapp.net/attachments/472313197836107780/650869393428971539/mQSlY8F.png',
          'rarete': 3, 'prix': rar[3], 'num': 33, 'attack': 75, 'defense': 75, 'intelligence': 75},
         {'prenom': 'Liliane', 'nom': 'WEINBERG', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/-Hb1B6Zop9nWQzQvrHOUjjN9UNEoQwcd-L5AuxxQIUU/https/media.discordapp.net/attachments/472313197836107780/669778085922603018/m30vi0Y.png',
          'rarete': 2, 'prix': rar[2], 'num': 34, 'attack': 25, 'defense': 25, 'intelligence': 100},
         {'prenom': 'Connie', 'nom': 'LEE', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/ibn9ww9uSg2W2kI5w-SERQc1I2javGe2ZDVRSDcfjmc/https/media.discordapp.net/attachments/472313197836107780/650871577843597341/3sKe2LA.png',
          'rarete': 1, 'prix': rar[1], 'num': 35, 'attack': 20, 'defense': 20, 'intelligence': 60},
         {'prenom': 'Shamil', 'nom': 'VOLKOV', 'manga': 'Dr.STONE',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/652297444075241480/tqxaHQL.png',
          'rarete': 1, 'prix': rar[1], 'num': 36, 'attack': 40, 'defense': 20, 'intelligence': 40},
         {'prenom': 'Yakov', 'nom': 'NIKITIN', 'manga': 'Dr.STONE',
          'url': 'https://cdn.myanimelist.net/images/characters/12/402305.jpg', 'rarete': 1, 'prix': rar[1], 'num': 37,
          'attack': 30, 'defense': 50, 'intelligence': 20},
         {'prenom': 'Darya', 'nom': 'NIKITINA', 'manga': 'Dr.STONE',
          'url': 'https://shikimori.one/system/characters/original/178270.jpg', 'rarete': 1, 'prix': rar[1], 'num': 38,
          'attack': 20, 'defense': 20, 'intelligence': 60},
         {'prenom': 'Rei37', 'nom': 'ISHIGAMI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/WHvfZA1a72ESQUVIqr95VbHs-U2gN4khjjjmHMX2gto/https/media.discordapp.net/attachments/872026548692209738/872141166328578058/fezeoNO.png',
          'rarete': 1, 'prix': rar[1], 'num': 39, 'attack': 0, 'defense': 0, 'intelligence': 100},
         {'prenom': 'Yuzuriha', 'nom': 'OGAWA', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/CvExmXjD77rtwh8-mKhrG1-0RmOAwEqmcjVQZmMgCCc/https/media.discordapp.net/attachments/472313197836107780/608433433802178570/9BplRFo.png',
          'rarete': 2, 'prix': rar[2], 'num': 40, 'attack': 25, 'defense': 25, 'intelligence': 100},
         {'prenom': 'Taiju', 'nom': 'OOKI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/_AvbLfpuUzyR97iOYfiwY4UY9zs4ftnkZt_yczKuVI8/https/media.discordapp.net/attachments/872026548692209738/872071581361401887/RQAyNkc.png',
          'rarete': 3, 'prix': rar[3], 'num': 41, 'attack': 100, 'defense': 100, 'intelligence': 25},
         {'prenom': 'Tsukasa', 'nom': 'SHISHIO', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/gGbiJxzV8MwCFE8I5mPw5FRdEZbuk8lyhyZK7VvJW00/https/imgur.com/UFY4xdF.png',
          'rarete': 5, 'prix': rar[5], 'num': 42, 'attack': 200, 'defense': 200, 'intelligence': 107},
         {'prenom': 'Kohaku', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/MFJgcC7w-GmvfDH_YJeqLTHAfK9ziywCcZlhp-zlk7M/https/media.discordapp.net/attachments/472313197836107780/608125696837156874/llFC3MV.png',
          'rarete': 3, 'prix': rar[3], 'num': 43, 'attack': 150, 'defense': 50, 'intelligence': 25},
         {'prenom': 'Alabaster', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/7/79/Alabaster.png/revision/latest?cb=20200215103617',
          'rarete': 1, 'prix': rar[1], 'num': 44, 'attack': 33, 'defense': 33, 'intelligence': 34},
         {'prenom': 'Sho', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/f/f1/Sho_Anime.png/revision/latest?cb=20210115203715&path-prefix=fr',
          'rarete': 1, 'prix': rar[1], 'num': 45, 'attack': 33, 'defense': 34, 'intelligence': 33},
         {'prenom': 'Suika', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/ogYkWbJiSapD_QnmZAKToe6z5Q79cT6s2SufZJKW7r0/https/media.discordapp.net/attachments/872026548692209738/872057312951558194/Tvm8e8P.png',
          'rarete': 4, 'prix': rar[4], 'num': 46, 'attack': 38, 'defense': 100, 'intelligence': 200},
         {'prenom': 'Chitan', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dublagem/images/1/18/Titan_DS.jpg/revision/latest?cb=20201115001707&path-prefix=pt-br',
          'rarete': 1, 'prix': rar[1], 'num': 47, 'attack': 20, 'defense': 60, 'intelligence': 20},
         {'prenom': 'Carbo', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/3/3e/Carbo_Anime_Infobox.png/revision/latest?cb=20191210073242',
          'rarete': 1, 'prix': rar[1], 'num': 48, 'attack': 25, 'defense': 55, 'intelligence': 20},
         {'prenom': 'Hagane', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://www.anime-planet.com/images/characters/thumbs/169837.jpg?t=1567819629', 'rarete': 1,
          'prix': rar[1], 'num': 49, 'attack': 25, 'defense': 50, 'intelligence': 25},
         {'prenom': 'Genbu', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/d/da/Genbu_Anime.png/revision/latest?cb=20210115205034&path-prefix=fr',
          'rarete': 1, 'prix': rar[1], 'num': 50, 'attack': 40, 'defense': 25, 'intelligence': 35},
         {'prenom': 'Diamond', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/6/6d/Dia_Portrait.png/revision/latest/top-crop/width/360/height/360?cb=20180901083948',
          'rarete': 1, 'prix': rar[1], 'num': 51, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Sango', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/0/08/Sango.png/revision/latest/top-crop/width/360/height/450?cb=20210525162114&path-prefix=es',
          'rarete': 1, 'prix': rar[1], 'num': 52, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Unmo', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://www.myutaku.com/media/personnage/178464.jpg', 'rarete': 1, 'prix': rar[1], 'num': 53,
          'attack': 25, 'defense': 50, 'intelligence': 25},
         {'prenom': 'Suzu', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/5/5e/Suzu.jpg/revision/latest/top-crop/width/360/height/450?cb=20210524031357&path-prefix=es',
          'rarete': 1, 'prix': rar[1], 'num': 54, 'attack': 20, 'defense': 40, 'intelligence': 40},
         {'prenom': 'Bery', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/0/00/Beryl_Portrait.png/revision/latest/top-crop/width/360/height/360?cb=20180901083946',
          'rarete': 1, 'prix': rar[1], 'num': 55, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Argo', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/2/25/Argo_Infobox.png/revision/latest?cb=20201110211145',
          'rarete': 1, 'prix': rar[1], 'num': 56, 'attack': 40, 'defense': 30, 'intelligence': 30},
         {'prenom': 'Magma', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/HRxL64sQKt8KTR81iGazqYmjAhSHGMXQKwbLryS5ofg/https/media.discordapp.net/attachments/472313197836107780/669744763267710976/LB5zJTb.png',
          'rarete': 2, 'prix': rar[2], 'num': 57, 'attack': 75, 'defense': 50, 'intelligence': 25},
         {'prenom': 'Ruri', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/ie9VQ0CxSrj02j4kpG1eKeJJggWGVkfx641sy8r77Us/https/media.discordapp.net/attachments/472313197836107780/633664284299231271/IN83Tsk.png',
          'rarete': 2, 'prix': rar[2], 'num': 58, 'attack': 25, 'defense': 25, 'intelligence': 100},
         {'prenom': 'Ruby', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/f5p1NluH6QYMugrDnOSdqdB3t7oOitevkpT9CUMUlfM/https/media.discordapp.net/attachments/872026548692209738/872102818926960710/oq7a4wm.png',
          'rarete': 1, 'prix': rar[1], 'num': 59, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Azura', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://cdn.anisearch.fr/images/character/cover/full/85/85712.webp', 'rarete': 1, 'prix': rar[1],
          'num': 60, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Chrome', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/i6S52lyYqmF46hFRmD3XeScjCtd2i9FKGfi8BG1uMbQ/https/media.discordapp.net/attachments/872026548692209738/872060188784488458/n7fbiqr.png',
          'rarete': 3, 'prix': rar[3], 'num': 61, 'attack': 50, 'defense': 50, 'intelligence': 125},
         {'prenom': 'Sagan', 'nom': '-', 'manga': 'Dr.STONE', 'url': 'https://cdn-us.anidb.net/images/main/238885.jpg',
          'rarete': 1, 'prix': rar[1], 'num': 62, 'attack': 25, 'defense': 50, 'intelligence': 25},
         {'prenom': 'Natori', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/9/9a/Natri_Talking.png/revision/latest?cb=20201030171834',
          'rarete': 1, 'prix': rar[1], 'num': 63, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Mantle', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/4/45/Mantle.png/revision/latest?cb=20210209104244',
          'rarete': 1, 'prix': rar[1], 'num': 64, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Kokuyo', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://www.myutaku.com/media/personnage/178454.jpg', 'rarete': 2, 'prix': rar[2], 'num': 65,
          'attack': 25, 'defense': 75, 'intelligence': 50},
         {'prenom': 'Saphir', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/f/f6/Sapphire-0.png/revision/latest?cb=20200204120430',
          'rarete': 1, 'prix': rar[1], 'num': 66, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Kuhjaku', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/d/d8/Kujaku_Portrait.png/revision/latest?cb=20190902034852',
          'rarete': 1, 'prix': rar[1], 'num': 67, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Shaberu', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/1/19/Shovel_Portrait.png/revision/latest?cb=20190928054818',
          'rarete': 1, 'prix': rar[1], 'num': 68, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'En', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/a/a4/En_Portrait.png/revision/latest?cb=20190902035848',
          'rarete': 1, 'prix': rar[1], 'num': 69, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Alumi', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/4/45/Alumi_Anime.png/revision/latest/top-crop/width/360/height/450?cb=20210427093730&path-prefix=fr',
          'rarete': 1, 'prix': rar[1], 'num': 70, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Kinro', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/AhP6a9ydky4YahzFQzseePPmKmXTrv3L1L-SWYQPIxY/https/imgur.com/WCHZAnD.png',
          'rarete': 3, 'prix': rar[3], 'num': 71, 'attack': 100, 'defense': 50, 'intelligence': 75},
         {'prenom': 'Shirogane', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/c/ca/Shirogane_Anime_Infobox.png/revision/latest/top-crop/width/360/height/360?cb=20200323063518',
          'rarete': 1, 'prix': rar[1], 'num': 72, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Jasper', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/c/ca/Jasper_Anime.jpg/revision/latest?cb=20201207150143&path-prefix=fr',
          'rarete': 1, 'prix': rar[1], 'num': 73, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Garnet', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/c/c4/Garnet_Anime.png/revision/latest?cb=20210122134306&path-prefix=fr',
          'rarete': 1, 'prix': rar[1], 'num': 74, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Chalk', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/8/84/Chalk_Anime_personnage.png/revision/latest?cb=20210115202839&path-prefix=fr',
          'rarete': 1, 'prix': rar[1], 'num': 75, 'attack': 50, 'defense': 40, 'intelligence': 10},
         {'prenom': 'Namari', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/c/c4/Namari_Portrait.png/revision/latest?cb=20201210103602',
          'rarete': 1, 'prix': rar[1], 'num': 76, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Ganen', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://www.myutaku.com/media/personnage/178452.jpg', 'rarete': 1, 'prix': rar[1], 'num': 77,
          'attack': 25, 'defense': 40, 'intelligence': 35},
         {'prenom': 'Kaseki', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/v_vuN8ONUOXwNvqq8R6rDa8GZHaubwgCbAgIV8qJXfw/https/media.discordapp.net/attachments/472313197836107780/650871976134443008/U5a860g.png',
          'rarete': 4, 'prix': rar[4], 'num': 78, 'attack': 50, 'defense': 138, 'intelligence': 150},
         {'prenom': 'Ginro', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/YtSSPGPZ_W5r4W6snjtEPCdgnMu0dUU4WSzWJYlB5Qk/https/media.discordapp.net/attachments/872026548692209738/873582556501663794/1c6UnV1.png',
          'rarete': 3, 'prix': rar[3], 'num': 79, 'attack': 100, 'defense': 100, 'intelligence': 25},
         {'prenom': 'Soyuz', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/ysnHQFMxjrM3-gJ890jDfp_0_tta6YFv4fGn9eTrC4k/https/media.discordapp.net/attachments/472313197836107780/700569696444874773/vJK9alC.png',
          'rarete': 2, 'prix': rar[2], 'num': 80, 'attack': 50, 'defense': 50, 'intelligence': 50},
         {'prenom': 'Turquoise', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/0/0a/Turquoise_Anime.jpg/revision/latest?cb=20201207150511&path-prefix=fr',
          'rarete': 1, 'prix': rar[1], 'num': 81, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Hyoga', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/0cTGat3klgtFJzw1UZ74Ub8boWaCuCNMfHkNIfzp3VQ/https/media.discordapp.net/attachments/472313197836107780/670890700874842122/dWogsu3.png',
          'rarete': 4, 'prix': rar[4], 'num': 82, 'attack': 150, 'defense': 50, 'intelligence': 138},
         {'prenom': 'Homura', 'nom': 'MOMIJI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/8So8PpJe3uSVy1TdMgiiIZURHlyKEcGdcjdhzunHL8U/https/imgur.com/fQaUXv0.png',
          'rarete': 3, 'prix': rar[3], 'num': 83, 'attack': 150, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Ukyo', 'nom': 'SAIONJI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/Cy9wQL3-Rc9G7a8A7Z_gq6YGlSAsZ14YgXacAhdJud8/https/media.discordapp.net/attachments/872026548692209738/872077969621909504/X7eCbY0.png',
          'rarete': 3, 'prix': rar[3], 'num': 84, 'attack': 50, 'defense': 50, 'intelligence': 125},
         {'prenom': 'Nikki', 'nom': 'HANADA', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/PTIRKhbazcWNnZKtpqe_HD-Ts2MyT-7zz81YR3Je1DA/https/media.discordapp.net/attachments/872026548692209738/872110300428664862/TCnLeFi.png',
          'rarete': 2, 'prix': rar[2], 'num': 85, 'attack': 50, 'defense': 50, 'intelligence': 50},
         {'prenom': 'You', 'nom': 'UEI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/HNdp-rOHNCF5sTFNKlqE-oRSJqu05XnNw2y48wr28bQ/https/media.discordapp.net/attachments/472313197836107780/749106867258785882/BIwZ4Sd.png',
          'rarete': 2, 'prix': rar[2], 'num': 86, 'attack': 50, 'defense': 50, 'intelligence': 50},
         {'prenom': 'Mirai', 'nom': 'SHISHIO', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/OXGel09EKmPAORwWGgkTr0S6FLm-gfwcyYZchf_rGEM/https/media.discordapp.net/attachments/872026548692209738/872189853532569650/Xa02zbH.png',
          'rarete': 2, 'prix': rar[2], 'num': 87, 'attack': 25, 'defense': 25, 'intelligence': 100},
         {'prenom': 'Tetsuya', 'nom': 'KINOMOTO', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/dr-stone/images/3/3f/Tetsuya_Kinomoto_%28anime%29.png/revision/latest?cb=20210325173900',
          'rarete': 1, 'prix': rar[1], 'num': 88, 'attack': 25, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Ryusui', 'nom': 'NANAMI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/gx8u_2sPSw5WmQ6PuSKxtf1ITSlAJlpIXsIcrpo8bGk/https/imgur.com/KFTTlyn.png',
          'rarete': 5, 'prix': rar[5], 'num': 89, 'attack': 250, 'defense': 107, 'intelligence': 150},
         {'prenom': 'Minami', 'nom': 'HOKUTOZAI', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/47ZJGi0QI_e9UYqy3Nstzcxs5f8trgw4H3YBILM4gOY/https/media.discordapp.net/attachments/472313197836107780/669428897779154944/tLjMA4Q.png',
          'rarete': 3, 'prix': rar[3], 'num': 90, 'attack': 25, 'defense': 25, 'intelligence': 175},
         {'prenom': 'Senku', 'nom': 'MECHA', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/KPl884eqG0sjyB0bN0j0mffLRlI63copg55XGb-_m3s/https/media.discordapp.net/attachments/872026548692209738/872097046021169162/MwFltMx.png',
          'rarete': 2, 'prix': rar[2], 'num': 91, 'attack': 0, 'defense': 0, 'intelligence': 150},
         {'prenom': 'Why', 'nom': 'MAN', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/villains/images/f/f1/Whyman_%28DrStone%29.png/revision/latest?cb=20200912231525',
          'rarete': 5, 'prix': rar[5], 'num': 92, 'attack': 169, 'defense': 169, 'intelligence': 169},
         {'prenom': 'Amaryllis', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/32CEP_6WDDq9jqm3hbQLULdYvKkR7xrg-sAx9tgmjlM/https/media.discordapp.net/attachments/472313197836107780/620066738599624725/QHwluRr.png',
          'rarete': 3, 'prix': rar[3], 'num': 93, 'attack': 25, 'defense': 25, 'intelligence': 175},
         {'prenom': 'Kirisame', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/8GEhgMmU3mNMLFp2iI_SJ7T0dXx-RKwPK5Bix_w6KAA/https/media.discordapp.net/attachments/472313197836107780/723017580826198016/BhRxrOr.png',
          'rarete': 3, 'prix': rar[3], 'num': 94, 'attack': 150, 'defense': 25, 'intelligence': 50},
         {'prenom': 'Mozu', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/ca5fMw5ZCtuDlIuTp4-fKxyqYaMpof0vvP-qvlsZaJA/https/media.discordapp.net/attachments/472313197836107780/683840633596936238/iqN5Ofn.png',
          'rarete': 3, 'prix': rar[3], 'num': 95, 'attack': 175, 'defense': 25, 'intelligence': 25},
         {'prenom': 'Ibara', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/aCQ8y4WcbWG9ab4DFX18m7iTAHAAc3U5X1-_6fhVILY/https/media.discordapp.net/attachments/472313197836107780/700102798578024508/aEiG20T.png',
          'rarete': 5, 'prix': rar[5], 'num': 96, 'attack': 250, 'defense': 50, 'intelligence': 207},
         {'prenom': 'Oarashi', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://static.wikia.nocookie.net/drstone/images/d/dc/Oarashi_Manga.jpg/revision/latest/top-crop/width/360/height/450?cb=20201207184330&path-prefix=fr',
          'rarete': 2, 'prix': rar[2], 'num': 97, 'attack': 100, 'defense': 25, 'intelligence': 25},
         {'prenom': 'Matsukaze', 'nom': '-', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-1.discordapp.net/external/hPL7F3QBJWlTtWB_K50KUDdlRsfQQri6ZjmwIK8euyE/https/media.discordapp.net/attachments/472313197836107780/723663534180925542/EbBYdtm.png',
          'rarete': 3, 'prix': rar[3], 'num': 98, 'attack': 100, 'defense': 50, 'intelligence': 75},
         {'prenom': 'Luna', 'nom': 'WRIGHT', 'manga': 'Dr.STONE',
          'url': 'https://images-ext-2.discordapp.net/external/68FRVAXf5JwB7HkUpeLFHvmNDi3NF6eLKlqulz7nizE/https/media.discordapp.net/attachments/872026548692209738/873582754841911347/qMsFaK1.png',
          'rarete': 2, 'prix': rar[2], 'num': 99, 'attack': 25, 'defense': 25, 'intelligence': 100},
         {'prenom': 'Nada', 'nom': 'Might', 'manga': 'My Hero Academia',
          'url': 'https://images-ext-1.discordapp.net/external/2ZPBhrOtRz9J1HCifRh3j8s45gQXXdt-9ncgp-vL550/https/imgur.com/0qh1ZZh.png',
          'rarete': 7, 'prix': rar[7], 'num': 100, 'attack': 380, 'defense': 380, 'intelligence': 380},
         {'prenom': 'Ichigo', 'nom': 'KUROSAKI', 'manga': 'Bleach',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/547313673618849802/Q3zXdxc.png',
          'rarete': 6, 'prix': rar[6], 'num': 101, 'attack': 400, 'defense': 260, 'intelligence': 100},
         {'prenom': 'Gon', 'nom': 'FREECSS', 'manga': 'Hunter x Hunter',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/548304744716828694/qwAipui.png',
          'rarete': 6, 'prix': rar[6], 'num': 102, 'attack': 360, 'defense': 200, 'intelligence': 200},
         {'prenom': 'Musashi', 'nom': 'MIYAMOTO', 'manga': 'Vagabond',
          'url': 'https://media.discordapp.net/attachments/472313197836107780/553756734058135565/1dlB5Hj.png',
          'rarete': 6, 'prix': rar[6], 'num': 103, 'attack': 460, 'defense': 100, 'intelligence': 200}]

# Repose-liens
# Repose-liens
# Repose-liens
# Repose-liens
# Repose-liens
# Repose-liens
# au dessus, un espace pour reposer des liens si besoin.


# Ici, on définit la liste des mangas concernés par les cartes 'cards'. Si on rajoute un personnage d'un nouvel univers, il faut le nommer dans la list 'mangas'.
mangas = ['Shingeki no Kyojin', 'Berserk', 'My Hero Academia', 'Dr.STONE', 'Bleach', 'Hunter x Hunter', 'Vagabond']


def compteetoile(text: str) -> int:
    """ Renvoie le nombre d'émojis '⭐' dans le str text.
    """
    i = 0
    cpt = 0
    while i < len(text):
        if text[i] == '⭐':
            cpt = cpt + 1
        i = i + 1
    return cpt


# 'number' est la list des symboles correspondants aux chiffres
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def verifnombre(text):
    """
    Vérifie que 'text' est exclusivement constitué de chiffres.
    """
    i = 0
    while i < len(text):
        if text[i] not in number:
            return False
        i = i + 1
    return True


@bot.command()
async def search(ctx, recherche):
    """
    Permet de chercher une carte-personnage par un indice, par un nombre d'étoiles, par un nom de manga.
    """
    if verifnombre(recherche):
        for item in cards:
            if item['num'] == int(recherche):
                couleur = discord.Color.light_grey()
                if item['rarete'] == 2:
                    couleur = discord.Color.dark_green()
                elif item['rarete'] == 3:
                    couleur = discord.Color.blue()
                elif item['rarete'] == 4:
                    couleur = discord.Color.red()
                elif item['rarete'] == 5:
                    couleur = discord.Color.dark_gold()
                elif item['rarete'] == 6:
                    couleur = discord.Color.gold()
                elif item['rarete'] == 7:
                    couleur = discord.Color.purple()

                if item['nom'] == '-':
                    nom = ''
                else:
                    nom = item['nom']

                if item['rarete'] == 0:
                    em = discord.Embed(title=f'{item["prenom"]} {nom} | édition limitée ', color=couleur)
                    em.add_field(name='Manga :', value=f'{item["manga"]}')
                    em.add_field(name="Prestige :", value="Inestimable")
                    em.set_image(url=f"{item['url']}")

                    await ctx.send(embed=em)
                    return

                em = discord.Embed(title=f'{item["prenom"]} {nom}', color=couleur)
                em.add_field(name='Manga :', value=f'{item["manga"]}')
                em.add_field(name="Prestige :", value=f"{item['rarete'] * '⭐'}")
                em.add_field(name="Prix :", value=f"{item['prix']} PM")
                em.set_image(url=f"{item['url']}")

                await ctx.send(embed=em)
                return

        await ctx.send("Aucune carte-personnage ne correspond à cet indice.")
        return

    if compteetoile(recherche) > 0:
        nb = compteetoile(recherche)
        print(nb)
        i = 0
        message = ''
        while i < len(cards):
            if cards[i]['rarete'] == nb:

                if cards[i]['nom'] == '-':
                    nom = ''
                else:
                    nom = cards[i]['nom']

                message = message + f'{cards[i]["prenom"]} {nom} | {cards[i]["manga"]} | {cards[i]["rarete"] * "⭐"} | {cards[i]["prix"]} PM \n ---------------------------------------------- \n'
            i = i + 1
        if message == '':
            await ctx.send(f"Aucun personnage ne possède {nb}⭐ de prestige.")
            return
        else:
            await ctx.send(message)
            return


def majuscule(mess: str) -> str:
    """
    Retire l'intégralité des majuscules de 'mess' et renvoie son équivalent en minuscules.
    """
    symbmini = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    symbmaj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    i = 0
    newmess = ''
    while i < len(mess):
        if mess[i] not in symbmaj:
            newmess = newmess + mess[i]
        else:
            j = 0
            while j < len(symbmaj) and symbmaj[j] != mess[i]:
                j = j + 1
            newmess = newmess + symbmini[j]
        i = i + 1
    return newmess


@bot.command()
async def stats(ctx, psge: str = None):
    """
    Affiche les points d'attributs du personnage 'psge'.
    """
    if psge == None:
        await ctx.send("Vous devez citer une carte-personnage.")
        return
    for item in cards:
        if majuscule(item['prenom']) == majuscule(psge) or majuscule(item['nom']) == majuscule(psge):
            couleur = discord.Color.light_grey()
            if item['rarete'] == 2:
                couleur = discord.Color.dark_green()
            elif item['rarete'] == 3:
                couleur = discord.Color.blue()
            elif item['rarete'] == 4:
                couleur = discord.Color.red()
            elif item['rarete'] == 5:
                couleur = discord.Color.dark_gold()
            elif item['rarete'] == 6:
                couleur = discord.Color.gold()
            elif item['rarete'] == 7 or item['rarete'] == 0:
                couleur = discord.Color.purple()

            if item['nom'] == '-' or item['nom'] == 'ENFANT':
                nom = ''
            else:
                nom = item['nom']

            em = discord.Embed(title=f'{item["prenom"]} {nom}', color=couleur)
            em.set_thumbnail(url=f'{item["url"]}')
            em.add_field(name="ATT :", value=f'{item["attack"]} ⚔')
            em.add_field(name='DEF :', value=f'{item["defense"]} 🛡')
            em.add_field(name='INT :', value=f'{item["intelligence"]} 🧠')
            em.add_field(name='STA :', value=f'{item["rarete"]} ⭐')
            em.add_field(name='PPM :', value=f'{item["prix"]} 💰')

            await ctx.send(embed=em)
            return

    await ctx.send("Aucune carte-personnage ne correspond.")
    return


@bot.command()
async def buy(ctx, psge: str = None):
    """
    Renvoie une proposition d'achat de la carte 'psge' à ctx.author. S'il a suffisamment d'argent et qu'il l'accepte, il reçoit la carte dans son inventaire.
    (modification du fichier 'cards.json' si c'est le cas)
    """
    if psge == None:
        await ctx.send("Vous devez citer une carte-personnage.")
        return
    for item in cards:
        if majuscule(item['prenom']) == majuscule(psge) or majuscule(item['nom']) == majuscule(psge):
            couleur = discord.Color.light_grey()
            if item['rarete'] == 2:
                couleur = discord.Color.dark_green()
            elif item['rarete'] == 3:
                couleur = discord.Color.blue()
            elif item['rarete'] == 4:
                couleur = discord.Color.red()
            elif item['rarete'] == 5:
                couleur = discord.Color.dark_gold()
            elif item['rarete'] == 6:
                couleur = discord.Color.gold()
            elif item['rarete'] == 7:
                couleur = discord.Color.purple()

            if item['nom'] == '-' or item['nom'] == 'ENFANT':
                nom = ''
            else:
                nom = item['nom']

            em = discord.Embed(title=f'{item["prenom"]} {nom}', color=couleur)
            em.add_field(name='Manga :', value=f'{item["manga"]}')
            em.add_field(name='Prestige :', value=f"{item['rarete'] * '⭐'}")
            em.add_field(name='Prix :', value=f"{item['prix']} PM")
            em.set_image(url=f'{item["url"]}')

            await ctx.send(embed=em)

            users = await get_cards_data()
            if item['num'] in users[str(ctx.author.id)]['indices']:
                await ctx.send(f"Vous possédez déjà la carte-personnage de {item['prenom']}.")
                return

            bal = await update_bank(ctx.author)
            if bal[0] < item['prix']:
                await ctx.send("Vous n'avez pas suffisamment de Points-Marrons !")
                return

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            await asyncio.sleep(5)
            await ctx.send(
                f"----------------------------------------------\nÊtes-vous sûr de vouloir acheter {item['prenom']} ?")

            try:
                msg = await bot.wait_for('message', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await ctx.send("Vous n'avez pas répondu suffisament rapidement, l'achat est annulé.")
                return

            if msg.content == 'o' or msg.content == 'O' or msg.content == 'y' or msg.content == 'Y' or msg.content == 'oui' or msg.content == 'yes' or msg.content == 'YES' or msg.content == 'OUI' or msg.content == 'Yes' or msg.content == 'Oui':
                await update_cards(ctx.author, item['num'])
                await update_bank(ctx.author, -item['prix'])
                await ctx.send(f"-{item['prix']} PM....")
                await asyncio.sleep(1)
                await ctx.send(f"Vous avez acheté {item['prenom']} ! Merci pour votre achat !")
                return

            else:
                await ctx.send("Revenez plus tard !")
                return

    await ctx.send("Personnage non trouvé.")
    return


def trouvecarte(indice: int):
    """
    Cherche une carte-personnage dans la liste 'cards' grâce à son indice (['num]}
    """
    for item in cards:
        if indice == item['num']:
            return item


@bot.command()
async def get_cards_data():
    """
    Récupère les informations du fichier 'cards.json'.
    """
    with open('cards.json', 'r') as f:
        users = json.load(f)
    return users


@bot.command()
async def setcards(ctx):
    """
    Crée un 'inventaire de cartes' à ctx.author, sauf si son inventaire est déjà existant.
    """
    user = ctx.author
    users = await get_cards_data()

    if str(user.id) in users:
        await ctx.send("Inventaire déjà existant.")
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['indices'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                          0, 0]

    with open('cards.json', 'w') as f:
        json.dump(users, f)
        await ctx.send("Inventaire créé !")
    return True


def trouv0(L: list):
    """
    Cherche la première case vide (case contenant l'int 0) dans une list L.
    """

    i = 0
    while i < len(L) and L[i] != 0:
        i = i + 1
    return i


@bot.command()
async def update_cards(user, indice: str):
    """
    Modifie l'inventaire de l'utilisateur 'user' avec l'indice 'indice' dans la première case vide.
    """
    users = await get_cards_data()

    whereiszero = trouv0(users[str(user.id)]['indices'])
    users[str(user.id)]['indices'][whereiszero] = int(indice)

    with open('cards.json', 'w') as f:
        json.dump(users, f)

    bal = users[str(user.id)]['indices']
    return bal


@bot.command()
async def lcards(ctx):
    """
    Renvoie la liste des cartes-personnages possédées par ctx.author.
    """
    users = await get_cards_data()
    await ctx.send('--------------------------------------------------------------------------- \n')
    for item in cards:
        if item["num"] in users[str(ctx.author.id)]['indices']:
            if item['nom'] == '-':
                nom = ''
            else:
                nom = item['nom']

            couleur = discord.Color.light_grey()
            if item['rarete'] == 2:
                couleur = discord.Color.dark_green()
            elif item['rarete'] == 3:
                couleur = discord.Color.blue()
            elif item['rarete'] == 4:
                couleur = discord.Color.red()
            elif item['rarete'] == 5:
                couleur = discord.Color.dark_gold()
            elif item['rarete'] == 6:
                couleur = discord.Color.gold()
            elif item['rarete'] == 7 or item['rarete'] == 0:
                couleur = discord.Color.purple()

            em = discord.Embed(title=f'**{item["prenom"]} {nom}**', color=couleur)
            em.add_field(name='Manga :', value=f'{item["manga"]}')
            em.add_field(name='Prestige :', value=f'{item["rarete"] * "⭐"}')
            em.set_thumbnail(url=f'{item["url"]}')
            await ctx.send(embed=em)
            await ctx.send('--------------------------------------------------------------------------- \n')
    return


##################################### FIN DU CODE DU JEU DE CARTES-PERSONNAGES ###################################


##################################### SYSTÈME ÉCONOMIQUE ##########################################################


@bot.command(aliases=['balance'])
async def money(ctx, member: discord.Member = None):
    """
    affiche le point économique de 'member' (sa banque, son porte-marrons...).
    """
    if member == None:
        arg = ctx.author
    else:
        arg = member
    await open_account(arg)
    user = arg
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]['wallet']
    bank_amt = users[str(user.id)]['bank']
    rotule_amt = users[str(user.id)]['rotul']

    em = discord.Embed(title=f'BRM - Banque Rotulaire et Marronière de {arg.display_name}:',
                       color=discord.Color.red())
    em.add_field(name="Porte-Marrons", value=wallet_amt)
    em.add_field(name='Banque-Marron', value=bank_amt)
    em.add_field(name='Points Rotules', value=rotule_amt)
    await ctx.send(embed=em)


@bot.command()
async def batou(ctx, member: discord.Member = None, amount=None):
    """
    Commande exclusive qui permet à des utilisateurs précis de donner 'amount' Points-Rotules à 'member'.
    """
    if ctx.author.id != 381467630478950400 and ctx.author.id != 299591668045185025:
        await ctx.send("Vous n'êtes pas le Dieu des Rotules et vous ne possédez pas le Haki des Rotules !")
        return
    else:
        if member == None and amount == None:
            ctx.send("Vous n'avez ni indiqué de membre ni indiqué de montant !")
            return
        elif member == None:
            ctx.send("Vous n'avez pas indiqué de membre à qui donner des points rotules !")
            return
        else:
            if amount == None:
                ctx.send("Vous n'avez pas indiqué de montant à donner.")
                return
            else:
                await update_rotule(member, amount)
                if int(amount) > 1:
                    await ctx.send \
                        (f"{member.mention} a reçu {amount} Points Rotules du Dieu des Rotules ! Félicitations !")
                elif int(amount) == 1:
                    await ctx.send \
                        (f"{member.mention} a reçu {amount} Point Rotule du Dieu des Rotules ! Félicitations !")
                elif int(amount) < 1:
                    await ctx.send(
                        f'{member.mention} a perdu {abs(amount)} Points Rotules... François est navré...')
                return


@bot.command()
async def give(ctx, member: discord.Member = None, amount=None):
    """
    Commande exclusive qui permet à l'administrateur d'ajouter 'amount' Points-Marrons à la banque de 'member'.
    """
    if ctx.author.id != 299591668045185025:
        await ctx.send("Vous n'êtes pas le Dieu des Marrons !")
        return
    else:
        if member == None and amount == None:
            ctx.send("Vous n'avez ni indiqué de membre ni indiqué de montant !")
            return
        elif member == None:
            ctx.send("Vous n'avez pas indiqué de membre à qui donner des Points Marrons !")
            return
        else:
            if amount == None:
                ctx.send("Vous n'avez pas indiqué de montant à donner.")
                return
            else:
                await update_bank(member, amount)
                if int(amount) > 1:
                    await ctx.send \
                        (f"{member.mention} a reçu {str(amount)} Points-Marrons du Dieu des Marrons ! Félicitations !")
                elif int(amount) == 1:
                    await ctx.send \
                        (f"{member.mention} a reçu {str(amount)} Point-Marron du Dieu des Marrons ! Félicitations !")
                elif int(amount) == 0:
                    await ctx.send \
                        (f"Le Dieu des Marrons a fait une blague de très mauvais goût et a donné 0 Point-Marron à {member.mention}!")

                elif int(amount) < 0:
                    amount = abs(int(amount))
                    await ctx.send(
                        f"Le Dieu des Marrons a retiré {str(amount)} Points-Marrons à {member.mention}...")
                return


@bot.command()
async def recupit(ctx, amount=None):
    """
    Permet à ctx.author de récupérer 'amount' Points-Marrons de sa banque.
    """
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Entrez le montant s'il vous plaît.")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("Vous n'avez pas suffisamment d'argent.")
        return

    if amount < 0:
        await ctx.send("Le montant doit être supérieur à 0 !")
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, (-1) * amount, "bank")

    await ctx.send(f'Vous avez récupéré {str(amount)} Points-Marrons de votre banque!')


@bot.command()
async def deposit(ctx, amount=None):
    """
    Permet à ctx.author de déposer 'amount' Points-Marrons dans sa banque.
    """
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Entrez le montant s'il vous plaît.")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Vous n'avez pas suffisamment d'argent.")
        return

    if amount < 0:
        await ctx.send("Le montant doit être supérieur à 0 !")
        return

    await update_bank(ctx.author, (-1) * amount)
    await update_bank(ctx.author, amount, "bank")

    await ctx.send(f'Vous avez déposé {str(amount)} Points-Marrons dans votre banque!')


@bot.command()
async def send(ctx, member: discord.Member, amount=None):
    """
    Permet à ctx.author d'envoyer 'amount' Points-Marrons à la banque de 'member s'il en a les moyens.
    """
    await open_account(ctx.author)
    await open_account(member)

    if amount == None:
        await ctx.send("Entrez le montant s'il vous plaît.")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("Vous n'avez pas suffisamment d'argent.")
        return

    if amount < 0:
        await ctx.send \
            (f"Vous ne pouvez pas voler des Points-Marrons de cette manière à {member.mention} enfin! À quoi pensiez-vous, brigand des mers du Nord ?!")
        return

    await update_bank(ctx.author, (-1) * amount)
    await update_bank(member, amount, "bank")

    await ctx.send(f'{ctx.author} a donné {str(amount)} Points-Marrons à la banque de {member.mention}!')


async def open_account(user):
    """
    Provoque l'ouverture d'un compte en banque à 'user'.
    """
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 0
        users[str(user.id)]['rotul'] = 0

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    """
    Récupère les informations du fichier 'mainbank.json'.
    """
    with open('mainbank.json', 'r') as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode='wallet'):
    """
    Modifie la balance de Points-Marrons de 'user' de 'change' Points-Marrons dans son 'mode' (soit sa banque, soit son porte-monnaie).
    """
    users = await get_bank_data()

    users[str(user.id)][mode] += int(change)

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank'], users[str(user.id)]['rotul']
    return bal


async def update_rotule(user, change):
    """
    Modifie la balance de Points-Rotules de 'user', de 'change' Points-Rotules.
    """
    users = await get_bank_data()

    users[str(user.id)]['rotul'] += int(change)

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank'], users[str(user.id)]['rotul']
    return bal


@bot.command()
async def liste(ctx):
    """
    Affiche la liste des id des utilisateurs ainsi que leurs Points-Marrons.
    """
    users = await get_bank_data()
    somme = 0
    for user in users:
        tamt = int(users[user]['wallet']) + int(users[user]['bank'])
        somme = somme + tamt
        await ctx.send(f"{user} a {tamt} Points-Marrons")
    await ctx.send(str(somme))


@bot.command()
async def lb(ctx, x=5):
    """
    Affiche le classement des utilisateurs les plus riches en Points-Marrons et en Points-Rotules.
    """
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        tamt = int(users[user]['wallet']) + int(users[user]['bank'])
        leader_board[tamt] = name
        total.append(tamt)

    total = sorted(total, reverse=True)

    page1 = discord.Embed(title=f'TOP {x} des plus riches en Points-Marrons.',
                          description='Cela représente **la somme** de la banque et du Porte-Marrons.',
                          color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = await bot.fetch_user(id_)
        name = member.name
        page1.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index = index + 1

    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        tamt = int(users[user]['rotul'])
        leader_board[tamt] = name
        total.append(tamt)

    total = sorted(total, reverse=True)

    page2 = discord.Embed(title=f'TOP {x} des plus riches en Points-Rotules.',
                          description="Cela représente les gens les plus drôles dans l'ordre décroissant.",
                          color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = await bot.fetch_user(id_)
        name = member.name
        page2.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index = index + 1

    bot.lbpages = [page1, page2]
    buttons = ['◀', '▶']
    current = 0
    msg = await ctx.send(embed=bot.lbpages[current])

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        try:
            reaction, user = await bot.wait_for('reaction_add', check=lambda reaction,
                                                                             user: user == ctx.author and reaction.emoji in buttons,
                                                timeout=60.0)
        except asyncio.TimeoutError:
            embed = bot.lbpages[current]
            embed.set_footer(text="temps écoulé.")
            await msg.clear_reactions()

        else:
            previous_page = current

            if reaction.emoji == '◀':
                if current == 0:
                    current = 1
                else:
                    current = 0

            else:
                if current == 1:
                    current = 0
                else:
                    current = 1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.lbpages[current])


@bot.command(pass_context=True)
@commands.cooldown(1, 60 * 60 * 3, commands.BucketType.user)
async def claim(ctx):
    """
    Donne une quantité aléatoire de Points-Marrons à ctx.author dans son porte-marrons. Utilisable une fois toutes les 3 heures.
    """
    await ctx.send("Arrêtez avec ça bande de ptits cons.")
    return

    nb = random.randint(1, 100)
    gain = 0
    if nb == 1:
        gain = 0
        await ctx.send("QUELLE CATASTROPHE !!!!!!!")
    elif 1 < nb <= 71:
        gain = random.randint(1, 122)
    elif 71 < nb <= 89:
        gain = random.randint(123, 174)
        await ctx.send("OH !")
    elif 89 < nb <= 99:
        gain = random.randint(175, 300)
        await ctx.send("WOAAAAH !!! C'EST FOU !!!")
    elif nb == 100:
        if random.randint(1, 100) == 100:
            gain = 50000
            await ctx.send("Impossible...")
            await asyncio.sleep(3)
            await ctx.send("Selon les calculs de François, cet évènement a 1 chance sur 10000 de se produire....")
            await asyncio.sleep(3)
            await ctx.send("Mesdames et messieurs, @everyone, l'impossible s'est produit !!!")
        else:
            gain = 5000
            await ctx.send \
                ("VOUS AVEZ GAGNÉ LE GROS LOT ! C'EST EXCEPTIONNEL CE QUI SE PASSE CE SOIR !!!!\n C'EST SENSATIONNEL !!!!! BRAVO !!!!! VOUS AVEZ LE TICKET GAGNANT !!!!!")

    await update_bank(ctx.author, gain)
    if gain > 1:
        await ctx.send(f"Vous avez gagné {gain} Points-Marrons !")
        return
    else:
        await ctx.send(f"Vous avez gagné {gain} Point-Marron ....")
        return


##################################### FIN DU CODE DU SYSTÈME ÉCONOMIQUE ###################################


@bot.command(pass_context=True)
@commands.cooldown(1, 60 * 2, commands.BucketType.user)
async def pileface(ctx):
    """
    Jeu du Pile ou Face. Utilisable une fois toutes les deux minutes.
    """
    await ctx.send("Arrêtez avec ça bande de ptits cons.")
    return
    gen = random.randint(1, 100)

    buttons = [
        create_button(
            style=ButtonStyle.blue,
            label="PILE",
            custom_id="pile"
        ),
        create_button(
            style=ButtonStyle.danger,
            label="FACE",
            custom_id="face"
        )
    ]

    actionrows = create_actionrow(*buttons)

    fait_choix = await ctx.send("Pile ou Face ?", components=[actionrows])

    def check(m):
        return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id

    button_ctx = await wait_for_component(bot, components=actionrows, check=check)
    pio = button_ctx.custom_id
    if pio == 'pile':
        inv = 'face'
    else:
        inv = 'pile'

    def check2(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Combien de Points-Marrons voulez-vous parier ?")

    try:
        msg = await bot.wait_for('message', timeout=10.0, check=check2)
    except asyncio.TimeoutError:
        await ctx.send("Vous n'avez pas répondu suffisament rapidement, le Pile ou Face est annulé.")
        return

    amount = int(msg.content)

    if amount <= 0:
        await ctx.send("Vous devez rentrer un montant d'une valeur positive.")
        return

    bal = await update_bank(ctx.author)
    print(bal[0])

    if int(bal[0]) < amount:
        await ctx.send("Vous n'avez pas suffisamment de Points-Marrons pour en parier autant !")
        return

    await asyncio.sleep(1)
    await ctx.send(f"Vous avez parié **{amount}** Points-Marrons sur **{pio}**.")
    await asyncio.sleep(2)
    await ctx.send("François lance la pièce, c'est parti !")
    await asyncio.sleep(1)
    await ctx.send("...")
    await asyncio.sleep(3)

    if gen == 100:
        await ctx.send("INCROYABLE !!! QUELLE CHANCE !!!! **TRANCHE** !!!!")
        await asyncio.sleep(2)
        await update_bank(ctx.author, 10 * amount)
        await ctx.send(f"VOUS AVEZ GAGNÉ **{10 * amount}** POINTS-MARRONS !!!!")
        return
    elif gen <= 5:
        await ctx.send("ARRRGHG !.. GEN A TRAFIQUÉ LA PIÈCE !!!")
        await asyncio.sleep(2)
        await update_bank(ctx.author, -(2 * amount))
        await ctx.send(
            f"Vous avez perdu **{2 * amount}** Points-Marrons... François est confus... François accourt faire son rapport à Maître Ryusui.")
        return
    elif 6 <= gen <= 10:
        await ctx.send("ARRRGHG !.. GEN A TRAFIQUÉ LA PIÈCE !!!")
        await asyncio.sleep(2)
        await update_bank(ctx.author, 2 * amount)
        await ctx.send(
            f"Vous avez gagné **{2 * amount}** Points-Marrons! François est ravi pour vous, mais Gen n'a qu'à bien se tenir !")
        return


    else:

        pf = random.randint(1, 2)
        if pf == 1:
            res = True
        else:
            res = False

        if res == True:
            await ctx.send(f"Bravo, la réponse était bien **{pio}** !")
            await asyncio.sleep(1)
            await update_bank(ctx.author, amount)
            await ctx.send(f"Vous avez gagné **{amount}** Points-Marrons, félicitations !")

        else:
            await ctx.send(f"Miséricorde ! La réponse était **{inv}** !")
            await asyncio.sleep(1)
            await update_bank(ctx.author, (-1) * amount)
            await ctx.send(f"Vous avez perdu **{amount}** Points-Marrons...")


def convert(time):
    """
    Permet de convertir un temps donné en secondes en jours, heures, minutes, secondes.
    """
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@bot.command()
@commands.has_role("giveaway")
async def giveaway(ctx):
    """
    Permet à un possesseur du rôle 'giveaway' d'organiser un giveaway.
    """
    await ctx.send("Lancement du concours...")
    await ctx.send("S'il vous plaît, répondez à ces quelques questions pour préparer au mieux le concours.")
    await ctx.send("Veuillez répondre en moins de 15 secondes.")

    for i in range(3):
        await asyncio.sleep(1)
        await ctx.send("...")

    questions = ["Dans quel channel voulez-vous organiser le concours ?",
                 "Quelle durée voulez vous imposer au concours ? (s|m|h|d)",
                 "Quel est la récompense de votre concours ?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await bot.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Vous n'avez pas répondu suffisament rapidement, le concours est annulé.")
            return
        else:
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send \
            (f"Vous n'avez pas mentionné de channel correctement. Essayez de cette manière : {ctx.channel.mention}")
        return

    channel = bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"Vous n'avez pas répondu avec une unité correcte. Utilisez les lettres s, m, h, ou d.")
        return
    elif time == -2:
        await ctx.send(f"Le temps doit être sous forme d'entier. Utilisez un entier s'il vous plait.")
        return

    prize = answers[2]

    await ctx.send(f"Le concours aura lieu dans le channel {c_id} et se terminera dans {answers[1]}!")

    embed = discord.Embed(title="Concours !", description=f"{prize}", color=ctx.author.color)

    embed.add_field(name="Organisé par:", value=ctx.author.mention)
    embed.set_footer(text=f"Fin dans {answers[1]} !")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")
    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Bravo à {winner.mention} qui a gagné {prize} !")


@bot.command()
async def petition(ctx):
    """
    Permet à ctx.author d'organiser une pétition.
    """
    await ctx.send \
        ("Pourquoi souhaitez vous faire une pétition ? Vous avez 30 secondes. Coefficient 3, la note comptera pour le 2e trimestre.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Vous n'avez pas répondu suffisament rapidement, la pétition est annulée.")
        return

    await ctx.send(f"{ctx.author.mention} a lancé une pétition ! voici ses propos:")
    message = await ctx.send(
        f'"**{msg.content}**"' + "\n Signez la pétition en appuyant sur le bouton ✅ ci-dessous.")
    await message.add_reaction('✅')
    return


@bot.command()
async def proces(ctx):
    """
    Permet à ctx.author d'organiser un procès.
    """
    await ctx.send("Désirs = Justice.\n Que désirez-vous?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=30.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("Vous n'avez pas répondu suffisament rapidement, le procès est annulé.")
        return

    await ctx.send(f"{ctx.author.mention} est pas content :```{msg.content}```")
    return


##################################### SYSTÈME MUSICAL ###################################


musics = {}
ytdl = youtube_dl.YoutubeDL()


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]


@bot.command()
async def leave(ctx):
    """
    Permet à ctx.author de provoquer la déconnexion de François.
    """
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []


@bot.command()
async def pause(ctx):
    """
    Permet à ctx.author de provoquer la pause de la musique en cours de lecture.
    """
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def resume(ctx):
    """
    Permet à ctx.author de provoquer la reprise de la musique en interruption
    """
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def skip(ctx):
    """
    Permet à ctx.author de passer la musique en cours de lecture.
    """
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    """
    Permet de jouer un son via François.
    """
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url
                                                                 ,
                                                                 before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        """
        Permet de basculer sur la première musique en attente dans la 'queue'.
        """
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    """
    Permet de lancer de la musique par l'intermédiaire de François.
    """
    await ctx.message.delete()
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"Je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)


##################################### FIN DU CODE DU SYSTÈME MUSICAL ###################################


bot.run('np')
