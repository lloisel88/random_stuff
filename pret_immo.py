# import dependencies
from matplotlib import pyplot as plt

# calculs basés sur https://www.pretto.fr/taux-immobilier/calcul-interet/
def mensualite(capital = 500000, taux = 0.015, annees = 20):
    numerateur = capital * taux / 12
    denominateur = 1 - (1 + taux / 12) ** (-12 * annees)
    return numerateur / denominateur

def interets_totaux(capital, annees, mensualite):
    return 12 * annees * mensualite - capital

capital = 500000
taux = 0.018
annees = 20

print("Pour un emprunt de", capital, "euros sur une durée de", annees, "années à un taux de", 
taux, "%, la valeur de la mensualité est de:", mensualite(capital, taux, annees), 
"euros. Les intérêts totaux à rembourser valent:", 
interets_totaux(capital, annees, mensualite(capital, taux, annees)), "euros")

# variation des mensualités et des intérêts totaux à rembourser en fonction du nombre d'années
ann = range(15, 26)
mensualite_annees = [mensualite(capital, taux, i)
                        for i in ann]
interets_annees = [interets_totaux(capital, j, mensualite(capital, taux, j))
                        for j in ann]

# plot des variations des intérêts totaux en fonction du nombre d'années de paiement
fig, ax = plt.subplots(2, 1)
ax[0].scatter(ann, interets_annees)
ax[0].set_title("Variation des intérêts totaux à rembourser en fonction du nombre d'années du prêt")
ax[0].set_ylabel("Intérêts totaux à rembourser (euros)")
plt.xlabel("Nombre d'années de remboursement du prêt")
ax[1].scatter(ann, mensualite_annees)
ax[1].set_title("Variation des mensualités de remboursement en fonction du nombre d'années du prêt")
ax[1].set_ylabel("Mensualité (euros)")
plt.show()

# Evolution du capital remboursé au cours du temps (à compléter)
"""
def capital_rembourse_annuel:
    interets_annee = 0
    return 12 * mensualite - interets_annee
"""