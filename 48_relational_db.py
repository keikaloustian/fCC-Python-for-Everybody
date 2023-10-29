# MAKE A RELATIONAL DATABASE WITH SQLITE

# In SQLite, semicolons are statement separators and not terminators.
# Therefore, they are only required when executing multiple statements in one go. Optional when executing individual commands.

'''
CREATE TABLE "Users" ("name" TEXT, "email" TEXT)

INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu');
INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu');

DELETE FROM Users WHERE email='ted@umich.edu'

UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

SELECT * FROM Users WHERE email='cvl@umich.edu'

SELECT * FROM Users ORDER BY email
'''