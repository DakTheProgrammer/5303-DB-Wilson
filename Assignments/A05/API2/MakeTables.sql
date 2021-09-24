CREATE TABLE Movies (
    t_id VARCHAR(10),
    title VARCHAR(100),
    PRIMARY KEY (t_id)
);

CREATE TABLE AboutMovies (
    t_id VARCHAR(10),
    is_adult BOOLEAN,
    runtime VARCHAR(5),
    genre TEXT(1000),
    year INT(4),
    PRIMARY KEY (t_id)
);

CREATE TABLE FilmMakers (
    name_id VARCHAR(10),
    name_real VARCHAR(100),
    birth_year INT(4),
    death_year INT(4),
    profesions VARCHAR(255),
    known_for VARCHAR(255),
    PRIMARY KEY (name_id)
);

CREATE TABLE Directors (
    t_id VARCHAR(10),
    directors TEXT(1000),
    PRIMARY KEY (t_id)
);

CREATE TABLE Writers (
    t_id VARCHAR(10),
    writers TEXT(1000),
    PRIMARY KEY (t_id)
);

CREATE TABLE Rating (
    t_id VARCHAR(10),
    avg_rating DECIMAL(65,1),
    num_votes INT(10),
    PRIMARY KEY (t_id)
);

CREATE TABLE MovieCrew (
    t_id VARCHAR(10),
    name_id VARCHAR(10),
    ordering int(5),
    catigory VARCHAR(100),
    characters TEXT(1000),
    PRIMARY KEY (t_id)
);