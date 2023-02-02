import NPC
import location
import mainchar
import items

mainchar.protagonist = mainchar.createchar()
items.pivas.use(mainchar.protagonist)
items.ulun.use(mainchar.protagonist)

mainchar.protagonist.charstate()
mainchar.protagonist.guild='рейвер'
print(mainchar.protstats.__dict__, mainchar.protagonist.type, mainchar.protagonist.guild)
mainchar.protagonist.goto()