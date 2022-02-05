import asyncio
import os
import random

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
    renvoie le texte en japonais le 'text' envoyé dans le salon 'ctx.channel'
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


def searchQuoi(message: str) -> str:
    """
    retire les caractères spéciaux de 'message', ainsi que les
    """
    newmessage = ''
    i = 0
    message = message.lower()
    erreurs = [' ', '!', '?', '.', ',', ':', ';', '∆', '÷', '<', '>', '+', '=', '°', '•', '/', '*', '^', '$', '-', ')',
               '&', ']', '_', "'", '"', '(', '[', '@', '€', '¥', '{', '}', '%', '#', '~', '√', '|', "\\"]
    while i < len(message):
        if message[i] not in erreurs:
            newmessage = newmessage + message[i]
        i = i + 1
    return newmessage


@bot.event
async def on_message(message):
    """
    renvoie "FEUR" si le 'message' finit par 'quoi'. Ne prend pas en compte la ponctuation.
    """
    message_content = str(message.content)
    message_content = searchQuoi(message_content)

    if message.author == bot.user:
        return

    if len(message_content) < 4:
        return

    verif = message_content[len(message_content) - 4] + message_content[len(message_content) - 3] + message_content[
        len(message_content) - 2] + message_content[len(message_content) - 1]
    if verif == 'quoi':
        await message.channel.send("FEUR")
        return


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
        await ctx.send \
            (f"{member.mention} n'a plus que {str(m)} minutes et {str(s)} secondes à vivre ! Une dernière danse "
             f"éventuellement ?")
    elif j == 0 and a == 0:
        await ctx.send \
            (f"{member.mention} n'a plus que {str(h)} heures, {str(m)} minutes et {str(s)} secondes à vivre ! "
             f"N'oubliez pas de fermer la porte à clé avant de partir !")
    elif a == 0:
        await ctx.send \
            (f"{member.mention} n'a plus que {str(j)} jours, {str(h)} heures, {str(m)} minutes et {str(s)} secondes à "
             f"vivre ! Un petit dernier test PCR avant le repos éternel ?")
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


bot.run('Normalement on est pas censé laisser un token comme ça')
