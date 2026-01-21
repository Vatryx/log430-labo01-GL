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

### Question 2 
Quelles commandes avez-vous utilisées pour effectuer les opérations dans MongoDB ? Avez-vous uniquement utilisé Python ou également du SQL ? Veuillez inclure le code pour illustrer votre réponse.

MongoDB est un style de base de donnée qui utilise le format JSON (clé, valeur). La syntaxe est donc forcément différente et unique pour pouvoir effectuer des opérations dans la base de donnée. Les tables sont appelées des collections et pour effectuer les opérations SELECT INSERT UPDATE DELETE il faut utiliser les commandes find, insert_one, update_one et delete_one de la collection voulue.
``` py
def select_all(self):
        """ Select all users from MongoDB """
        users = []
        for doc in self.collection.find():
            users.append(
                User(
                    str(doc["_id"]),
                    doc.get("name"),
                    doc.get("email")
                )
            )
        return users

    def insert(self, user):
        """ Insert given user into MongoDB """
        new_user = self.collection.insert_one({
            "name": user.name,
            "email": user.email
        })
        return str(new_user.inserted_id)


    def update(self, user):
        """ Update given user in MongoDB """
        update_user = self.collection.update_one(
            { "_id": ObjectId(user.id) },
            {
                "$set": {
                    "name": user.name,
                    "email": user.email
                }
            }
        )
        return update_user.matched_count == 1


    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        delete_filter = { "_id": ObjectId(user_id) }
        delete_user = self.collection.delete_one(delete_filter)
        return delete_user.deleted_count == 1
```