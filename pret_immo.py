# import dependencies
from matplotlib import pyplot as plt

def calcul_interets(capital = 500000, taux = 0.015, annees = 20):
    # si les intérêts remboursés décroissent linéairement de la première année à la dernière année (0,
    # il ne reste plus de capital à rembourser donc plus d'intérêts), les intérêts totaux sont 
    # égaux à la surface sous la décroissance linéaire, c'est à dire l'aire du triangle rectangle
    return (annees * capital * taux) / 2 

# print(calcul_interets(500000, 0.015, 20))

# plot l'augmentation des intérêts pour un prêt donné en fonction des années 
ann = range(15,26)
interets_annees = [calcul_interets(annees = i) 
                    for i in ann]

plt.plot(ann, interets_annees, marker = "o", linestyle = "solid")
plt.xlabel("Années de remboursement")
plt.ylabel("Montant des intérêts totaux")
plt.title(r"Montant des intérêts pour un prêt de 500 000 € avec un taux de 1,5% en fonction du nombre d'années")
plt.show()

# plot le remboursement du prêt 
# print(calcul_interets(annees = annee) for annee in annees)

