# DATABASE DESIGN

# Starts with an Entity Relationship Diagram (ERD) that shows the different tables and the relationships between them.

# Basic simplified normalization rule: DON'T put the same string data more than once - use a relationship instead.
# When there is one thing IRL, there should be one representation of that thing in the database

# Start with the most central entity for the application and build a mock table with all it's attributes of interest.
# The columns with duplicate values may be better stored as a table of their own, with relationships to the first entity.