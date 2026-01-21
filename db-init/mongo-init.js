db = db.getSiblingDB("labo01_db");

db.createUser({
    user: "gl-lab01",
    pwd: "labo01",
    roles:[
        {
             role: "readWrite",
             db: "labo01_db",
        },
    ],
});

db.createCollection("users");

db.users.insertMany([
    {name: "Ada Lovelace", email: "alovelace@example.com"},
    {name: "Adele Goldberg", email: "agoldberg@example.com"},
    {name: "Alan Turing", email: "aturing@example.com"}
])