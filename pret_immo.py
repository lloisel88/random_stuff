# import dependencies
from matplotlib import pyplot as plt

def calcul_interets(capital = 500000, taux = 0.015, annees = 20):
    # si les intérêts remboursés décroissent linéairement de la première année à la dernière année (0,
    # il ne reste plus de capital à rembourser donc plus d'intérêts), les intérêts totaux sont 
    # égaux à la surface sous la décroissance linéaire, c'est à dire l'aire du triangle rectangle
    return (annees * capital * taux) / 2 

# print(calcul_interets(500000, 0.015, 20))

# plot l'augmentation des intérêts pour un prêt donné en fonction des années 
# ann = range(15,26)
# interets_annees = [calcul_interets(annees = i) 
#                     for i in ann]

# plt.plot(ann, interets_annees, marker = "o", linestyle = "solid")
# plt.xlabel("Années de remboursement")
# plt.ylabel("Montant des intérêts totaux")
# plt.title(r"Montant des intérêts pour un prêt de 500 000 € avec un taux de 1,5% en fonction du nombre d'années")
# plt.show()

# re-calcul des intérêts totaux en prenant pour point de départ l'annuité basée sur les intérêts totaux calculés
# on veut voir si on retombe sur nos pattes (est-ce que l'hypothèse de la décroissance linéaire des intérêts à rembourser est valide)
def calcul_interets_methode_2(capital = 500000, taux = 0.015, annees = 20):
    # initialisation des listes utilisées
    liste_interets_annuel = []
    liste_capital_annuel = []
    liste_capital_restant = []
    # remboursement total = capital + intérêts totaux 
    remboursement_total = capital = calcul_interets(capital, taux, annees) 
    annuite = remboursement_total / annees
    # au début il nous reste tout le capital à rembourser
    capital_restant = capital 
    # pour chaque annee, on calcule les intérêts à rembourser, basés sur le capital restant, puis le capital remboursé, enfin on met à jour le capital restant
    for _ in range(annees):
        interets_annuel = capital_restant * taux
        liste_interets_annuel.append(interets_annuel)
        capital_annuel = annuite - interets_annuel
        liste_capital_annuel.append(capital_annuel)
        capital_restant = capital_restant - capital_annuel 
        liste_capital_restant.append(capital_restant)
    return sum(liste_interets_annuel)

print(calcul_interets(), calcul_interets_methode_2())



