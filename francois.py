"""
CODE DU BOT FRANCOIS. Bienvenue, bonne lecture !
Si jamais il y a un manque de clareté quelque part, un conseil à donner, n'hésite pas à me le dire !
"""

from datetime import datetime
import json
import math
import os
import random
import asyncio
import youtube_dl
import discord.ext
from discord.ext.commands import CommandOnCooldown
import cartes
import gen
import discord
from discord.ext import commands
from keep_alive import keep_alive

bot = discord.ext.commands.Bot(command_prefix="!", description="Prefix : !")

@bot.event
async def on_ready():
  """
  renvoie "françois is ready !" dans le terminal au lancement du bot.
  attribue l'activité "[terminal]" à Francois.
  """
  print("françois is ready !")
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='[terminal]'))
  return

#############################################################################################################################
# Admin :


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
  return


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


@bot.command()
async def report(ctx, *, text: str):
  mod1 = await bot.fetch_user(299591668045185025)
  mod2 = await bot.fetch_user(381467630478950400)
  mod3 = await bot.fetch_user(659183608489181204)
  mods = [mod1,mod2,mod3]
  for mod in mods:
    await mod.send("`----------------------`")
    await mod.send(ctx.author)
    await mod.send(text)
    await mod.send("`----------------------`")
  await ctx.send("Rapport envoyé à l'équipe de François Industries. Merci infiniment de votre coopération !")  




def alt(id: int):
  alts = [828030828692766751, 851571034045284352, 558676593711513610, 817890207415271464]
  if id in alts:
    return True
  else:
    return False
    


@bot.command()
async def give(ctx, member: discord.Member = None, amount=None, type='m'):
  """
  Commande exclusive qui permet à l'administrateur d'ajouter 'amount' Points-Marrons à la banque de 'member'.
  """
  if ctx.author.id not in [299591668045185025,381467630478950400,659183608489181204]:
    await ctx.send("Vous n'êtes pas le Dieu des Marrons et des Rotules !")
    return
  else:
    if type == 'm':
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
          await update_info(member, amount)
          if int(amount) > 1:
            await ctx.send (f"{member.mention} a reçu {str(amount)} Points-Marrons du Dieu des Marrons ! Félicitations !")
          elif int(amount) == 1:
            await ctx.send(f"{member.mention} a reçu {str(amount)} Point-Marron du Dieu des Marrons ! Félicitations !")
          elif int(amount) == 0:
            await ctx.send(f"Le Dieu des Marrons a fait une blague de très mauvais goût et a donné 0 Point-Marron à {member.mention}!")
          elif int(amount) < 0:
            amount = abs(int(amount))
            await ctx.send(f"Le Dieu des Marrons a retiré {str(amount)} Points-Marrons à {member.mention}...")
            return
    elif type == 'r':
      if member == None and amount == None:
          ctx.send("Vous n'avez ni indiqué de membre ni indiqué de montant !")
          return
      elif member == None:
        ctx.send("Vous n'avez pas indiqué de membre à qui donner des Points-Rotules !")
        return
      else:
        if amount == None:
          ctx.send("Vous n'avez pas indiqué de montant à donner.")
          return
        else:      
          await update_info(member, amount, 'rotul')
          if int(amount) > 1:
            await ctx.send (f"{member.mention} a reçu {str(amount)} Points-Rotules du Dieu des Rotules ! Félicitations !")
          elif int(amount) == 1:
            await ctx.send(f"{member.mention} a reçu {str(amount)} Point-Rotule du Dieu des Rotules ! Félicitations !")
          elif int(amount) == 0:
            await ctx.send(f"Le Dieu des Rotules a fait une blague de très mauvais goût et a donné 0 Point-Rotule à {member.mention}!")
          elif int(amount) < 0:
            amount = abs(int(amount))
            await ctx.send(f"Le Dieu des Rotules a retiré {str(amount)} Points-Rotules à {member.mention}...")
            return
    
#############################################################################################################################

#############################################################################################################################
#Tuyauterie

@bot.event
async def on_command_error(ctx, exc):
  """
  si l'utilisateur est soumis a un cooldown sur une commande, alors em est renvoyé.
  """
  if isinstance(exc, CommandOnCooldown):
    adjectifs =['chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','chevalier','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru','malotru',"gros chien", "enculé de ta race", "énorme bg", "gros fils de pute"]
    if int(exc.retry_after//60) == 0:
      if (str(exc.retry_after % 60))[1] == '.':
        if (str(exc.retry_after % 60))[0] == '1':
          em = discord.Embed(title=f"Arrière {random.choice(adjectifs)} !",description=f"Réessayez dans `{(str(exc.retry_after % 60))[0]}` seconde !",color=discord.Color.red())
        elif (str(exc.retry_after % 60))[0] == '0':
          em = discord.Embed(title=f"Arrière {random.choice(adjectifs)} !",description=f"Réessayez dans un instant !",color=discord.Color.red())
        else:
          em = discord.Embed(title=f"Arrière {random.choice(adjectifs)} !",description=f"Réessayez dans `{(str(exc.retry_after % 60))[0]}` secondes !",color=discord.Color.red())
      else:
        em = discord.Embed(title=f"Arrière {random.choice(adjectifs)} !",description=f"Réessayez dans `{(str(exc.retry_after % 60))[0] + (str(exc.retry_after % 60))[1]}` secondes !",color=discord.Color.red())
    else:  
      em = discord.Embed(title=f"Arrière {random.choice(adjectifs)} !",description=f"Réessayez dans `{int(exc.retry_after // 60)}` minutes et `{(str(exc.retry_after % 60))[0] + (str(exc.retry_after % 60))[1]}` secondes !",color=discord.Color.red())
    await ctx.send(embed=em)






#############################################################################################################################

  
#############################################################################################################################
# François :

  
@bot.command()
async def francois(ctx):
  """
  donne des informations sur François.
  """
  await ctx.send("François est un personnage emblématique du manga Shonen 'Dr. STONE'. Il fait partie du royaume de la science "
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
  return


@bot.command()
async def debug(ctx):
  """
  vérifie le bon fonctionnement de François.
  """
  await ctx.send("François vous reçoit parfaitement depuis la borne radio de la famille Nanami, prêt à vous servir !")
  return

bot.remove_command('help')

@bot.command()
async def help(ctx):
  em = discord.Embed(title="HELP", description='Liste des commandes de François', color=discord.Color.gold())
  ###########################################################################################################################################
  em.add_field(name="INFORMATIONS :", value='`!help` : Envoie ce message.\n`!report [message]` : Envoie [message] directement chez François Industries.\n`!debug` : Vérifie que François fonctionne correctement.\n`!francois` : Affiche des informations sur François.\n`!constitution` : Affiche la constitution.', inline=False)
  ###########################################################################################################################################
  em.add_field(name='ÉCONOMIE :', value="`!pmclaim` (!pm) : Donne un nombre aléatoire de PM.\n`!money [user]` (!m) : Affiche le point-économique de [user].\n`!deposit [montant]` : permet de déposer [montant]PM en banque.\n`!recupit [montant]` : permet de récupérer [montant]PM de sa banque.\n`!send [@quelquun] [montant]` : permet d'envoyer [montant]PM à [@quelquun].", inline=False)
  ###########################################################################################################################################
  em.add_field(name="MANUMA :", value ="`!claim` : Donne une carte-personnage de Manuma aléatoire. Utilisable 1fois/30m.\n`!sell [1!2!3] / [all]` (!ms) : Permet de vendre les cartes d'indice [1,2,3]. !sell [all] permet de vendre l'intégralité de ses cartes d'un coup.\n`!search [x]` : Permet de chercher une carte-personnage via son prénom/nom [prenom/nom], ou par son indice [indice], ou par son niveau de prestige [étoiles], ou par son manga [manga].\n`!galeryshow` (!gs) : Permet de voir sa galerie en images.\n`!galerylist` (!gl) : Donne une liste de sa galerie en MP.\n`!changeordregalery` (!cog) : Permet de changer l'ordre de rangement de sa galerie.\n`!changefirstcard` (!cfc) : Permet de changer sa carte prioritaire.\n`!store [opt:indice]` : Permet d'accéder à la boutique. Si un [indice] est précisé, la boutique démarre à la page [indice].\n`!openbooster [indice]` (!ob) : Permet d'ouvrir un booster.\n`!openpanini [indice]` (!op) : Permet d'ouvrir un panini.\n`!useitem [indice]` (!ui) : Permet d'utiliser un item.")
  ###########################################################################################################################################
  em.add_field(name='UTILITAIRES :',value="`!chat` :Commande commémorative faisant référence à la période où Antoine pensait que cette même commande faisait disjoncter François.\n`!question [message]` : François répond à la question [message].\n`!profil` (!p) : Permet d'obtenir un certain nombre d'informations sur l'utilisateur demandé.\n`!mail [@quelquun] [message]` : Envoie [message] en MP à [@quelquun].",inline=False)
  ###########################################################################################################################################
  em.add_field(name='MATHS :', value="`!nr [opt:limite]` : Donne un nombre aléatoire entre 1 et 100. Si une limite est proposée, alors la limite n'est plus 100 mais est [limite].\n", inline=False)
  ###########################################################################################################################################
  await ctx.send(embed=em)

###############################################################################################################################


###############################################################################################################################
#lol

@bot.command(pass_context=True)
@commands.cooldown(1, 60 * 1, commands.BucketType.user)
async def chat(ctx):
  """
  Commande commémorative.
  """
  event = random.randint(1, 23)
    
  if event == 1: # évènement n°1
    nb = random.randint(-15000, 15000)
    await update_info(ctx.author, nb)
    if nb < 0:
      if nb < -10000:
        await ctx.send("https://images-ext-1.discordapp.net/external/eOCV8ttk8GK0rSsJYHaCXTMP9nLa1F6qERdA2nrPrJ0/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/ZLda9M-H1hYAAAPo/cat-cute.mp4")
      await ctx.send(f"Vous avez perdu {abs(nb)} Points-Marrons !")
    elif nb == 0:
      await ctx.send("Rien?")
    else:
      await ctx.send(f"Vous avez gagné {nb} Points-Marrons !")
    return
      
  elif event == 2: # évènement n°2
    await ctx.send(f"ET UN TONNERRE D'APLAUDISSEMENTS POUR LES RATS MESDAMES ET MESSIEURS !")
    return
      
  elif event == 3: # évènement n°3
    await ctx.send("Un chat.")
    return
      
  elif event == 4: # évènement n°4
    await ctx.send("48828125 est un diviseur de 10 puissance 14, le saviez-vous ?")
    return
    
  elif event == 5: # évènement n°5
    await ctx.reply("feur")
    return
    
  elif event == 6: # évènement n°6
    await ctx.send("Innondation de MPs en cours. François est navré. :)")
    mps = ['Êtes-vous présentement présent ?', "François est ici.",
           "François vous prévient, cela risque d'être long",
           'Coucou mère, François est présent dans la boîte visuelle.',
           "Ne pas se baigner dans la piscine de sulfate de cuivre. Merci d'avance.", "18h40",
           "Un petit bonjour de la part d'Antoine qui espère que vous passez une très bonne journée.",
           f"Êtes-vous là {ctx.author.mention} ?",
           "François sait pertinemment que vous souhaiter que cela cesse, malheureusement François n'est pas en mesure d'arrêter ce processus.", "François : Reboot, c'est comme François, mais en mieux.", "Imagine", "18h40", "Il est fort",
           "2² == 4", "AHHHHHHHH 23", "Buvez du jus de clémentine.", "STABILO BOSS", "feur", "Antoine saigne du nez",
           "l'EPS c'est vraiment pour les petits zizis", "Maths-Physique-SVT c'est vraiment pour les kékés",
           "HLP c'est pour les pouilleux", "Antoine a eu 14.5 en danse en EPS, oui c'est une revanche contre la vie.",
           "faites Maths complémentaires, j'ai des connaissances en mathématiques que vous n'avez pas, calculez, je vous calcule pas.", "L'arrêt de François 1.0.0.0 a été programmée plus d'un mois à l'avance, avant de revenir avec François : Reboot.",
           "Connaissez-vous la constante de Kaprekar ? Elle est égale à 6174.", "Hajime no Ippo > Haikyuu",
           "Volvic ou Evian ?", "Denis quel crack", "François > Joma", "Lisez Berserk", "Vous savez que Antoine a résolu Développement Décimal II, le dernier problème de MicroEuler, le 23 mars dernier ?",
           "Dr.STONE c'est fini SNIF SNIF", "1220703125 est aussi un diviseur de 10 puissance 14.",
           "tu veux du pain ?", "https://youtu.be/9S50a4rStNA", "NFFC for ever"]
    for i in mps:
        await ctx.author.send(i)
        await ctx.author.send("`-----------`")
        await asyncio.sleep(15)
    await ctx.author.send(
        "François est désoeuvré de vous avoir fait subir ces horreurs, néanmoins votre calvaire s'achève ici. Bonne journée à vous.")
    return
    
  elif event == 7: # évènement n°7
    await ctx.send("FÉLICITATIONS !!!!! VOUS AVEZ CORROMPU LE SERVEUR !")
    await ctx.send("zoadazoijdOJZIDOJoazdijoazdijoazjfpsqjdazpoijd")
    return
    
  elif event == 8: # évènement n°8
    await ctx.send("gratouillage de tétons.")
    await ctx.send("_gratte gratte_")
    return
    
  elif event == 9: # évènement n°9
    await ctx.send("AHHHHHHHHHHHHHHHHHHH 23")
    return
    
  elif event == 10: # évènement n°10
    await ctx.send(
        "https://i.notretemps.com/1400x787/smart/2021/05/03/trois-facons-de-distraire-votre-chat-a-la-maison.jpeg")
    return
  
  elif event == 11: # évènement n°11
    index = '```def index(L:list, x:int) -> int:```'
    await ctx.send(index)
    return
    
  elif event == 12: # évènement n°12
    await ctx.send("Qui est le petit fils du petit Gregory ?")
    return

  elif event == 13: # évènement n°13
    await ctx.send("Développement Décimal II oOIAZHDOIZAJDOIZJ")
    return

  elif event == 14: # évènement n°14
    await ctx.send("NFFC champions d'Europe, François vous aura prévenu.")
    return
    
  elif event == 15: # évènement n°15
    await ctx.send("DENIIIIIIIIIIIIIS HAAAAAAAAAAAAAAAAAAAAAN")
    return

  elif event == 16: # évènement n°16
    await ctx.send("Thaïs a envoyé valser une gomme à travers la salle par contre.")
    return

  elif event == 17: # évènement n°17
    await ctx.send("François risque de rerpleu.")
    return

  elif event == 18: # évènement n°18
    await ctx.send("LES TÉTONS DE FRANCOIS POINTENT AHHHHHHHHHHH")
    return

  elif event == 19: # évènement n°19
    await ctx.send("Un beau selfie de la François Industries, rien que pour vous.")
    await ctx.send("https://media.discordapp.net/attachments/830759403710971915/954065836526669885/unknown.png?width=966&height=559")
    return

  elif event == 20: # évènement n°20
    await ctx.send("En tout objectivité, François > Joma.")
    return

  elif event == 21: # évènement n°21
    await ctx.send("N'empêche Maths Expertes, y'a de l'idée.")
    return

  elif event == 22: # évènement n°22
    await ctx.send("Selon la théorie du Eudisme, nous nous appelons tous Eude et devons tous respect envers Eude Le Magnifique. "
        "Or, nous nous appelons tous Eude, donc nous nous devons tous du respect.")
    return

  else: # Dernier évènement
    await ctx.send("https://resize.programme-television.ladmedia.fr/r/670,670/img/var/premiere/storage/images/tele-7-jours/videos/bug-technique-m6/99133840-1-fre-FR/Bug-technique-M6.png")
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
                "totales : oui.", "Bien sûr", "Mme Bouchetal cherche des créneaux, le secrétariat vous communiquera les dates d'ici 4 ans.", "Avant la fin de One Piece", "Ah !", "Veuillez émettre cette problématique à votre ronda (daron en verlan).", "Poisson d'avril.", "أنت تمزح معي ?", "Vous jouez sur les mots.","D'après le théorème de Cardilès, oui."]
    rep = reponses[random.randint(0, len(reponses) - 1)]
    await ctx.send(rep)
    return





##############################################################################################################################

##############################################################################################################################
# Maths

@bot.command()
async def nr(ctx, limite:int=100):
  """
  renvoie dans 'ctx.channel' un nombre aléatoire entre 1 et 100.
  """
  await ctx.send(f"François a choisi un numéro aléatoire entre 1 et 100, comme vous lui avez demandé : {random.randint(1,limite)}")
  return

##############################################################################################################################

##############################################################################################################################
# Système économique

async def get_info_data():
  """
  Récupère les informations du fichier 'info.json'.
  """
  with open('info.json', 'r') as f:
    users = json.load(f)
  return users



async def open_account(user):
  """
  Provoque l'ouverture d'un compte informatique à 'user'.
  """
  users = await get_info_data()

  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}
    users[str(user.id)]['user'] = int(user.id)
    users[str(user.id)]['wallet'] = 0
    users[str(user.id)]['bank'] = 0
    users[str(user.id)]['rotul'] = 0
    users[str(user.id)]['boosters'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    users[str(user.id)]['paninis'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    users[str(user.id)]['items'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    users[str(user.id)]['vodkapple'] = False
    users[str(user.id)]['vol'] = [False,user.id]
    users[str(user.id)]['veutvol'] = [False,user.id]
    users[str(user.id)]['manga'] = "myheroacademia"
    users[str(user.id)]['firstcard'] = 0
    users[str(user.id)]['ordre'] = 0
    users[str(user.id)]['lists'] = {}
    users[str(user.id)]['indices'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  with open('info.json', 'w') as f:
    json.dump(users, f)
  return True



def trouveIndice(L: list, val: int) -> int:
  """
  Trouve l'emplacement de val dans la liste L. Renvoie -1 si val n'existe pas.
  """
  if val not in L:
    return -1
  for i in range(len(L)):
    if L[i] == val:
      return i


@bot.command()
async def update_info(user, change=0, mode='wallet', spe:str=None, user2: discord.Member=None):
  """
  Modifie le compte informatique de 'user'.
  """
  users = await get_info_data()
  
  if mode in ('boosters','paninis','indices', 'items'):
    if change < 0:
      if not abs(change) in users[str(user.id)][mode]:
        return
      indice = trouveIndice(users[str(user.id)][mode],abs(change))
      del users[str(user.id)][mode][indice]
      users[str(user.id)][mode].append(0)
    else:
      if mode == 'indices':
        if abs(change) in users[str(user.id)][mode]:
          return
      indice = trouveIndice(users[str(user.id)][mode],0)
      users[str(user.id)][mode][indice] = change

  elif mode in ('firstcard', 'ordre'):
    users[str(user.id)][mode] = int(change)
  elif mode == 'vodkapple':
    users[str(user.id)][mode] = not(users[str(user.id)][mode])
  elif mode == "manga":
    if spe != None and spe in mangas:
      users[str(user.id)][mode] = spe
  elif mode in ['vol','veutvol']:
    users[str(user.id)][mode] = [not(users[str(user.id)][mode][0]),user2.id]
    
  else:
    users[str(user.id)][mode] += int(change)
      
  with open('info.json', 'w') as f:
    json.dump(users, f)

  bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank'], users[str(user.id)]['rotul'], users[str(user.id)]['indices'], users[str(user.id)]['boosters']
  return bal




@bot.command(pass_context=True, aliases=['pm'])
#@commands.cooldown(1, 60 * 15, commands.BucketType.user)
async def pmclaim(ctx):
  """
  Donne une quantité aléatoire de Points-Marrons à ctx.author dans son porte-marrons. Utilisable une fois toutes les 15 minutes.
  """
  
  if await open_account(ctx.author):
    await ctx.send("Compte informatique en cours d'initialisation, veuillez patienter...")
    await asyncio.sleep(3)
    await ctx.send("Compte informatique initialisé ! Bon jeu !")
    
  if alt(ctx.author.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  nb = random.randint(1, 100)
  gain = 0
  if nb == 1:
    gain = 0
  elif 1 < nb <= 55:
    gain = random.randint(1, 700)
  elif 56 < nb <= 84:
    gain = random.randint(701, 1400)
  elif 85 < nb <= 99:
    gain = random.randint(1401, 2121)
  elif nb == 100:
    if random.randint(1, 100) == 100:
      gain = 500000
      await ctx.send("Impossible....")
      await asyncio.sleep(3)
      await ctx.send("Selon les calculs de François, cet évènement a 1 chance sur 10000 de se produire....")
      await asyncio.sleep(3)
      await ctx.send("Mesdames et messieurs, @everyone, l'impossible s'est produit !!!")
    else:
      gain = 50000
      await ctx.send("VOUS AVEZ GAGNÉ LE GROS LOT ! C'EST EXCEPTIONNEL CE QUI SE PASSE CE SOIR !!!!\n C'EST SENSATIONNEL !!!!! BRAVO !!!!! VOUS AVEZ LE TICKET GAGNANT !!!!!")

  await update_info(ctx.author, gain, 'wallet')
  if gain > 1:
    await ctx.send(f"Vous avez gagné `{gain}` Points-Marrons !")
    return
  else:
    await ctx.send(f"Vous avez gagné `{gain}` Point-Marron ....")
    return




@bot.command(aliases=['balance', 'm'])
async def money(ctx, member: discord.Member = None):
  """
  affiche le point économique de 'member' (sa banque, son porte-marrons...).
  """
  if member == None:
    user = ctx.author
  else:
    user = member

  if alt(user.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return
  
  
  if await open_account(user):
    await ctx.send("Compte informatique en cours d'initialisation, veuillez patienter...")
    await asyncio.sleep(3)
    await ctx.send("Compte informatique initialisé ! Bon jeu !")
    
  users = await get_info_data()

  wallet_amt = users[str(user.id)]['wallet']
  bank_amt = users[str(user.id)]['bank']
  rotule_amt = users[str(user.id)]['rotul']
  
  em = discord.Embed(title=f'BMR - Banque Marronière et Rotulaire de {user.display_name}:',color=discord.Color.red())
  em.add_field(name="Porte-Marrons", value=wallet_amt)
  em.add_field(name='Banque-Marrons', value=bank_amt)
  em.add_field(name='Points-Rotules', value=rotule_amt)
  await ctx.send(embed=em)


  
@bot.command()
async def recupit(ctx, amount=None):
  """
  Permet à ctx.author de récupérer 'amount' Points-Marrons de sa banque.
  """

  if alt(ctx.author.id):
      await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
      return

  await open_account(ctx.author)

  if amount == None:
    await ctx.send("Entrez le montant s'il vous plaît.")
    return

  bal = await update_info(ctx.author)

  amount = int(amount)
  if amount > bal[1]:
    await ctx.send("Vous n'avez pas suffisamment d'argent.")
    return

  if amount < 0:
    await ctx.send("Le montant doit être supérieur à 0 !")
    return

  await update_info(ctx.author, amount,'wallet')
  await update_info(ctx.author, (-1) * amount, "bank")

  await ctx.send(f'Vous avez récupéré {str(amount)} Points-Marrons de votre banque!')
  return



@bot.command()
async def deposit(ctx, amount=None):
  """
  Permet à ctx.author de déposer 'amount' Points-Marrons dans sa banque.
  """

  if alt(ctx.author.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  await open_account(ctx.author)

  if amount == None:
    await ctx.send("Entrez le montant s'il vous plaît.")
    return

  bal = await update_info(ctx.author)

  amount = int(amount)
  if amount > bal[0]:
    await ctx.send("Vous n'avez pas suffisamment d'argent.")
    return

  if amount < 0:
    await ctx.send("Le montant doit être supérieur à 0 !")
    return

  await update_info(ctx.author, (-1) * amount, 'wallet')
  await update_info(ctx.author, amount, "bank")

  await ctx.send(f'Vous avez déposé {str(amount)} Points-Marrons dans votre banque!')
  return





@bot.command()
async def send(ctx, member: discord.Member, amount=None):
  """
  Permet à ctx.author d'envoyer 'amount' Points-Marrons à la banque de 'member s'il en a les moyens.
  """

  if alt(ctx.author.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  if alt(member.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  await open_account(ctx.author)
  await open_account(member)

  if amount == None:
    await ctx.send("Entrez le montant s'il vous plaît.")
    return

  bal = await update_info(ctx.author)

  amount = int(amount)
  if amount > bal[0]:
    await ctx.send("Vous n'avez pas suffisamment d'argent.")
    return

  if amount < 0:
    await ctx.send(f"Vous ne pouvez pas voler des Points-Marrons de cette manière à {member.mention} enfin! À quoi pensiez-vous, brigand des mers du Nord ?!")
    return

  await update_info(ctx.author, (-1) * amount,"wallet")
  await update_info(member, amount,"wallet")

  await ctx.send(f'{ctx.author} a donné {str(amount)} Points-Marrons à la banque de {member.mention}!')
  return



##############################################################################################################################

##############################################################################################################################
# Manuma

"""
Jeu de cartes-personnages : Manuma
"""

# Ici, on définit les prix des différents niveaux de prestige des cartes.
rar = [0, 1000, 2000, 5000, 25000, 75000, 250000, 1500000]
# 1 - 100 | 2 - 150 | 3 - 225 | 4 - 338 | 5 - 507 | 6 - 760 | 7 - 1140


# Ici, list des dictionnaires des différents boosters :
lboosters = [{'nom': 'Cécile', 'prix': 10000, 'gar':[3],'nbcards':10,'img':'https://media.discordapp.net/attachments/851847250224480326/944705500010917899/unknown.png?width=370&height=559', "couleur" : discord.Color.dark_grey(),"type" : "ULTRA BOOSTER",'ind': 1},
             {'nom': 'Sabrina', 'prix': 50000, 'gar': [4, 3], 'nbcards': 10,   'img':'https://media.discordapp.net/attachments/851847250224480326/944707122548060252/unknown.png?width=368&height=559',"couleur" : discord.Color.green(),"type" : "ULTRA BOOSTER",'ind': 2},
             {'nom': 'Christophe', 'prix': 200000, 'gar': [5, 5], 'nbcards': 10,
              'img': 'https://media.discordapp.net/attachments/821130009783042108/944708611656011806/unknown.png?width=369&height=558',"couleur" : discord.Color.dark_gold(),
              "type" : "ULTRA BOOSTER",'ind': 3},
             {'nom': 'Francis', 'prix': 750000, 'gar': [6, 5], 'nbcards': 15,
              'img': 'https://media.discordapp.net/attachments/821130009783042108/944710029200740422/unknown.png?width=366&height=559',"couleur" : discord.Color.gold(),"type" : "ULTRA BOOSTER",
              'ind': 4},
             {'nom': 'Règles', 'prix': 0, 'gar': [4], 'nbcards': 5,
              'img': 'https://media.discordapp.net/attachments/894207389476192256/951880462240997406/unknown.png?width=372&height=559',"couleur" : discord.Color.red(),"type" : "ULTRA BOOSTER",
              'ind': 5},
             {'nom': 'Spécial', 'prix': 75000, 'gar': [4, 3, 3], 'nbcards': 9,
              'img': 'https://media.discordapp.net/attachments/916042287832784979/951881834386579497/unknown.png?width=371&height=559',"couleur" : discord.Color.red(),"type" : "ULTRA BOOSTER",
              'ind': 6}]

lpaninis = [{'nom': 'SVT Crunch', 'prix': 5000, 'gar': [1], 'nbcards': 3,
              'img': 'https://media.discordapp.net/attachments/381753969103601666/949700844457168976/unknown.png',"couleur" : discord.Color.dark_grey(),"type" : "ULTRA PANINI",
              'ind': 1},
             {'nom': 'Chèvre Crunch', 'prix': 25000, 'gar': [3, 3, 3], 'nbcards': 5,
              'img': 'https://media.discordapp.net/attachments/381753969103601666/949701470905839666/unknown.png',"couleur" : discord.Color.dark_green(),"type" : "ULTRA PANINI",'ind': 2},
             {'nom': 'Joma Crunch', 'prix': 100000, 'gar': [5, 4], 'nbcards': 8,
              'img': 'https://media.discordapp.net/attachments/381753969103601666/949702035492716564/unknown.png',"couleur" : discord.Color.light_grey(),"type" : "ULTRA PANINI",'ind': 3},
             {'nom': 'Chimie Crunch', 'prix': 2500000, 'gar': [7, 6], 'nbcards': 10,'img': 'https://media.discordapp.net/attachments/381753969103601666/949702547382370374/unknown.png',"couleur" : discord.Color.purple(),"type" : "ULTRA PANINI",
              'ind': 4},
             {'nom': 'MicroEuler Crunch', 'prix': 6000000, 'gar': [7, 7, 7], 'nbcards': 10,
              'img': 'https://media.discordapp.net/attachments/381753969103601666/949702880162644039/unknown.png',"couleur" : discord.Color.red(),"type" : "ULTRA PANINI",
              'ind': 5}]

litems = [{'nom' : "Banckeur", 'prix' : 50000, 'img' : "https://media.discordapp.net/attachments/830759403710971915/967488758301741157/unknown.png", "couleur": discord.Color.green(), 'ind' : 1},
         {'nom' : 'Drop Vodkapple', "prix" : 50000, 'img' : 'https://media.discordapp.net/attachments/830759403710971915/967490644354424842/unknown.png', 'couleur' : discord.Color.red(), 'ind' : 2},
         {'nom' : "Spécichange", 'prix' : 15000, 'img' : "https://media.discordapp.net/attachments/830759403710971915/967488733484040272/unknown.png", "couleur" : discord.Color.purple(), "ind" :3},
         {"nom" : "Volbombe", "prix" : 5000, 'img' : 'https://media.discordapp.net/attachments/830759403710971915/967488708091711528/unknown.png', "couleur" : discord.Color.blue(), 'ind' : 4}]



def dcouleur(rarete: int):
    if rarete in [0, 1]:
        couleur = discord.Color.light_grey()
    elif rarete == 2:
        couleur = discord.Color.dark_green()
    elif rarete == 3:
        couleur = discord.Color.blue()
    elif rarete == 4:
        couleur = discord.Color.red()
    elif rarete == 5:
        couleur = discord.Color.dark_gold()
    elif rarete == 6:
        couleur = discord.Color.gold()
    else:
        couleur = discord.Color.purple()
    return couleur





# Ici, tous les réglages de toutes les cartes.
# Cela se présente de la manière suivante:
# {prenom, nom, manga, lien d'image, prestige, prix correspondant, indice, points d'attaque, points de défense, points d'intelligence}
# Il est nécessaire de suivre ce système tout en veillant à vérifier ses informations et à les présenter correctement.
# Présenter correctement les informations permet de gagner un temps monstrueux dans le code de François.

cards = cartes.cards

# Repose-liens
# Repose-liens
# Repose-liens
# Repose-liens
# Repose-liens
# Repose-liens
# au dessus, un espace pour reposer des liens si besoin.
  
# Ici, on définit la liste des mangas concernés par les cartes 'cards'. Si on rajoute un personnage d'un nouvel univers, il faut le nommer dans la list 'mangas'.
mangas = ['shingekinokyojin','shingekinokyojin', 'berserk','myheroacademia','myheroacademia', 'dr.stone', "chainsawman", "jojo", 'tokyorevengers','tokyorevengers','bluelock','jujutsukaisen','demonslayer','demonslayer', 'deathnote', 'dragonball', 'bleach', 'naruto', 'fairytail','onepiece','onepiece', 'hunterxhunter', 'onepunchman', 'tokyoghoul(&re)', 'haikyuuu', 'codegeass','assassinationclassroom','inazumaeleven','vinlandsaga','blackclover', 'autres']


trad = [("shingekinokyojin","Shingeki no Kyojin"),('berserk','Berserk'),('myheroacademia',"My Hero Academia"),("dr.stone","Dr.STONE"),("chainsawman","Chainsaw Man"),("jojo", "Jojo's Bizarre Adventure"), ("tokyorevengers","Tokyo Revengers"), ('bluelock',"Blue Lock"),("jujutsukaisen","Jujutsu Kaisen"),("demonslayer","Demon Slayer"),('deathnote','Death Note'),("dragonball",'Dragon Ball'),("bleach",'Bleach'),('naruto','Naruto'),('fairytail','Fairy Tail'),('onepiece',"One Piece"),('hunterxhunter', "Hunter x Hunter"),('onepunchman',"One-Punch Man"), ('tokyoghoul(&re)','Tokyo Ghoul'),('haikyuuu','Haikyuuu'),('codegeass',"Code Geass"),("assassinationclassroom","Assassination Classroom"),('inazumaeleven',"Inazuma Eleven"),('vinlandsaga','Vinland Saga'),('blackclover',"Black Clover")]




def majuscule(mess: str) -> str:
  """
  Retire l'intégralité des majuscules de 'mess' et renvoie son équivalent en minuscules.
  """
  symbmini = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
  symbmaj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']
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


def sansspace(text):
    """
    Renvoie text sans les espaces
    """
    i = 0
    newtext = ''
    while i < len(text):
        if text[i] != ' ':
            newtext = newtext + text[i]
        i = i + 1
    return newtext
  

@bot.command(pass_context=True)
#@commands.cooldown(1, 60 * 30, commands.BucketType.user)
async def claim(ctx):
  """
  Utilisable une fois toutes les demi-heures. Permet de débloquer une carte-personnage.
  """
  if alt(ctx.author.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  if await open_account(ctx.author):
    await ctx.send("Compte informatique en cours d'initialisation, veuillez patienter...")
    await asyncio.sleep(3)
    await ctx.send("Compte informatique initialisé ! Bon jeu !")
    
  manga = mangas[random.randint(0, len(mangas) - 2)]
  nb = random.randint(1, 1000000)
  if nb <= 620000:
    raret = 1
  elif nb <= 820000:
    raret = 2
  elif nb <= 940000:
    raret = 3
  elif nb <= 985000:
    em2 = discord.Embed(title="OH !", color=discord.Color.red())
    em2.set_image(url="https://media.discordapp.net/attachments/660792805161041920/967437167397847040/unknown.png")
    await ctx.send(embed=em2)
    await asyncio.sleep(2)
    raret = 4
  elif nb <= 995000:
    em2 = discord.Embed(title="Woaaaah! C'est fou!", color=discord.Color.dark_gold())
    em2.set_image(url="https://media.discordapp.net/attachments/660792805161041920/967437775982956645/unknown.png?width=1080&height=393")
    await ctx.send(embed=em2)
    await asyncio.sleep(2)
    raret = 5
  elif nb <= 999977:
    em2 = discord.Embed(title="IMPOSSIBLE...", color=discord.Color.gold())
    em2.set_image(url="https://media.discordapp.net/attachments/660792805161041920/967439060832505856/unknown.png?width=1080&height=374")
    await ctx.send(embed=em2)
    await asyncio.sleep(3)
    raret = 6
  else:
    raret = 7
    em2 = discord.Embed(title="Serait-ce?", color=discord.Color.purple())
    em2.set_image(url="https://media.discordapp.net/attachments/660792805161041920/967440685651329113/unknown.png")
    await ctx.send(embed=em2)
    await asyncio.sleep(5)

  couleur = dcouleur(raret)
  raradapt = []
  if raret == 7:
    for item in cards:
      if item['rarete'] == 7:
        raradapt.append(item['num'])
  else:
    for item in cards:
      if item['rarete'] == raret and sansspace(majuscule(item['manga'])) == manga:
        raradapt.append(item['num'])

  obt = random.choice(raradapt)

  if cards[obt-1]['nom'] == '-':
      prenom = cards[obt-1]['prenom']
      nom = ''
  elif cards[obt-1]['manga'] == 'One Piece' and cards[obt-1]['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
    prenom = f"{cards[obt-1]['nom']} D. {cards[obt-1]['prenom']}"
    nom = ""
  else:
    prenom = cards[obt-1]['prenom']
    nom = cards[obt-1]['nom']

  em = discord.Embed(title=f"{prenom} {nom}", color=couleur, description=f"Indice : {cards[obt - 1]['num']}")
  em.add_field(name="Manga :", value=f"{cards[obt - 1]['manga']}",inline=True)
  em.add_field(name="Prestige :", value=f"{cards[obt - 1]['rarete']*'⭐'}",inline=True)
  em.add_field(name="Prix :", value=f"{cards[obt - 1]['prix']}PM",inline=True)
  em.set_image(url=f"{cards[obt - 1]['url']}")
  await ctx.send(embed=em)
  await asyncio.sleep(2)
  users = await get_info_data()

  if users[str(ctx.author.id)]['veutvol'][0] == True:
    user2 = await bot.fetch_user(users[str(ctx.author.id)]['veutvol'][1])
    await asyncio.sleep(3)
    await ctx.send("ARRRG..!")
    await asyncio.sleep(1)
    await ctx.send(f"Vous étiez pris pour cible par {user2.mention} !")
    await ctx.send(f"Il récupère, par conséquent, la carte de {cards[obt-1]['prenom']}!")
    await update_info(ctx.author,0,'veutvol','blude',user2)
    await update_info(user2,0,'vol','blude',ctx.author)
    if not obt in users[str(user2.id)]['indices']:
      await update_info(user2,int(obt),'indices')
      await asyncio.sleep(2)
      msg = await ctx.send(f"{user2}, vous possédez à présent la carte de {cards[obt - 1]['prenom']} ! Félicitations !")
      await msg.add_reaction('💰')
      while True:
        try:
          reaction,user=await bot.wait_for('reaction_add',check=lambda reaction,user:user == user2 and reaction.emoji == '💰',timeout=60.0)
        except asyncio.TimeoutError:
          await msg.clear_reactions()
  
        if reaction.emoji == '💰':
          await ctx.send("Vente en cours....")
          await asyncio.sleep(1)
          await update_info(user2,-(cards[obt - 1]['num']),'indices')
          await ctx.send(f"Carte de {cards[obt - 1]['prenom']} vendue !")
          await ctx.send(f"+{cards[obt - 1]['prix'] // 2}PM")
          return
    else:
      await ctx.send(f"Vous possédez déjà la carte de {cards[obt - 1]['prenom']}.")
      await ctx.send(f"Vous gagnez {cards[obt - 1]['prix'] // 2} Points-Marrons !")
      await update_info(user2, cards[obt - 1]['prix'] // 2, 'wallet')
      return
      
  if not obt in users[str(ctx.author.id)]['indices']:
    await update_info(ctx.author,int(obt),'indices')
    msg = await ctx.send(f"{ctx.author}, vous possédez à présent la carte de {cards[obt - 1]['prenom']} ! Félicitations !")
    await msg.add_reaction('💰')
    while True:
      try:
        reaction,user=await bot.wait_for('reaction_add',check=lambda reaction,user:user == ctx.author and reaction.emoji == '💰',timeout=60.0)
      except asyncio.TimeoutError:
        await msg.clear_reactions()

      if reaction.emoji == '💰':
        await ctx.send("Vente en cours....")
        await asyncio.sleep(1)
        await update_info(ctx.author,-(cards[obt - 1]['num']),'indices')
        await ctx.send(f"Carte de {cards[obt - 1]['prenom']} vendue !")
        await ctx.send(f"+{cards[obt - 1]['prix'] // 2}PM")
        return
  
  else:
    await ctx.send(f"Vous possédez déjà la carte de {cards[obt - 1]['prenom']}.")
    await ctx.send(f"Vous gagnez {cards[obt - 1]['prix'] // 2} Points-Marrons !")
    await update_info(ctx.author, cards[obt - 1]['prix'] // 2, 'wallet')
    return


@bot.command(aliases=['gs'])
async def galeryshow(ctx, user: discord.Member = None):
  """
  Affiche la galerie de 'user'. Si 'user' == None, alors 'user' == ctx.author.
  """
  if user == None:
    user = ctx.author
  
  users = await get_info_data()
  
  if alt(user.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés.")
    return

  if str(user.id) not in users and user != ctx.author:
    await ctx.send(f"{user.mention} ne possède pas encore de compte informatique.")
    return
    
  elif str(user.id) not in users and user == ctx.author:
    await open_account(user)
    await ctx.send("Compte informatique en cours d'initialisation, veuillez patienter...")
    await asyncio.sleep(1)
    await ctx.send("Compte informatique initialisé ! Bon jeu !")
    await asyncio.sleep(1)
    await ctx.send("Par conséquent, vous n'avez pour l'instant aucune carte.")
    return

  elif users[str(user.id)]['indices'][0] == 0:
    await ctx.send("Aucune carte détectée. François est navré.")
    return

  fcard = False
  # fcard est un booléen qui détecte (ou pas) la présence d'une carte prioritaire.
  if users[str(user.id)]['firstcard'] > 0:
    firstcard = users[str(user.id)]['firstcard']
    # firstcard contient l'indice de la carte prioritaire définie par l'utilisateur.
    if firstcard not in users[str(user.id)]['indices']:
      # Vérifie que la carte prioritaire est bien dans la galerie de l'utilisateur, pour éviter tout bug.
      await ctx.send("Erreur interne liée à votre 'firstcard'. Veuillez contacter Antoine pour plus d'informations.")
      return
    fcard = True

  ordre = users[str(user.id)]['ordre']
  gal = []
  if fcard:
    gal.append(firstcard)
  for x in users[str(user.id)]['indices']:
    if x == 0:
      break
    if not fcard or x != firstcard:
      gal.append(x)
  gal = ranger(gal,ordre)
  bot.gspages = []
  for item in gal:
    if cards[item-1]['rarete'] == 0:
      couleur = discord.Color.light_grey()
      nom = "ENFANT | ÉDITION LIMITÉE"
      rar = "Inestimable"
  
      em = discord.Embed(title=f"{cards[item-1]['prenom']} {nom}", color=couleur)
      em.add_field(name="Manga :", value=f"{cards[item-1]['manga']}")
      em.add_field(name='Prestige', value=f'{rar}')
      em.add_field(name="Indice :", value=f"{cards[item-1]['num']}")
      em.set_image(url=f'{cards[item-1]["url"]}')
      bot.gspages.append(em)
    else:
      couleur = dcouleur(cards[item-1]['rarete'])
      if cards[item-1]['nom'] == '-':
        prenom = cards[item-1]['prenom']
        nom = ''
      elif cards[item-1]['manga'] == 'One Piece' and cards[item-1]['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
        prenom = f"{cards[item-1]['nom']} D. {cards[item-1]['prenom']}"
        nom = ""
      else:
        prenom = cards[item-1]['prenom']
        nom = cards[item-1]['nom']

      rar = cards[item-1]["rarete"] * "⭐"

      em = discord.Embed(title=f"{prenom} {nom}", color=couleur)
      em.add_field(name="Manga :", value=f"{cards[item-1]['manga']}")
      em.add_field(name='Prestige', value=f'{rar}')
      em.add_field(name="Prix :", value=f"{cards[item-1]['prix']}")
      em.add_field(name="Indice :", value=f"{cards[item-1]['num']}")
      em.set_image(url=f'{cards[item-1]["url"]}')
      bot.gspages.append(em)

  buttons = ['◀', '▶']
  current = 0

  msg = await ctx.send(embed=bot.gspages[current])

  for button in buttons:
    await msg.add_reaction(button)

  while True:
    try:
      reaction, user = await bot.wait_for('reaction_add', check=lambda reaction,user: user == ctx.author and reaction.emoji in buttons,timeout=60.0)
    except asyncio.TimeoutError:
      embed = bot.gspages[current]
      embed.set_footer(text="temps écoulé.")
      await msg.clear_reactions()

    else:
      previous_page = current

      if reaction.emoji == '◀':
        if current == 0:
          current = len(bot.gspages) - 1
        else:
          current = current - 1

      else:
        if current == len(bot.gspages) - 1:
          current = 0
        else:
          current = current + 1

      for button in buttons:
        await msg.remove_reaction(button, ctx.author)

      if current != previous_page:
        await msg.edit(embed=bot.gspages[current])
  return

@bot.command(aliases=['gl'])
async def galerylist(ctx, user: discord.Member=None):
  """
  Renvoie la liste des cartes-personnages possédées par l'utilisateur désiré.
  """
  if user == None:
    user = ctx.author
  if alt(user.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return
  
  users = await get_info_data()
  if str(user.id) not in users and user != ctx.author:
    await ctx.send(f"{user.mention} ne possède pas encore de compte informatique.")
    return
  elif str(user.id) not in users and user == ctx.author:
    await open_account(user)
    await ctx.send("Compte informatique en cours d'initialisation, veuillez patienter...")
    await asyncio.sleep(1)
    await ctx.send("Compte informatique initialisé ! Bon jeu !")
    await asyncio.sleep(1)
    await ctx.send("Par conséquent, vous n'avez pour l'instant aucune carte.")
    return
  elif users[str(user.id)]['indices'][0] == 0:
    await ctx.send("Aucune carte détectée. François est navré.")
    return
  
  fcard = False
  firstcard = users[str(user.id)]['firstcard']
  if firstcard != 0:
    if firstcard not in users[str(user.id)]['indices']:
      # Vérifie que la carte prioritaire est bien dans la galerie de l'utilisateur, pour éviter tout bug.
      await ctx.send("Erreur interne liée à votre 'firstcard'. Veuillez contacter Antoine pour plus d'informations.")
      return
    fcard = True
  ordre = users[str(user.id)]['ordre']
  gal = []
  if firstcard != 0:
    gal.append(firstcard)
  for x in users[str(user.id)]['indices']:
    if x == 0:
      break
    if not fcard or x != firstcard:
      gal.append(x)
  gal = ranger(gal,ordre)
  mess = ''
  await ctx.author.send(f"**Liste des cartes-personnages de {user}**")
  for x in gal:
    if cards[x-1]['nom'] == '-':
      prenom = cards[x-1]['prenom']
      nom = ''
    elif cards[x-1]['manga'] == 'One Piece' and cards[x-1]['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
      prenom = f"{cards[x-1]['nom']} D. {cards[x-1]['prenom']}"
      nom = ""
    else:
      prenom = cards[x-1]['prenom']
      nom = cards[x-1]['nom']
      
    mess = mess + f"- **{prenom} {nom}** | {cards[x-1]['manga']} | {cards[x-1]['rarete']}⭐ | `{cards[x-1]['num']}`\n"
    if len(mess) > 800:
      await user.send(mess)
      mess = ''
  await user.send(mess)
  return
  
# 0 - étoiles décroissant
# 1 - étoiles croissant
# 2 - indices croissant
# 3 - indices décroissant
# 4 - prénoms ordre alphabétique
# 5 - prénoms ordre alphabétique inversé
# 6 - prénoms ordre alphabétique
# 7 - prénoms ordre alphabétique inversé
#PSST
# psst
  
longcartes = len(cards)
cartesp0 = sum([1 for x in cards if x['rarete'] == 0])
cartesp1 = sum([1 for x in cards if x['rarete'] == 1])
cartesp2 = sum([1 for x in cards if x['rarete'] == 2])
cartesp3 = sum([1 for x in cards if x['rarete'] == 3])
cartesp4 = sum([1 for x in cards if x['rarete'] == 4])
cartesp5 = sum([1 for x in cards if x['rarete'] == 5])
cartesp6 = sum([1 for x in cards if x['rarete'] == 6])
cartesp7 = sum([1 for x in cards if x['rarete'] == 7])
totalpres = [cartesp0,cartesp1,cartesp2,cartesp3,cartesp4,cartesp5,cartesp6,cartesp7]


@bot.command(aliases=['cog'])
async def changeordregalery(ctx, ind: int=None):
  """
  Permet à un utilisateur de changer l'ordre de rangement de sa galerie.
  """
  user = ctx.author
  users = await get_info_data()
  if ind == None:
    em = discord.Embed(title="AIDE DE RANGEMENT DE CARTES", description="Liste des différents types d'ordre de rangement des cartes de votre galerie.", color= discord.Color.red())
    em.add_field(name="!cog 0", value="Range les cartes par niveau de prestige décroissant (par défaut)", inline=False)
    em.add_field(name="!cog 1", value="Range les cartes par niveau de prestige croissant",inline=False)
    em.add_field(name="!cog 2", value="Range les cartes par indice croissant",inline=False)
    em.add_field(name="!cog 3", value="Range les cartes par indice décroissant",inline=False)
    em.add_field(name="!cog 4", value="Range les cartes par ordre alphabétique (prénoms)",inline=False)
    em.add_field(name="!cog 5", value="Range les cartes par ordre inverse alphabétique (prénoms)",inline=False)
    em.add_field(name="!cog 6", value="Range les cartes par ordre inverse alphabétique (noms)",inline=False)
    em.add_field(name="!cog 7", value="Range les cartes par ordre inverse alphabétique (noms)",inline=False)
    await ctx.send(embed=em)
    return
    
  elif ind > 7:
    await ctx.send("Vous n'avez pas rentré un indice d'ordre valide. Veuillez réessayer.")
    return
    
  else:
    await update_info(user,ind,'ordre')
    await ctx.send("Ordre actualisé !")
    return

@bot.command(aliases=['cfc'])
async def changefirstcard(ctx, ind:int=None):
  """
  permet à un utilisateur de changer sa carte-personnage prioritaire. Elle apparaitra toujours en premier.
  """
  user = ctx.author
  users = await get_info_data()
  if ind == None:
    await ctx.send("Vous devez citer une nouvelle carte à définir en tant que firstcard.")
    return
  else:
    if ind not in users[str(user.id)]['indices']:
      await ctx.send("Vous devez citer une carte que vous possédez !")
      return
    else:
      await update_info(user,ind,'firstcard')
      await ctx.send("firstcard actualisée !")
      return
  
  
def ranger(gal:list,ordre:int) -> None:
  if ordre == 0:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['rarete'] < cards[gal[j]-1]['rarete']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  elif ordre == 1:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['rarete'] > cards[gal[j]-1]['rarete']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  elif ordre == 2:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['num'] > cards[gal[j]-1]['num']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  elif ordre == 3:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['num'] < cards[gal[j]-1]['num']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  elif ordre == 4:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['prenom'] < cards[gal[j]-1]['prenom']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  elif ordre == 5:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['prenom'] > cards[gal[j]-1]['prenom']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  elif ordre == 6:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['nom'] < cards[gal[j]-1]['nom']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  elif ordre == 7:
    n = len(gal)
    if n > 1:
      for k in range(1, n):
        j = k
        while j > 1 and cards[gal[j-1]-1]['nom'] > cards[gal[j]-1]['nom']:
          gal[j-1], gal[j] = gal[j], gal[j-1]
          j = j - 1
  return gal



@bot.command()
async def mail(ctx, user: discord.Member,*,msg: str):
  """
  Permet d'envoyer un MP à user.
  """
  await user.send(f"**MAIL DE LA PART DE {ctx.author} :**")
  await asyncio.sleep(3)
  await user.send(f"       `{msg}`")
  await ctx.send("Mail envoyé avec succès !")
  return


  
@bot.command(aliases=['p'])
async def profil(ctx, user: discord.Member = None):
  """
  affiche le profil de 'user'
  """
  if user == None:
    user = ctx.author
  if alt(user.id):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return
  users = await get_info_data()
  em = discord.Embed(title="Profil", color=discord.Color.dark_green(), description=f"Utilisateur : {user._user}\nIdentifiant : {user.id}\nCompte créé le {user.created_at.strftime('%d/%m/%Y %H:%M:%S')}\nA rejoint la nation le {user.joined_at.strftime('%d/%m/%Y %H:%M:%S')}",timestamp=datetime.utcnow())
  if users[str(user.id)]['firstcard'] != 0:
    firstcard = users[str(user.id)]['firstcard']
    if firstcard in users[str(user.id)]['indices']:
      em.set_thumbnail(url=cards[firstcard-1]['url'])
  if users[str(user.id)]['wallet']+users[str(user.id)]['bank'] == 0:
    em.add_field(name="Points-Marrons :", value ="Aucun !", inline = False)
  else:
    em.add_field(name = "Points-Marrons :", value=f"{users[str(user.id)]['wallet']+users[str(user.id)]['bank']}PM", inline=False)
  if users[str(user.id)]['rotul'] == 0:
    em.add_field(name="Points-Rotules :", value=f"Aucun !", inline=False)
  else:
    em.add_field(name="Points-Rotules :", value=f"{users[str(user.id)]['rotul']}", inline=False)
  perso = [0]*8
  total = [0]*8
  for indice in users[str(user.id)]['indices']:
    perso[cards[indice-1]['rarete']] += 1
  tperso = sum(perso)
  if tperso == 0:
    em.add_field(name = "Cartes-Personnages :", value="Vous n'en avez aucune ! Qu'attendez-vous ?",inline = False)
  else:
    i = 0
    mess = ""
    for x in perso:
      if x != 0:
        mess = mess + f'{x}/{totalpres[i]} - {i}⭐\n'
      i = i + 1
    em.add_field(name = "Cartes-Personnages :", value=mess+f"{tperso}/{longcartes} au total.",inline = False)
  boosters = users[str(user.id)]['boosters']
  paninis = users[str(user.id)]['paninis']
  items = users[str(user.id)]['items']
  if boosters[0] == 0:
    em.add_field(name = "Boosters :", value="Aucun !", inline=False)
  else:
    lboosts = [0]*len(lboosters)
    for booster in boosters:
      if booster != 0:
        lboosts[booster-1] = lboosts[booster-1] + 1
    msg = ''
    for i in range(0,len(lboosts)):
      if lboosts[i] > 0:
        nom = "ULTRA BOOSTER - " + lboosters[i]['nom']
        nb = lboosts[i]
        if nb > 1:
          plur = 's'
        else:
          plur = ''
        msg = msg + f"{nom} : {nb} booster{plur}\n"
    em.add_field(name = "Boosters :", value=msg, inline=False)
    
  if paninis[0] == 0:
    em.add_field(name = "Paninis :", value="Aucun !", inline=False)
  else:
    lpans = [0]*len(lpaninis)
    for panini in paninis:
      if panini != 0:
        lpans[panini-1] = lpans[panini-1] + 1
    msg = ''
    for i in range(0,len(lpans)):
      if lpans[i] > 0:
        nom = "ULTRA PANINI - " + lpaninis[i]['nom']
        nb = lpans[i]
        if nb > 1:
          plur = 's'
        else:
          plur = ''
        msg = msg + f"{nom} : {nb} panini{plur}\n"
    em.add_field(name = "Paninis :", value=msg, inline=False)

  if items[0] == 0:
    em.add_field(name="Items :", value="Aucun !", inline=False)
  else:
    litem = [0] * len(litems)
    for item in items:
      if item != 0:
        litem[item-1] = litem[item-1] + 1
    msg = ''
    for i in range(0,len(litem)):
      if litem[i] > 0:
        nom = 'ULTRA ITEM - ' + litems[i]['nom']
        nb = litem[i]
        if nb > 1:
          plur = "s"
        else:
          plur = ""
        msg = msg + f"{nom} : {nb} item{plur}\n"
    em.add_field(name="Items :", value=msg, inline=False)
  
  await ctx.send(embed=em)
  return
    
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


def veriflettres(text : str):
  for let in text:
    if let not in 'azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN':
      return False
  return True

def verifneg(text: str):
  for let in text:
    if let not in '123456789-':
      return False
  return True



@bot.command()
async def search(ctx, *, recherche):
  """
  Permet de chercher une carte-personnage par un indice, par un nombre d'étoiles, par un nom de manga.
  """
  if alt(ctx.author):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return
  
  users = await get_info_data()
  
  if verifnombre(recherche):
    if int(recherche) > len(cards):
      await ctx.send("Aucune carte-personnage ne correspond à cet indice.")
      return
    em2 = discord.Embed(title="Possesseurs :", description="Liste des personnes possédant cette carte.",color=discord.Color.blue())
    ind = 0
    item = cards[int(recherche)-1]
        
    for user in users:
      if item['num'] in users[str(user)]['indices']:
        username = await bot.fetch_user(user)
        em2.add_field(name=f"{username}", value="possède cette carte", inline=False)
        ind = ind + 1

    couleur = dcouleur(item['rarete'])

    if item['nom'] == '-':
      prenom = item['prenom']
      nom = ''
    elif item['manga'] == 'One Piece' and item['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
      prenom = f"{item['nom']} D. {item['prenom']}"
      nom = ""
    else:
      prenom = item['prenom']
      nom = item['nom']

    if item['rarete'] == 0:
      em = discord.Embed(title=f'{item["prenom"]} {nom} | édition limitée', color=couleur)
      em.add_field(name='Manga :', value=f'{item["manga"]}')
      em.add_field(name="Prestige :", value="Inestimable")
      em.set_image(url=f"{item['url']}")

      await ctx.send(embed=em)
      if ind == 0:
        await ctx.send("Personne ne possède cette carte actuellement.")
        return
      await ctx.send(embed=em2)
      return

    em = discord.Embed(title=f'{item["prenom"]} {nom}', color=couleur)
    em.add_field(name='Manga :', value=f'{item["manga"]}')
    em.add_field(name="Prestige :", value=f"{item['rarete'] * '⭐'}")
    em.add_field(name="Prix :", value=f"{item['prix']} PM")
    em.add_field(name="Indice :", value=f"{item['num']}")
    em.set_image(url=f"{item['url']}")

    await ctx.send(embed=em)
    if ind == 0:
      await ctx.send("Personne ne possède cette carte actuellement.")
      return
    await ctx.send(embed=em2)
    return

  elif compteetoile(recherche) > 0:
    nb = compteetoile(recherche)
    i = 0
    message = ''
    while i < len(cards):
      if cards[i]['rarete'] == nb:

        if cards[i]['nom'] == '-':
          nom = ''
        else:
          nom = cards[i]['nom']

        message = message + f'{cards[i]["prenom"]} {nom} | {cards[i]["manga"]} | {cards[i]["rarete"] * "⭐"} | {cards[i]["prix"]} PM | {cards[i]["num"]}\n ---------------------------------------------- \n'
        if len(message) > 1000:
          await ctx.send(message)
          message = ''
          i = i + 1
      await ctx.send(message)
      return

  if sansspace(majuscule(recherche)) in mangas:
    pres = [0] * 7
    i = 0
    message = ''
    while i < len(cards):
      if majuscule(cards[i]['manga']) == majuscule(recherche):

        if cards[i]['nom'] == '-':
          prenom = cards[i]['prenom']
          nom = ''
        elif cards[i]['manga'] == 'One Piece' and cards[i]['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
          prenom = f"{cards[i]['nom']} D. {cards[i]['prenom']}"
          nom = ""
        else:
          prenom = cards[i]['prenom']
          nom = cards[i]['nom']

        if cards[i]['rarete'] == 0:
          rarete = 'Inestimable'
          prix = 'Aucun prix'
        else:
          rarete = cards[i]['rarete'] * '⭐'
          prix = f"{cards[i]['prix']} PM"
          if cards[i]['rarete'] != 7:
            pres[len(rarete)] = pres[len(rarete)] + 1

        message = message + f'{cards[i]["prenom"]} {nom} | {cards[i]["manga"]} | {rarete} | {prix} | {cards[i]["num"]}\n ---------------------------------------------- \n'
        if len(message) > 900:
          await ctx.send(message)
          message = ''
      i = i + 1
    await ctx.send("zizi mou wolaye")
    if len(message) > 0:
      await ctx.send(message)
    em = discord.Embed(title=f"Répartition nombre de personnages/prestige")
    em.add_field(name="1⭐ :", value=f"{pres[1]}")
    em.add_field(name="2⭐ :", value=f"{pres[2]}")
    em.add_field(name="3⭐ :", value=f"{pres[3]}")
    em.add_field(name="4⭐ :", value=f"{pres[4]}")
    em.add_field(name="5⭐ :", value=f"{pres[5]}")
    em.add_field(name="6⭐ :", value=f"{pres[6]}")
    em.add_field(name="Total :", value=f"{pres[1] + pres[2] + pres[3] + pres[4] + pres[5] + pres[6]}")
    await ctx.send(embed=em)
    return

  else:
    em2 = discord.Embed(title="Possesseurs :", description="Liste des possesseurs de cette carte :",color=discord.Color.blue())
    ind = 0
    for item in cards:
      if majuscule(f'{item["prenom"]} {item["nom"]}') == majuscule(recherche) or majuscule(f'{item["nom"]} {item["prenom"]}') == majuscule(recherche) or majuscule(           item['prenom']) == majuscule(recherche) or majuscule(item['nom']) == majuscule(recherche):
        users = await get_info_data()
        for user in users:
          if item['num'] in users[str(user)]['indices']:
            username = await bot.fetch_user(user)
            em2.add_field(name=f"{username}", value="possède cette carte", inline=False)
            ind = ind + 1

        couleur = dcouleur(item['rarete'])

        if item['nom'] == '-':
          prenom = item['prenom']
          nom = ''
        elif item['manga'] == 'One Piece' and item['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
          prenom = f"{item['nom']} D. {item['prenom']}"
          nom = ""
        else:
          prenom = item['prenom']
          nom = item['nom']

        em = discord.Embed(title=f'{prenom} {nom}', color=couleur)
        em.add_field(name='Manga :', value=f'{item["manga"]}')
        em.add_field(name='Prestige :', value=f"{item['rarete'] * '⭐'}")
        em.add_field(name='Prix :', value=f"{item['prix']} PM")
        em.add_field(name="Indice :", value=f"{item['num']}")
        em.set_image(url=f'{item["url"]}')
  
        await ctx.send(embed=em)
        if ind == 0:
          await ctx.send("Personne ne possède cette carte actuellement.")
        else:
          await ctx.send(embed=em2)
          return




@bot.command(aliases=['ms'])
async def sell(ctx, *, text: str):
  if alt(ctx.author):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  if await open_account(ctx.author):
    await ctx.send("Compte informatique en cours d'initialisation, veuillez patienter...")
    await asyncio.sleep(1)
    await ctx.send("Compte informatique initialisé ! Bon jeu !")
    await asyncio.sleep(1)
    await ctx.send("Par conséquent, vous n'avez pour l'instant aucune carte.")
    return

  if majuscule(text) == 'all':
    def check2(m):
      return m.author == ctx.author and m.channel == ctx.channel
    users = await get_info_data()
    liste = [indice for indice in users[str(ctx.author.id)]['indices'] if indice != 0]
    somme = 0
    for indice in liste:
      somme = somme + cards[indice-1]['prix']//2
    await ctx.send(f"Si vous effectuez cette action, vous perdrez ⚠**toutes vos cartes-personnages**⚠ et vous gagnerez `{somme}PM`.")
    await ctx.send(f"Êtes-vous sûr de ce que vous faites ? (o/y/oui/yes)")

    try:
      m = await bot.wait_for('message', timeout=30.0, check = check2)
    except asyncio.TimeoutError:
      await ctx.send(f"temps écoulé. Vente annulée.")
      return
      
    if majuscule(m.content) not in ['o', 'y', 'oui', 'yes']:
      await ctx.send("À la revoyure !")
      return
    else:
      await ctx.send(f"VRAIMENT sûr ? (o/y/oui/yes)")

      try:
        m = await bot.wait_for('message', timeout=30.0, check = check2)
      except asyncio.TimeoutError:
        await ctx.send(f"temps écoulé. Vente annulée.")
        return
      
      if majuscule(m.content) not in ['o', 'y', 'oui', 'yes']:
        await ctx.send("À la revoyure !")
        return
      else:
        await ctx.send(f"DITES WOLA ? (o/y/oui/yes)")
  
        try:
          m = await bot.wait_for('message', timeout=30.0, check = check2)
        except asyncio.TimeoutError:
          await ctx.send(f"temps écoulé. Vente annulée.")
          return

        if majuscule(m.content) not in ['o', 'y', 'oui', 'yes']:
          await ctx.send("À la revoyure !")
          return
        else:
          await ctx.send(f"Écrivez 'CONFIRMER' pour confirmer.")
    
          try:
            m = await bot.wait_for('message', timeout=30.0, check = check2)
          except asyncio.TimeoutError:
            await ctx.send(f"temps écoulé. Vente annulée.")
            return
          if m.content != "CONFIRMER":
            await ctx.send("À la revoyure !")
            return
          else:
            await ctx.send("Vous l'aurez voulu...")
            await asyncio.sleep(3)
            await update_info(ctx.author, somme)
            await ctx.send(f"+`{somme}PM`...")
            if users[str(ctx.author.id)]["firstcard"] != 0:            
              firstcard = users[str(ctx.author.id)]['firstcard']
              await update_info(ctx.author,firstcard,'firstcard')
              await ctx.send("FIRSTCARD RÉINITIALISÉE")
            for x in users[str(ctx.author.id)]['indices']:
              await update_info(ctx.author, -x, 'indices')
            await ctx.send("Toute votre galerie a été vidée, les plus sincères remerciements de François, et bonne continuation !")
            return
        
    return
  
  i = 0
  chiffres = []
  msg = ''
  while i < len(text):
    if text[i] == '!':
      chiffres.append(msg)
      msg = ''
    else:
      msg = msg + text[i]
    i = i + 1
  chiffres.append(msg)

  numb = []
  for i in chiffres:
    if not verifnombre(i):
      await ctx.send("Vous devez donner un ou plusieurs indices.")
      return
    else:
      numb.append(int(i))

  users = await get_info_data()
  c = []
  if len(numb) > 1:
    em = discord.Embed(title=f"VENTE MULTIPLE DE {ctx.author}",description="Avertissement ⚠ :\n la vente multiple vend instantanément toutes les cartes ci-dessous.\n Aucun remboursement ne sera accordé : soyez-sûr des cartes que vous vendez.",color=discord.Color.red())
  else:
    em = discord.Embed(title=f"VENTE DE {ctx.author}",description="Avertissement ⚠ :\n Cette procédure vend instantanément la carte ci-dessous.\n Aucun remboursement ne sera accordé : soyez-sûr de la carte que vous vendez.",color=discord.Color.red())
  long = len(cards)
  for i in numb:
    if i > long:
      await ctx.send(f"Une erreur est survenue... {i} n'est pas un indice valide.")
      return
    if i not in users[str(ctx.author.id)]['indices']:
      await ctx.send(f"Vous ne possédez pas la carte de {cards[i-1]['prenom']} d'indice ``{cards[i-1]['num']}``.")
      return
    if cards[i-1]['rarete'] == 0:
      await ctx.send("Sacrebleu on ne vend pas un enfant de la sorte ! Vicieux personnage !")
      return
    c.append(cards[i-1])
  prix = 0
  for psge in c:
    
    if psge['nom'] == '-':
      prenom = psge['prenom']
      nom = ''
    elif psge['manga'] == 'One Piece' and psge['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
      prenom = f"{psge['nom']} D. {psge['prenom']}"
      nom = ""
    else:
      prenom = psge['prenom']
      nom = psge['nom']

    fcard = False
    if users[str(ctx.author.id)]['firstcard'] == psge['num']:
      fcard = True

    if fcard:
      em.add_field(name=f"{prenom} {nom}", value=f"indice : {psge['num']} - ⚠ FIRSTCARD ⚠", inline=False)
    else:
      em.add_field(name=f"{prenom} {nom}", value=f"indice : {psge['num']}", inline=False)
    prix = prix + psge['prix'] // 2

  await ctx.send(embed=em)

  def check2(m):
    return m.author == ctx.author and m.channel == ctx.channel

  if len(c) > 1:
    await ctx.send(f"Êtes-vous sûr de vouloir revendre **toutes** ces cartes pour `{prix}` Points-Marrons ? (o / oui / yes / y)")
  else:
    await ctx.send(f"Êtes-vous sûr de vouloir revendre cette carte pour `{prix}` Points-Marrons ? (o / oui / yes / y)")
  
  try:
    msg = await bot.wait_for('message', timeout=30.0, check=check2)
  except asyncio.TimeoutError:
    await ctx.send("Délai expiré. Vente annulée.")
    return

  if majuscule(msg.content) in ['o', 'y', 'oui', 'yes']:
    await ctx.send("Vente en cours...")
    await update_info(ctx.author, prix)
    for psge in c:
      if users[str(ctx.author.id)]['firstcard'] == psge['num']:
        await update_info(ctx.author, 0, 'firstcard')
        await ctx.send("`FIRSTCARD RÉINITIALISÉE`")
      await update_info(ctx.author, -psge['num'], "indices")
    await ctx.send(f"+`{prix}`PM")
    await ctx.send("Processus terminé, merci à vous et bonne journée !")
    return
  else:
    await ctx.send("à plus tard !")
    return


@bot.command()
async def lstore(ctx):
  """
  Affiche la boutique sous forme de liste.
  """
  nbpage = 0
  store = discord.Embed(title=f"ULTRA BOUTIQUE", description =f"Page d'accueil | Numéro de page : {nbpage}", color= discord.Color.blue())
  nbpage = nbpage + 1
  text = ''
  for booster in lboosters:
    if booster['prix'] == 0:
      prix = "Indisponible"
    else:
      prix = f"{booster['prix']}PM"
    
    text = text + f"`{booster['nom']}` | {prix} | Numéro de page : {nbpage} | **Indice de booster : {booster['ind']}**\n"    
    nbpage = nbpage + 1
  store.add_field(name="ULTRA BOOSTERS :", value=text,inline=False)
  text = ''
  for panini in lpaninis:
    prix = f"{panini['prix']}PM"
    text = text + f"`{panini['nom']}` | {prix} | Numéro de page : {nbpage} | **Indice de panini : {panini['ind']}**\n"
    nbpage = nbpage + 1
  store.add_field(name="ULTRA PANINIS", value=text, inline=False)
  text = ''
  for item in litems:
    if item['nom'] in ('Banckeur',"Drop Vodkapple"):
      users = await get_info_data()
      prix = f"{(users[str(ctx.author.id)]['bank']+users[str(ctx.author.id)]['wallet'])//4}PM"
    else:
      prix = f"{item['prix']}PM"

    text = text + f"`{item['nom']}` | {prix} | Numéro de page : {nbpage} | **Indice d'item : {item['ind']}**\n"
    nbpage = nbpage + 1
  store.add_field(name="ULTRA ITEMS :", value=text, inline=False)
  await ctx.send(embed=store)
  return

@bot.command(pass_context=True)
@commands.cooldown(1, 1 * 15, commands.BucketType.user)
async def store(ctx, page:int=0):
  """
  Affiche la boutique. Contient des boosters et des paninis pour l'instant.
  """

  if alt(ctx.author):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  storepages = []
  nbpage = 0
  paccueil = discord.Embed(title=f"ULTRA BOUTIQUE - Tom Nook", description = f"Page d'accueil\nNuméro de page : {nbpage}", color = discord.Color.blue())
  paccueil.set_image(url='https://media.discordapp.net/attachments/916042287832784979/967097928822947860/unknown.png')
  storepages.append(paccueil)
  nbpage = nbpage + 1
  for booster in lboosters:

    couleur = booster['couleur']
    
    garanti = ''
    for garant in booster['gar']:
      garanti = garanti + f'1x{garant}⭐\n'

    name = "ULTRA BOOSTER"

    if booster['prix'] == 0:
      prix = "Indisponible"
    else:
      prix = f"{booster['prix']}PM"

    boutique = discord.Embed(title=f"{name} - {booster['nom']}", description=f"Numéro de page : {nbpage}",color=couleur)
    boutique.set_image(url=booster['img'])
    boutique.add_field(name="Quantité :", value=f"{booster['nbcards']} cartes")
    boutique.add_field(name="Garanti :", value=garanti)
    boutique.add_field(name='Prix :', value=f"{prix}")
    boutique.add_field(name="Indice de BOOSTER :", value=f"{booster['ind']}")
    storepages.append(boutique)
    nbpage = nbpage + 1
    
  for panini in lpaninis:

    couleur = panini['couleur']
    
    garanti = ''
    for garant in panini['gar']:
      garanti = garanti + f'1x{garant}⭐\n'

    name = "ULTRA PANINI"

    if panini['prix'] == 0:
      prix = "Indisponible"
    else:
      prix = f"{panini['prix']}PM"

    boutique = discord.Embed(title=f"{name} - {panini['nom']}", description=f"Numéro de page : {nbpage}", color=couleur)
    boutique.set_image(url=panini['img'])
    boutique.add_field(name="Quantité :", value=f"{panini['nbcards']} cartes")
    boutique.add_field(name="Garanti :", value=garanti)
    boutique.add_field(name='Prix :', value=f"{prix}")
    boutique.add_field(name="Indice de PANINI :", value=f"{panini['ind']}")
    storepages.append(boutique)
    nbpage = nbpage + 1

  for item in litems:

    couleur = item['couleur']
    name = 'ULTRA ITEM'
    if item['nom'] in ("Banckeur","Drop Vodkapple"):
      users = await get_info_data()
      prix = f"{(users[str(ctx.author.id)]['bank']+users[str(ctx.author.id)]['wallet'])//4}PM"
    else:
      prix = f"{item['prix']}PM"

    boutique = discord.Embed(title=f"{name} - {item['nom']}", description=f"Numéro de page : {nbpage}", color = couleur)
    boutique.set_image(url=item['img'])
    boutique.add_field(name="Prix :", value=f"{prix}")
    boutique.add_field(name="Indice d'ITEM :", value=f"{item['ind']}")
    storepages.append(boutique)
    nbpage = nbpage + 1

  if page > len(storepages)-1:
    await ctx.send("Indice invalide. Il est trop élevé.")
    return
  if page < 0:
    await ctx.send("Indice invalide. Il est trop faible.")
    return
  await ctx.send("**BOUTIQUE** ! BIENVENUE !")
  buttons = ['⬅', '💰', '➡']
  current = page
  msg = await ctx.send(embed=storepages[current])

  for button in buttons:
    await msg.add_reaction(button)

  while True:
    try:
      reaction, user = await bot.wait_for('reaction_add', check=lambda reaction,user: user == ctx.author and reaction.emoji in buttons,timeout=180.0)
    except asyncio.TimeoutError:
      embed = storepages[current]
      embed.set_footer(text="temps écoulé.")
      await msg.clear_reactions()

    else:
      previous_page = current
  
      if reaction.emoji == '⬅':
        if current == 0:
          current = len(storepages) - 1
        else:
          current = current - 1

      elif reaction.emoji == '➡':
        if current == len(storepages) - 1:
          current = 0
        else:
          current = current + 1

      elif reaction.emoji == '💰':
        if current == 0:
          await ctx.send("Vous ne pouvez pas acheter la page d'accueil !")
          return
        elif current > 11:
          name = "ULTRA ITEM"
          vnom = litems[current-12]['nom']
          if vnom in ("Banckeur","Drop Vodkapple"):
            prix = (users[str(ctx.author.id)]['bank']+users[str(ctx.author.id)]['wallet'])//4
          elif vnom == "Volbombe" and users[str(ctx.author.id)]['vol'][0] == True:
            await ctx.send("Vous ciblez déjà quelqu'un ! Une escroquerie à la fois, François vous en serait très reconnaissant !")
            return
          else:
            prix = litems[current-12]['prix']
        elif current > len(lboosters):
          name = "ULTRA PANINI"
          vnom = lpaninis[current-7]['nom']
          prix = lpaninis[current-7]['prix']
        else:
          name = "ULTRA BOOSTER"
          vnom = lboosters[current-1]['nom']
          prix = lboosters[current-1]['prix']

        if current == 5:
          await ctx.send("Vous ne pouvez pas vous procurer un ``ULTRA BOOSTER - Règles`` de cette manière. Si vous avez vos règles, contactez le maître Antoine au plus vite.")
          return

        await ctx.send(f"Vous êtes sur le point d'acheter le `'{name} - {vnom}'` ! Êtes-vous sûr de votre choix ? (o / oui / y / yes)")

        def check2(m):
          return m.author == ctx.author and m.channel == ctx.channel

        try:
          m = await bot.wait_for('message', timeout=30.0, check=check2)
        except asyncio.TimeoutError:
          await ctx.send("Délai expiré. Vente annulée.")
          return

        if majuscule(m.content) not in ['o', 'y', 'oui', 'yes']:
          await ctx.send("À la revoyure !")
          return
        else:
          users = await get_info_data()
          if prix <= users[str(user.id)]['wallet']:
            await ctx.send("Achat en cours...")
            if name == "ULTRA ITEM":
              await update_info(ctx.author, current-11,"items")
            elif name == "ULTRA PANINI":
              await update_info(ctx.author, current-6,"paninis")
            else:
              await update_info(ctx.author, current, "boosters")
            await update_info(ctx.author, -prix)
            await ctx.send(f"-{prix}PM....")
            await asyncio.sleep(3)
            await ctx.send(f"``{name} - {vnom}`` ajouté à votre inventaire ! Consultez votre inventaire avec le `!profil` !")
            return
          else:
            await ctx.send("Vous n'avez pas suffisamment de Points-Marrons!")
            return

      for button in buttons:
        await msg.remove_reaction(button, ctx.author)

      if current != previous_page:
        await msg.edit(embed=storepages[current])
  return

@bot.command()
async def buy(ctx, indice:str=None):
  """
  Permet d'acheter un personnage d'indice [indice].
  """
  if indice == None:
    await ctx.send("Vous devez citer un indice.")
    return
  elif (indice[0] == '-' and verifneg(indice)) or indice == '0':
    await ctx.send("Indice invalide, il est trop faible. La première carte-personnage porte l'indice 1.")
    return
  elif not verifnombre(indice):
    await ctx.send("Vous devez citer un indice et pas autre chose !")
    return
    
  indice = int(indice)
  
  if indice > len(cards):
    await ctx.send(f"Indice invalide, il est trop élevé. La dernière carte-personnage actuelle porte l'indice {len(cards)}.")
    return
  
  if cards[indice-1]['rarete'] == 0:
    await ctx.send("Vous n'avez pas honte ?! On n'achète pas un enfant de la sorte !")
    return
  users = await get_info_data()
  if indice in users[str(ctx.author.id)]['indices']:
    await ctx.send(f"Vous possédez déjà la carte-personnage de {cards[indice-1]['prenom']}!")
    return
  info = users[str(ctx.author.id)]
  carte = cards[indice-1]
  if info['wallet'] < carte['prix']:
    diff = carte['prix'] - info['wallet']
    await ctx.send(f"La carte-personnage de {info['prenom']} est trop chère ! il vous manque `{diff}PM` dans votre porte-marrons pour espérer vous la procurer.")
    return
  else:
    if carte['nom'] == '-':
      prenom = carte['prenom']
      nom = ''
    elif carte['manga'] == 'One Piece' and carte['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
      prenom = f"{carte['nom']} D. {carte['prenom']}"
      nom = ""
    else:
      prenom = carte['prenom']
      nom = carte['nom']

    couleur = dcouleur(carte['rarete'])
    
    em = discord.Embed(title=f"{prenom} {nom}",description=f"Indice : {indice}", color = couleur)
    em.add_field(name="Manga :", value=f"{carte['manga']}")
    em.add_field(name="Prestige :", value=f"{carte['rarete']}⭐")
    em.add_field(name="Prix :", value=f"{carte['prix']} PM")
    em.set_image(url=f"{carte['url']}")
    await ctx.send(embed=em)
    await ctx.send(f"Êtes-vous certain de vouloir vous procurer la carte de {prenom} pour la somme de `{carte['prix']}PM` ? (o/y/oui/yes)")

    def check2(m):
      return m.author == ctx.author and m.channel == ctx.channel

    try:
      m = await bot.wait_for('message', timeout=30.0, check = check2)
    except asyncio.TimeoutError:
      await ctx.send(f"temps écoulé. Achat annulé.")
      return
      
    if majuscule(m.content) in ['o', 'y', 'oui', 'yes']:
      await ctx.send("Achat en cours...")
      await update_info(ctx.author, indice, 'indices')
      await update_info(ctx.author, -carte['prix'], 'wallet')
      await asyncio.sleep(2)
      await ctx.send(f"Achat effectué ! Vous possédez à présent la carte de {carte['prenom']} ! Félicitations !")
      return
    else:
      await ctx.send("En vous remerciant !")
      return
    
    




import francais
authors = francais.authors


@bot.command()
async def rtt(ctx):
  choix = [x for x in authors]
  a = random.choice(choix)
  print(a)
  choix = [x for x in authors[a]]
  used = []
  while len(used) < len(choix):
    r = random.choice([x for x in choix if x not in used])
    used.append(r)
    if r == 'mvtLittéraire':
      nr = "Mouvement littéraire"
    elif r == 'info':
      nr = "informations"
    else:
      nr = r
    await ctx.send(f"`{nr} de {a}`")

    def check2(m):
      return m.author == ctx.author and m.channel == ctx.channel

    try:
      await bot.wait_for('message', timeout=150.0, check = check2)
    except asyncio.TimeoutError:
      await ctx.send(f"temps écoulé. La réponse était {authors[a][r]}.")
      return

    await ctx.send(authors[a][r])
  await ctx.send("`QUESTIONNAIRE TERMINÉ.`")


gen = gen.gen

@bot.command()
async def genar(ctx):
  for x in gen:
    em = discord.Embed(title=f"{x['pnom']} {x['nom']}")
    em.add_field(name="Prestige :",value= x['rar']*'⚽', inline=False)
    if x['gr'] != '-':
      em.add_field(name='Thème :', value=f"{x['theme']} - {x['gr']}",inline=False)
    else:
      em.add_field(name="Thème :", value=f"{x['theme']}", inline=False)
    em.set_image(url=f"{x['img']}")
    await ctx.send(embed=em)

#Ici, on définit les prix des différents niveaux de prestige des cartes.
rar = [0, 1000, 2000, 5000, 25000, 75000, 250000, 1500000]
ptsi = [100,150,225,338,507,760,1140]
# 1 - 100 | 2 - 150 | 3 - 225 | 4 - 338 | 5 - 507 | 6 - 760 | 7 - 1140


dropsboosters = [([68, 93, 99, 100, 110, 110, 110],[40, 78, 94, 98, 100, 110, 110]),
                 ([25, 60, 95, 99, 100, 110, 110],[10, 45, 83, 96, 100, 110, 110]),
                 ([10, 35, 70, 90, 99, 100, 110],[3, 29, 65, 86, 97, 100, 110]),
                ([5, 25, 55, 81, 97, 99.9, 100],[3, 23, 53, 77, 95, 98, 100]),
                ([35, 65, 85, 95, 100, 110, 110],[31, 62, 83, 94, 100, 110, 110]),
                ([35, 60, 80, 95, 99, 100, 110],[31, 57, 78, 94, 98, 100, 110])]


@bot.command(aliases=['ob'], pass_context=True)
#@commands.cooldown(1, 60 * 1, commands.BucketType.user)
async def openbooster(ctx, indice: int = 0):
  """
  Permet d'ouvrir un booster.
  """
  if alt(ctx.author):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  users = await get_info_data()
  if users[str(ctx.author.id)]['boosters'][0] == 0:
    await ctx.send("Vous n'avez aucun booster !")
    return

  vodkapple = False
  drops = 0
  if users[str(ctx.author.id)]['vodkapple'] == True:
    await ctx.send("`DROP VODKAPPLE` UTILISÉE !")
    vodkapple = True
    drops = 1

  boosters = users[str(ctx.author.id)]['boosters']
  if indice > len(lboosters):
    await ctx.send("Ce booster n'existe pas.")
    return
  elif indice not in boosters:
    await ctx.send("Vous ne possédez pas ce booster.")
    return
  else:
    for testbooster in lboosters:
      if testbooster['ind'] == indice:
        booster = testbooster
    tdrops = dropsboosters[indice-1][drops]
    name = "ULTRA BOOSTER - " + booster['nom']
    nb = booster['nbcards']
    gar = booster['gar']
    await ctx.send(f"Ouverture du `{name}` en cours...")
    await ctx.send(f"{booster['img']}")
    if indice == 6:
      r = [users[str(ctx.author.id)]['manga']]
    else:
      r = [x for x in mangas if (x != "autres")]
    await asyncio.sleep(1)
    boost = []
    gain = 0
    rec = ''
    liste = ''
    for pre in gar:
      if gar == 7:
        raradapt = []
        for card in cards:
          if card['rarete'] == 7:
            raradapt.append(card['num'])
        obt = random.choice(raradapt)
        if cards[obt-1]['rarete'] != 7:
          await ctx.send("Erreur algorithmique. Veuillez réessayer.")
          return

        card = cards[obt-1]
        
        if card['nom'] == '-':
          prenom = card['prenom']
          nom = ''
        elif card['manga'] == 'One Piece' and card['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
          prenom = f"{card['nom']} D. {card['prenom']}"
          nom = ""
        else:
          prenom = card['prenom']
          nom = card['nom']


        if card['num'] in users[str(ctx.author.id)]['indices']:
          await update_info(ctx.author,card['prix']//2)
          gain = gain + card['prix']//2
        else:
          await update_info(ctx.author, card['num'], 'indices')
          rec = rec + f'- {prenom} {nom} | Indice : {card["num"]}\n'
          liste = liste + f'{card["num"]}!'

        couleur = dcouleur(card['rarete'])

        em = discord.Embed(title=f"{prenom} {nom}", color=couleur)
        em.add_field(name="Manga :", value=card['manga'])
        em.add_field(name="Prestige :", value=card['rarete'] * '⭐')
        em.add_field(name='Prix :', value=card['prix'])
        em.add_field(name="Indice :", value=card['num'])
        em.add_field(name="Statut :", value="GARANTI")
        em.set_image(url=card['url'])
        boost.append(em)
        nb = nb - 1

      else:
        manga = random.choice(r)
        raradapt = []
        for card in cards:
          if card['rarete'] == pre and sansspace(majuscule(card['manga'])) == manga:
            raradapt.append(card['num'])
        obt = random.choice(raradapt)
        card = cards[obt-1]
        
        if card['nom'] == '-':
          prenom = card['prenom']
          nom = ''
        elif card['manga'] == 'One Piece' and card['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
          prenom = f"{card['nom']} D. {card['prenom']}"
          nom = ""
        else:
          prenom = card['prenom']
          nom = card['nom']

        if card['num'] in users[str(ctx.author.id)]['indices']:
          await update_info(ctx.author, card['prix']//2)
          gain = gain + card['prix']//2
        else:
          await update_info(ctx.author, card['num'],'indices')
          rec = rec + f'- {card["prenom"]} {nom} | Indice : {card["num"]}\n'
          liste = liste + f'{card["num"]}!'

        couleur = dcouleur(card['rarete'])

        em = discord.Embed(title=f"{prenom} {nom}", color=couleur)
        em.add_field(name="Manga :", value=card['manga'])
        em.add_field(name="Prestige :", value=card['rarete'] * '⭐')
        em.add_field(name='Prix :', value=card['prix'])
        em.add_field(name="Indice :", value=card['num'])
        em.add_field(name="Statut :", value="GARANTI")
        em.set_image(url=card['url'])
        boost.append(em)
        nb = nb - 1
    for i in range(nb):
      manga = random.choice(r)
      raradapt = []
      na = random.uniform(1, 100)
      if na <= tdrops[0]:
        rarete = 1
      elif na <= tdrops[1]:
        rarete = 2
      elif na <= tdrops[2]:
        rarete = 3
      elif na <= tdrops[3]:
        rarete = 4
      elif na <= tdrops[4]:
        rarete = 5
      elif na <= tdrops[5]:
        rarete = 6
      else:
        rarete = 7
      couleur = dcouleur(rarete)

      for card in cards:
        if card['rarete'] == rarete and sansspace(majuscule(card['manga'])) == manga:
          raradapt.append(card['num'])
      obt = random.choice(raradapt)

      card = cards[obt-1]
        
      if card['nom'] == '-':
        prenom = card['prenom']
        nom = ''
      elif card['manga'] == 'One Piece' and card['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
        prenom = f"{card['nom']} D. {card['prenom']}"
        nom = ""
      else:
        prenom = card['prenom']
        nom = card['nom']

      if card['num'] in users[str(ctx.author.id)]['indices']:
        await update_info(ctx.author, card['prix']//2)
        gain = gain + card['prix']//2
      else:
        await update_info(ctx.author, card['num'], 'indices')
        rec = rec + f'- {prenom} {nom} | Indice : {card["num"]}\n'
        if nb > 0:
          liste = liste + f'{card["num"]}!'
        else:
          liste = liste + f'{card["num"]}'

      em = discord.Embed(title=f"{prenom} {nom}", color=couleur)
      em.add_field(name="Manga :", value=card['manga'])
      em.add_field(name="Prestige :", value=card['rarete'] * '⭐')
      em.add_field(name='Prix :', value=card['prix'])
      em.add_field(name="Indice :", value=card['num'])
      em.set_image(url=card['url'])
      boost.append(em)

    await ctx.send("Chargement des récompenses, veuillez patienter...")
    await asyncio.sleep(2)
    for i in boost:
      await ctx.send(embed=i)
      await asyncio.sleep(2)

    if rec == '':
      await ctx.send(f"Vous aviez déjà toutes les cartes présentes dans ce booster !\nPM récoltés: `{gain}PM`")
      return
    em = discord.Embed(title=f"BILAN DES RÉCOMPENSES DE {ctx.author} :", color=discord.Color.gold(),description="affiche les cartes **ajoutées à l'inventaire** ainsi que les PM récoltés **avec les doublons de cartes déjà obtenues**.")
    em.add_field(name="Liste des récompenses :", value=rec)
    em.add_field(name="PM récoltés :", value=f'{gain}PM')
    em.set_thumbnail(url=lboosters[indice-1]['img'])
    await ctx.send(embed=em)
    await update_info(ctx.author, -indice, 'boosters')
    if vodkapple:
      await update_info(ctx.author, 0, 'vodkapple')
    liste2 = ''
    i = 0
    while i < len(liste) - 1:
      liste2 = liste2 + liste[i]
      i = i + 1
    await ctx.send(f"``{liste2}``")
    return


dropspaninis = [([90, 96, 99, 100, 110, 110, 110],[75, 86, 97, 100, 110, 110, 110]),
                 ([50, 65, 95, 99, 100, 110, 110],[40, 60, 92, 98, 100, 110, 110]),
                 ([20, 50, 75, 90, 99, 100, 110],[15, 47, 73, 89, 98, 100, 110]),
                ([10, 20, 40, 75, 93, 99, 100],[8, 18, 36, 72, 90, 98, 100]),
                ([5, 15, 25, 55, 75, 95, 100],[3, 12, 22, 53, 73, 94, 100])]


@bot.command(aliases=['op'],pass_context=True)
#@commands.cooldown(1, 60 * 1, commands.BucketType.user)
async def openpanini(ctx, indice: int = 0):
  """
  Permet d'ouvrir un panini.
  """
  if alt(ctx.author):
    await ctx.send("Les comptes secondaires ne sont pas autorisés à utiliser cette fonctionnalité.")
    return

  users = await get_info_data()
  if users[str(ctx.author.id)]['paninis'][0] == 0:
    await ctx.send("Vous n'avez aucun panini !")
    return

  vodkapple = False
  drops = 0
  if users[str(ctx.author.id)]['vodkapple'] == True:
    vodkapple = True
    drops = 1

  paninis = users[str(ctx.author.id)]['paninis']
  if indice > len(lpaninis):
    await ctx.send("Ce panini n'existe pas.")
    return
  elif indice not in paninis:
    await ctx.send("Vous ne possédez pas ce panini.")
    return
  else:
    for testpanini in lpaninis:
      if testpanini['ind'] == indice:
        panini = testpanini
    tdrops = dropspaninis[indice-1][drops]
    name = "ULTRA PANINI - " + panini['nom']
    nb = panini['nbcards']
    gar = panini['gar']
    await ctx.send(f"Ouverture du `{name}` en cours...")
    await ctx.send(f"{panini['img']}")
    if indice == 6:
      r = [users["29959166804518502"]['manga']]
    else:
      r = [x for x in mangas if (x != "autres")]
    await asyncio.sleep(1)
    boost = []
    gain = 0
    rec = ''
    liste = ''
    for pre in gar:
      print(pre)
      if pre == 7:
        raradapt = []
        for card in cards:
          if card['rarete'] == 7:
            raradapt.append(card['num'])
        obt = random.choice(raradapt)
        if cards[obt-1]['rarete'] != 7:
          await ctx.send("Erreur algorithmique. Veuillez réessayer.")
          return

        card = cards[obt-1]
        
        if card['nom'] == '-':
          prenom = card['prenom']
          nom = ''
        elif card['manga'] == 'One Piece' and card['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
          prenom = f"{card['nom']} D. {card['prenom']}"
          nom = ""
        else:
          prenom = card['prenom']
          nom = card['nom']


        if card['num'] in users[str(ctx.author.id)]['indices']:
          await update_info(ctx.author,card['prix']//2)
          gain = gain + card['prix']//2
        else:
          await update_info(ctx.author, card['num'], 'indices')
          rec = rec + f'- {prenom} {nom} | Indice : {card["num"]}\n'
          liste = liste + f'{card["num"]}!'

        couleur = dcouleur(card['rarete'])

        em = discord.Embed(title=f"{prenom} {nom}", color=couleur)
        em.add_field(name="Manga :", value=card['manga'])
        em.add_field(name="Prestige :", value=card['rarete'] * '⭐')
        em.add_field(name='Prix :', value=card['prix'])
        em.add_field(name="Indice :", value=card['num'])
        em.add_field(name="Statut :", value="GARANTI")
        em.set_image(url=card['url'])
        boost.append(em)
        nb = nb - 1

      else:
        manga = random.choice(r)
        raradapt = []
        for card in cards:
          if card['rarete'] == pre and sansspace(majuscule(card['manga'])) == manga:
            raradapt.append(card['num'])
        obt = random.choice(raradapt)
        card = cards[obt-1]
        
        if card['nom'] == '-':
          prenom = card['prenom']
          nom = ''
        elif card['manga'] == 'One Piece' and card['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
          prenom = f"{card['nom']} D. {card['prenom']}"
          nom = ""
        else:
          prenom = card['prenom']
          nom = card['nom']

        if card['num'] in users[str(ctx.author.id)]['indices']:
          await update_info(ctx.author, card['prix']//2)
          gain = gain + card['prix']//2
        else:
          await update_info(ctx.author, card['num'],'indices')
          rec = rec + f'- {card["prenom"]} {nom} | Indice : {card["num"]}\n'
          liste = liste + f'{card["num"]}!'

        couleur = dcouleur(card['rarete'])

        em = discord.Embed(title=f"{prenom} {nom}", color=couleur)
        em.add_field(name="Manga :", value=card['manga'])
        em.add_field(name="Prestige :", value=card['rarete'] * '⭐')
        em.add_field(name='Prix :', value=card['prix'])
        em.add_field(name="Indice :", value=card['num'])
        em.add_field(name="Statut :", value="GARANTI")
        em.set_image(url=card['url'])
        boost.append(em)
        nb = nb - 1
    for i in range(nb):
      manga = random.choice(r)
      raradapt = []
      na = random.uniform(1, 100)
      if na <= tdrops[0]:
        rarete = 1
      elif na <= tdrops[1]:
        rarete = 2
      elif na <= tdrops[2]:
        rarete = 3
      elif na <= tdrops[3]:
        rarete = 4
      elif na <= tdrops[4]:
        rarete = 5
      elif na <= tdrops[5]:
        rarete = 6
      else:
        rarete = 7
      couleur = dcouleur(rarete)

      for card in cards:
        if card['rarete'] == rarete and sansspace(majuscule(card['manga'])) == manga:
          raradapt.append(card['num'])
      obt = random.choice(raradapt)

      card = cards[obt-1]
        
      if card['nom'] == '-':
        prenom = card['prenom']
        nom = ''
      elif card['manga'] == 'One Piece' and card['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
        prenom = f"{card['nom']} D. {card['prenom']}"
        nom = ""
      else:
        prenom = card['prenom']
        nom = card['nom']

      if card['num'] in users[str(ctx.author.id)]['indices']:
        await update_info(ctx.author, card['prix']//2)
        gain = gain + card['prix']//2
      else:
        await update_info(ctx.author, card['num'], 'indices')
        rec = rec + f'- {prenom} {nom} | Indice : {card["num"]}\n'
        if nb > 0:
          liste = liste + f'{card["num"]}!'
        else:
          liste = liste + f'{card["num"]}'

      em = discord.Embed(title=f"{prenom} {nom}", color=couleur)
      em.add_field(name="Manga :", value=card['manga'])
      em.add_field(name="Prestige :", value=card['rarete'] * '⭐')
      em.add_field(name='Prix :', value=card['prix'])
      em.add_field(name="Indice :", value=card['num'])
      em.set_image(url=card['url'])
      boost.append(em)

    await ctx.send("Chargement des récompenses, veuillez patienter...")
    await asyncio.sleep(2)
    for i in boost:
      await ctx.send(embed=i)
      await asyncio.sleep(2)

    if rec == '':
      await ctx.send(f"Vous aviez déjà toutes les cartes présentes dans ce panini !\nPM récoltés: `{gain}PM`")
      return
    em = discord.Embed(title=f"BILAN DES RÉCOMPENSES DE {ctx.author} :", color=discord.Color.gold(),description="affiche les cartes **ajoutées à l'inventaire** ainsi que les PM récoltés **avec les doublons de cartes déjà obtenues**.")
    em.add_field(name="Liste des récompenses :", value=rec)
    em.add_field(name="PM récoltés :", value=f'{gain}PM')
    em.set_thumbnail(url=lboosters[indice-1]['img'])
    await ctx.send(embed=em)
    await update_info(ctx.author, -indice, 'paninis')
    if vodkapple:
      await update_info(ctx.author, 0, 'vodkapple')
    liste2 = ''
    i = 0
    while i < len(liste) - 1:
      liste2 = liste2 + liste[i]
      i = i + 1
    await ctx.send(f"``{liste2}``")
    return

@bot.command(aliases=['ui'])
async def useitem(ctx, objet: str, usx: discord.Member = None):
  """
  Permet d'utiliser un ULTRA ITEM.
  """
  if not verifnombre(objet):
    await ctx.send("Vous devez citer un numéro d'item !")
    return
  objet = int(objet)
  users = await get_info_data()
  if str(ctx.author.id) not in users:
    await ctx.send("Vous n'avez pas de compte informatique !")
    return
  else:
    if users[str(ctx.author.id)]['items'][0] == 0:
      await ctx.send("Vous n'avez aucun objet ! François est navré !")
      return
    elif objet not in users[str(ctx.author.id)]['items']:
      await ctx.send("Vous ne possédez pas cet objet ! François est navré !")
      return
    else:
      await update_info(ctx.author,-objet,'items')
      await ctx.send("ULTRA ITEM enclenché ! @nopeveryone")
      await asyncio.sleep(1)
      await ctx.send("...")
      await asyncio.sleep(2)
      for item in litems:
        if item['ind'] == objet:
          name = item['nom']
          prix = item['prix']
      if name == 'Banckeur':
        await ctx.send("**Banckeur is hacking.**")
        await asyncio.sleep(2)
        await ctx.send("...")
        await asyncio.sleep(1)
        await ctx.send("https://wpformation.com/wp-content/uploads/2019/01/hack-WordPress.png")
        for user in users:
          id = await bot.fetch_user(user)
          prebanque = users[user]['bank']
          if prebanque > 0:
            tok = random.randint(1,100)
            if tok <= 60:
              brude = random.uniform(0.1,1.9)
            elif tok <= 85:
              brude = random.uniform(0.00001,0.1)
            elif tok <= 95:
              brude = random.uniform(1.9,2.0)
            else:
              brude = random.uniform(2.1,3.0)
            newbanque = int(prebanque*brude)
            if brude >=1.0:
              await update_info(id, newbanque-prebanque,'bank')
            else:
              await update_info(id, -(prebanque-newbanque),"bank")
            users2 = await get_info_data()
            nbank = users2[user]['bank']
            await asyncio.sleep(3)
            await id.send(f"François est désoeuvré ! La banque a été hackée par un utilisateur de l'ULTRA ITEM - Banckeur ! Votre banque a été affectée par un ratio de `x{round(brude,2)}` ! Vous êtes passé de `{prebanque}PM` à `{nbank}PM` ! François est navré pour la gêne occasionnée !")
            return
      elif name == 'Drop Vodkapple':
        await ctx.send("**Glouglouglou...**")
        await asyncio.sleep(2)
        await ctx.send("...")
        await asyncio.sleep(1)
        await ctx.send("https://www.planetesante.ch/var/ezdemo_site/storage/images/media/images/01_images-articles/lmd_alcool_trop_combien/990153-1-fre-CH/LMD_alcool_trop_combien.jpg")
        await update_info(ctx.author, 0, 'vodkapple')
        await ctx.send(f"{ctx.author.mention} a ingéré la `Drop Vodkapple` ! Il aura un boost de drops sur son prochain booster/panini !")
        return
      elif name == "Spécichange":
        await ctx.send("**\/\/\/\/\/\...**")
        await asyncio.sleep(2)
        await ctx.send("...")
        await asyncio.sleep(1)
        manga = random.choice(mangas)
        i = 0
        while trad[i][0] != manga and i < len(trad):
          i = i + 1
        mangatrad = trad[i][1]
        await update_info(ctx.author, 0, 'manga', manga)
        await ctx.send(f"{ctx.author.mention} a changé le contenu de ses `ULTRA BOOSTER - SPÉCIAL` : ils contiendront maintenant des personnages de l'univers de {mangatrad} !")
        return
      elif name == "Volbombe":
        if usx == None:
          await update_info(ctx.author,objet,'items')
          await ctx.send("Vous devez cibler quelqu'un !")
          return
        await ctx.send("**Hehehehe...**")
        await asyncio.sleep(2)
        await ctx.send("...")
        await asyncio.sleep(1)
        if str(usx.id) not in users:
          await ctx.send(f"{usx.mention} n'a pas encore de compte informatique !")
          return
        if users[str(usx.id)]['veutvol'][0]:
          await ctx.send("Vous devez cibler quelqu'un qui n'est pas encore pris pour cible !")
          await update_info(ctx.author,objet,'items')
          return
        await update_info(usx,0,"veutvol","blude",ctx.author)
        await update_info(ctx.author,0,"vol","blude",usx)
        await ctx.send(f"{ctx.author.mention} a pris {usx.mention} pour cible ! Gare à vous !")
        return
      else:
        await update_info(ctx.author,objet,'items')
        await ctx.send("ULTRA ITEM non détecté !")
        return
        
        































@bot.command()
async def psge(ctx):
  def check(m):
    return m.author == ctx.author and m.channel == ctx.channel

  await ctx.send("prénom")

  try:
    msg = await bot.wait_for('message', timeout=300.0, check=check)
  except asyncio.TimeoutError:
    await ctx.send("Vous n'avez pas répondu suffisament rapidement, l'achat est annulé.")
    return

  prenom = msg.content

  await ctx.send("nom")

  try:
    msg = await bot.wait_for('message', timeout=300.0, check=check)
  except asyncio.TimeoutError:
    await ctx.send("Vous n'avez pas répondu suffisament rapidement, l'achat est annulé.")
    return

  nom = msg.content

  await ctx.send("url")

  try:
    msg = await bot.wait_for('message', timeout=300.0, check=check)
  except asyncio.TimeoutError:
    await ctx.send("Vous n'avez pas répondu suffisament rapidement, l'achat est annulé.")
    return

  url = msg.content

  await ctx.send("rareté")

  try:
    msg = await bot.wait_for('message', timeout=300.0, check=check)
  except asyncio.TimeoutError:
    await ctx.send("Vous n'avez pas répondu suffisament rapidement, l'achat est annulé.")
    return

  rarete = msg.content
  if not verifnombre(rarete) and int(rarete) < 7:
    await ctx.send("Une erreur est survenue, veuillez réessayer.")
    return

  ptstemp = ptsi[int(rarete)-1]
  attk = random.randint(1,ptstemp-2)
  ptstemp = ptstemp - attk
  defs = random.randint(1,ptstemp-1)
  ptstemp = ptstemp - defs
  inte = ptstemp
  

  channel = bot.get_channel(947502162995466291)
  indice = await upplace()
  await channel.send('{' + f'"prenom": "{prenom}", "nom": "{nom}", "manga": "Inazuma Eleven","url": "{url}" ,"rarete": {rarete}, "prix": rar[{rarete}], "num": {indice}, "attack": {attk}, "defense": {defs}, "intelligence": {inte}' + '},')
  return


@bot.command()
async def upplace():
  users = await get_info_data()

  users["299591668045185025"]['rotul'] += 1  
  
  with open('info.json', 'w') as f:
    json.dump(users, f)

  print('ouais')
  bal = users["299591668045185025"]['rotul']
  return bal


@bot.command()
async def maj(ctx):
  """
  Renvoie le patchnote de la dernière maj en date.
  """
  em = discord.Embed(title="MISE À JOUR : François 2.1.0.0", description='Patch note de la mise à jour', color=discord.Color.red())
  em.add_field(name="COMMANDES :",value="- !chat : 13->23 évènements (10 inédits et 2 'aggravés')\n- !question : +8 réponses\n- !constitution : affiche la Constitution.\n- !mail : permet d'envoyer un message privé via François à quelqu'un.",inline=False)
  em.add_field(name="AUTRES :",value="- cooldown : message modifié et système amélioré.\n- !help : intégralement refaite.\n- !report : modifications en interne.\n- !pmclaim : optimisée et plus rapide.\n- !claim : système interne grandement amélioré (plus rapide et optimisé).\n- !profil : refaite, améliorée, complétée, mise à jour.\n- !search : refaite et améliorée (plus rapide).\n- !nr [opt:limit] : on peut, à présent, définir une limite à la commande !nr. Par défaut, la limite est fixée à 100.",inline=False)
  em.add_field(name="MODIFICATIONS MAJEURES :",value="- !galeryshow (!gs) : descendante de !scards, permet d'afficher sa galerie en images.\n- !galerylist (!gl) : permet d'afficher une liste de ses cartes.\n- !openpanini (!op) : Séparation entre les boosters et les paninis, il faudra utiliser cette commande pour ouvrir des paninis.\n- !store [opt:page] : on peut à présent donner le numéro de la page vers laquelle on veut directement se diriger dans la boutique.",inline=False)
  em.add_field(name="NOUVEAUTÉS :",value="- Vous pouvez dorénavant définir une 'firstcard'.\n- !changefirstcard (!cfc) : permet de changer sa firstcard.\n- !changeordregalery (!cog) : permet de modifier l'ordre de rangement de vos cartes.\n- !lstore : permet d'afficher la liste des articles sous forme de liste.\n⚠ **ULTRA ITEMS** ⚠ : Ils rejoignent le catalogue du !store. Ces items sont au nombre de 4 et ont chacun un objectif et un effet très précis.\n- Le Banckeur : permet de hacker les banques-marrons de tous les utilisateurs et altère leur nombre de Points-Marrons.\n- Drop Vodkapple : permet de modifier les taux de drops des cartes à plus haut prestige dans les boosters et les paninis.\n- Spécichange : permet de changer le contenu de vos `ULTRA BOOSTER - Spécial`.\n- Volbombe : permet de voler le prochain !claim d'un autre utilisateur.\nCes items vont valoriser les interactions entre utilisateurs et vont obliger chacun à réfléchir à ses actions, stratégiquement, en fonction des évènements qui pourraient arriver.", inline=False)
  await ctx.send(embed=em)
  return
  

@bot.command()
async def stats(ctx, indice: int = None):
  """
  Affiche les points d'attributs du personnage 'psge'.
  """
  if indice == None:
    await ctx.send("Vous devez citer un indice de carte-personnage.")
    return

  if indice > len(cards):
    await ctx.send("Indice invalide.")
    return
  if indice < 1:
    await ctx.send("Indice invalide.")
    return
    
  card = cards[indice-1]
  if card['rarete'] == 0:
    await ctx.send("On ne cherche pas les statistiques d'un enfant de la sorte !")
    return
  couleur = dcouleur(card['rarete'])

  if card['nom'] == '-':
    prenom = card['prenom']
    nom = ''
  elif card['manga'] == 'One Piece' and card['nom'] in ['MONKEY', 'GOL', 'PORTGAS', 'TRAFALGAR', 'ROCKS', 'HAGUAR', 'MARSHALL']:
    prenom = f"{card['nom']} D. {card['prenom']}"
    nom = ""
  else:
    prenom = card['prenom']
    nom = card['nom']

  em = discord.Embed(title=f'{prenom} {nom}',color=couleur)
  em.set_thumbnail(url=f'{card["url"]}')
  em.add_field(name="ATT :", value=f'{card["attack"]} ⚔')
  em.add_field(name='DEF :', value=f'{card["defense"]} 🛡')
  em.add_field(name='INT :', value=f'{card["intelligence"]} 🧠')
  em.add_field(name='STA :', value=f'{card["rarete"]} ⭐')
  em.add_field(name='PPM :', value=f'{card["prix"]} 💰')

  await ctx.send(embed=em)
  return




keep_alive()
bot.run('bludre')
