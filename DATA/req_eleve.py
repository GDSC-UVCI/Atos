import mysql.connector

# In `DATA/req_eleve.py`

def ajouter_eleve_db(curseur, eleve):
    query = """
    INSERT INTO eleves (date_naissance, ville, prenom, nom, telephone, classe, matricule)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    curseur.execute(query, (eleve.get_date_naissance, eleve.get_ville, eleve.get_prenom, eleve.get_nom, eleve.get_telephone, eleve.get_classe, eleve.get_matricule))

def modifier_eleve_db(curseur, eleve):
    query = """
    UPDATE eleves
    SET date_naissance = %s, ville = %s, prenom = %s, nom = %s, telephone = %s, classe = %s
    WHERE matricule = %s
    """
    curseur.execute(query, (eleve.get_date_naissance, eleve.get_ville, eleve.get_prenom, eleve.get_nom, eleve.get_telephone, eleve.get_classe, eleve.get_matricule))

def supprimer_eleve_db(curseur, identifiant):
    query = "DELETE FROM eleves WHERE matricule = %s"
    curseur.execute(query, (identifiant,))

def lister_eleves(curseur):
    """Liste tous les élèves de la base de données."""
    query = "SELECT * FROM eleves"
    curseur.execute(query)
    return curseur.fetchall()

def recuperer_eleve(curseur, matricule):
    """Récupère un élève par son matricule."""
    query = "SELECT * FROM eleves WHERE matricule = %s"
    curseur.execute(query, (matricule,))
    return curseur.fetchone()