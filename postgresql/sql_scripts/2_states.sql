CREATE TABLE IF NOT EXISTS beer.states(
   id   INTEGER NOT NULL PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   created_at TIMESTAMP without TIME ZONE DEFAULT (now() at time zone 'utc'),
   updated_at TIMESTAMP without TIME ZONE DEFAULT (now() at time zone 'utc')
);
    SELECT beer.trigger_creation('beer','states','tr_b_states');
INSERT INTO beer.states(id,name) VALUES (1,'Alaska') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (2,'Alabama') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (3,'Arkansas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (4,'Arizona') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (5,'California') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (6,'Colorado') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (7,'Connecticut') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (8,'District of Columbia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (9,'Delaware') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (10,'Florida') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (11,'Georgia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (12,'Hawaii') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (13,'Iowa') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (14,'Idaho') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (15,'Illinois') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (16,'Indiana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (17,'Kansas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (18,'Kentucky') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (19,'Louisiana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (20,'Massachusetts') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (21,'Maryland') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (22,'Maine') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (23,'Michigan') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (24,'Minnesota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (25,'Missouri') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (26,'Mississippi') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (27,'Montana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (28,'North Carolina') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (29,'North Dakota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (30,'Nebraska') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (31,'New Hampshire') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (32,'New Jersey') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (33,'New Mexico') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (34,'Nevada') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (35,'New York') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (36,'Ohio') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (37,'Oklahoma') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (38,'Oregon') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (39,'Pennsylvania') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (40,'Puerto Rico') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (41,'Rhode Island') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (42,'South Carolina') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (43,'South Dakota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (44,'Tennessee') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (45,'Texas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (46,'Utah') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (47,'Virginia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (48,'Vermont') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (49,'Washington') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (50,'Wisconsin') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (51,'West Virginia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(id,name) VALUES (52,'Wyoming') ON CONFLICT DO NOTHING;
