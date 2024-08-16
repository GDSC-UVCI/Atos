from mysql.connector import connect
from sqlalchemy.engine import connection_memoize

from Models.personne import Personne
from Models.ICrudEleve import ICRUDEleve
from DATA.req_eleve import ajouter_eleve_db, modifier_eleve_db, supprimer_eleve_db
from DATA.bd import create_connection

class Eleve(Personne, ICRUDEleve):
    """
    Classe représentant un élève, héritant de la classe Personne et de la classe ICRUDEleve.
    """
    __eleves = []

    def __init__(self, dateNaissance, ville, prenom, nom, telephone, classe, matricule):
        super().__init__(dateNaissance, ville, prenom, nom, telephone)
        self.__classe = classe
        self.__matricule = matricule
        Eleve.__eleves.append(self)

    def __str__(self):
        return (f"Eleve n° {self.get_id} : {self.get_nom} {self.get_prenom}, "
                f"née le {self.get_date_naissance} à {self.get_ville}, "  # Utilisation de get_ville()
                f"classe: {self.get_classe}, matricule: {self.get_matricule}, "
                f"téléphone: {self.get_telephone}")

    @property 
    def get_matricule(self):
        return self.__matricule
    
    @property 
    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe            

    def set_matricule(self, matricule):
        self.__matricule = matricule

    # Implémentation des méthodes CRUD
    # Ajouter un élève
    @staticmethod
    def ajouter(cls, dateNaissance, ville, prenom, nom, telephone, classe, matricule):
        nouvel_eleve = cls(dateNaissance, ville, prenom, nom, telephone, classe, matricule)
        connection = create_connection()
        if create_connection() and connection.is_connected():
            try:
                curseur = connection.cursor()
                ajouter_eleve_db(curseur, dateNaissance)
                connection.commit()
                print("Elève ajouté avec succès.")
            except Exception as e:
                print(f"Erreur lors de l'ajout de l'élève: {e}")
                connection.rollback()
            finally:
                curseur.close()
                connection.close()



    # Modifier un élève
    @staticmethod
    def modifier(eleve):
        for index, eleve_existe in enumerate(Eleve.__eleves):
            if eleve_existe.get_id == eleve.get_id:
                Eleve.__eleves[index] = eleve
                return True
        return False

    # Supprimer un élève 
    @staticmethod
    def supprimer(identifiant):
        for index, eleve in enumerate(Eleve.__eleves):
            if eleve.get_matricule == identifiant:
                del Eleve.__eleves[index]
                return True
        return False

    # Obtenir les élèves
    @staticmethod
    def obtenirEleve():
        return [str(eleve) for eleve in Eleve.__eleves]

    # Obtenir un élève par son id
    @staticmethod
    def obtenir(identifiant):
        for eleve in Eleve.__eleves:
            if eleve.get_matricule == identifiant:
                return eleve
        return None
