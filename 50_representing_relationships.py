# BASIC DATABASE NORMALIZATION TIPS

# Don't replicate data - reference (point at) data
# Use integers for keys and references
# Add a special "key" column to each table (commnoly named id)

# KEYS

# Primary Key - generally an integer auto-increment field
# Logical Key - what the outside world uses for lookup
# Foregin Key - typically an integer key pointing to a row in another table

# Don't use a logical key as the primary (e.g. name or email - they can change)
# Relationships based on matching string fields are less efficient than integers
