"""creating tables for the database"""
users_table = """CREATE TABLE IF NOT EXISTS users
            (
                user_id SERIAL PRIMARY KEY, 
                name VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL UNIQUE,
                phone VARCHAR (300) NOT NULL,
                registered TIMESTAMP DEFAULT NOW(),
                message VARCHAR(200) NOT NULL
                
        )"""



queries = [users_table]
droppings = [
                "DROP TABLE users CASCADE",
                
            ]