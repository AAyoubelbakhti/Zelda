use ZeldaSQL;

-- Usuarios
ALTER TABLE Users
ADD PRIMARY KEY (user_id),
ADD CONSTRAINT username_unique UNIQUE (username),
MODIFY COLUMN user_id INT AUTO_INCREMENT,
MODIFY COLUMN username VARCHAR(50) NOT NULL,
MODIFY COLUMN created_at DATETIME NOT NULL,
MODIFY COLUMN modified_at DATETIME NOT NULL;

-- Partidas
ALTER TABLE Games
ADD PRIMARY KEY (game_id),
ADD CONSTRAINT fk_user_games FOREIGN KEY (user_id) REFERENCES Users(user_id),
MODIFY COLUMN game_id INT AUTO_INCREMENT,
MODIFY COLUMN date_started DATETIME NOT NULL,
MODIFY COLUMN hearts_remaining INT NOT NULL,
MODIFY COLUMN blood_moon_countdown INT NOT NULL,
MODIFY COLUMN blood_moon_appearances INT NOT NULL,
MODIFY COLUMN region VARCHAR(20) NOT NULL,
MODIFY COLUMN created_at DATETIME NOT NULL,
MODIFY COLUMN modified_at DATETIME NOT NULL;

-- Armas
ALTER TABLE Weapons
ADD PRIMARY KEY (weapon_id),
MODIFY COLUMN weapon_id INT AUTO_INCREMENT,
MODIFY COLUMN weapon_name VARCHAR(15) NOT NULL;

-- Comidas
ALTER TABLE Foods
ADD PRIMARY KEY (food_id),
MODIFY COLUMN food_id INT AUTO_INCREMENT,
MODIFY COLUMN food_name VARCHAR(15) NOT NULL;

-- Enemigos
ALTER TABLE Enemies
ADD PRIMARY KEY (enemy_id),
ADD CONSTRAINT fk_game_enemies FOREIGN KEY (game_id) REFERENCES Games(game_id),
MODIFY COLUMN enemy_id INT AUTO_INCREMENT,
MODIFY COLUMN region VARCHAR(20) NOT NULL,
MODIFY COLUMN num INT NOT NULL,
MODIFY COLUMN xpos INT NOT NULL,
MODIFY COLUMN ypos INT NOT NULL,
MODIFY COLUMN lifes_remaining INT NOT NULL;

-- Santuarios
ALTER TABLE Sanctuaries
ADD PRIMARY KEY (sanctuary_id),
ADD CONSTRAINT fk_game_sanctuaries FOREIGN KEY (game_id) REFERENCES Games(game_id),
MODIFY COLUMN sanctuary_id INT AUTO_INCREMENT,
MODIFY COLUMN region VARCHAR(20) NOT NULL,
MODIFY COLUMN num INT NOT NULL,
MODIFY COLUMN xpos INT NOT NULL,
MODIFY COLUMN ypos INT NOT NULL;

-- Cofres
ALTER TABLE Chests
ADD PRIMARY KEY (chest_id),
ADD CONSTRAINT fk_game_chests FOREIGN KEY (game_id) REFERENCES Games(game_id),
MODIFY COLUMN chest_id INT AUTO_INCREMENT,
MODIFY COLUMN region VARCHAR(20) NOT NULL,
MODIFY COLUMN num INT NOT NULL,
MODIFY COLUMN xpos INT NOT NULL,
MODIFY COLUMN ypos INT NOT NULL;

-- Armas utilizadas por usuarios
ALTER TABLE WeaponsUsed
ADD CONSTRAINT fk_user_weaponsused_user FOREIGN KEY (user_id) REFERENCES Users(user_id),
ADD CONSTRAINT fk_weapon_weaponsused_weapon FOREIGN KEY (weapon_id) REFERENCES Weapons(weapon_id),
ADD CONSTRAINT fk_game_weaponsused_game FOREIGN KEY (game_id) REFERENCES Games(game_id),
MODIFY COLUMN lives_remaining INT NOT NULL;

-- Comidas consumidas por usuarios
ALTER TABLE FoodsConsumed
ADD CONSTRAINT fk_user_foodsconsumed_user FOREIGN KEY (user_id) REFERENCES Users(user_id),
ADD CONSTRAINT fk_food_foodsconsumed_food FOREIGN KEY (food_id) REFERENCES Foods(food_id),
ADD CONSTRAINT fk_game_foodsconsumed_game FOREIGN KEY (game_id) REFERENCES Games(game_id),
MODIFY COLUMN quantity_remaining INT NOT NULL;
