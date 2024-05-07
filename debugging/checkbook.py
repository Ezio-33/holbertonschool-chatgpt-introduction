#!/usr/bin/env python3

class Checkbook:
    """
    Classe représentant un carnet de chèques.

    Attributs:
        balance (float): Le solde actuel du carnet de chèques.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de Carnet de
        chèques avec un solde de 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose le montant spécifié dans le carnet de chèques.

        Paramètres:
            amount (float): Le montant à déposer.

        """
        self.balance += amount
        print("Dépôt de €{:.2f}".format(amount))
        print("Solde actuel : €{:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire le montant spécifié du carnet de chèques.

        Paramètres:
            amount (float): Le montant à retirer.

        """
        if amount > self.balance:
            print("Fonds insuffisants pour effectuer le retrait.")
        else:
            self.balance -= amount
            print("Retrait de €{:.2f}".format(amount))
            print("Solde actuel : €{:.2f}".format(self.balance))

    def get_balance(self):
        """
        Affiche le solde actuel du carnet de chèques.
        """
        print("Solde actuel : €{:.2f}".format(self.balance))


def main():
    """
    Lance une boucle qui permet à l'utilisateur d'effectuer des actions
    sur une instance de Carnet de chèques.

    Paramètres:
        None
    """
    cb = Checkbook()
    while True:
        action = input(
            "Que souhaitez-vous faire ? "
            "(déposer, retirer, solde, quitter) : "
        )
        if action.lower() in ['quitter', 'exit']:
            break
        elif action.lower() == 'déposer':
            try:
                amount = float(input("Entrez le montant à déposer : €"))
                cb.deposit(amount)
            except ValueError:
                print("Montant invalide. Veuillez "
                      "entrer une valeur numérique.")
        elif action.lower() == 'retirer':
            try:
                amount = float(input("Entrez le montant à retirer : €"))
                cb.withdraw(amount)
            except ValueError:
                print("Montant invalide. Veuillez "
                      "entrer une valeur numérique.")
        elif action.lower() == 'solde':
            cb.get_balance()
        else:
            print("Commande invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
