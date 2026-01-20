## Gabriel Lessard - 20 janvier 2026
### Lab 00 - LOG430

### Question 1 
Quelles commandes avez-vous utilisées pour effectuer les opérations UPDATE et DELETE dans MySQL ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

La commande << execute >> du curseur nous permet d'effectuer des commandes SQL sur les tables dans la base de donnée.
De plus, la commande commit nous permet de confirmer les modifications que nous avons fait à la table en question.
``` py
def update(self, user):
    """ Update given user in MySQL """
    self.cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (user.name, user.email, user.id))
    self.conn.commit()
    return self.cursor.rowcount

def delete(self, user_id):
    """ Delete user from MySQL with given user ID """
    self.cursor.execute("DELETE FROM users WHERE id=%s", (user_id))
    self.cursor.commit()
    return self.cursor.rowcount
``` 