import core
from creep import Creep
from ennemi import Ennemi
from joueur import Joueur


def setup():
    print("Setup START----------")

    core.fps = 30
    core.WINDOW_SIZE = [800, 800]
    core.memory("Creep",Creep())
    core.memory("Joueur", Joueur())
    core.memory("listCreep", [])
    core.memory("listJoueur", [])

    core.memory("Ennemi",Ennemi())
    core.memory("listEnnemi", [])

    for c in range(300):
        core.memory("listCreep").append(Creep())
    for j in range(1):
        core.memory("listJoueur").append(Joueur())
    for e in range(5):
        core.memory("listEnnemi").append(Ennemi())

def run():

    core.cleanScreen()

    for c in core.memory("listCreep"):
        c.show(core.screen)

    for e in core.memory("listEnnemi"):
        e.draw(core.screen)
        core.memory("Ennemi").deplacer(core.memory("Joueur"))

    core.memory("Joueur").draw(core.screen)
    core.memory("Joueur").deplacer(core.getMouseLeftClick())

    for c in core.memory("listCreep"):
        if c.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + c.rayon :
            c.dead()
            core.memory("Joueur").grossir()

    for e in core.memory("listEnnemi"):
        if e.position.distance_to(core.memory("Joueur").position) < core.memory("Joueur").rayon + e.rayon:
            e.dead()
            core.memory("Joueur").grossir()






core.main(setup, run)