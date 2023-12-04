CREATE TABLE IF NOT EXISTS beer.states(
   id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   created_at TIMESTAMP without TIME ZONE DEFAULT (now() at time zone 'utc'),
   updated_at TIMESTAMP without TIME ZONE DEFAULT (now() at time zone 'utc')
);

SELECT beer.trigger_creation('beer','states','tr_b_states');

INSERT INTO beer.states(name) VALUES ('Alaska') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Alabama') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Arkansas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Arizona') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('California') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Colorado') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Connecticut') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('District of Columbia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Delaware') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Florida') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Georgia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Hawaii') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Iowa') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Idaho') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Illinois') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Indiana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Kansas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Kentucky') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Louisiana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Massachusetts') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Maryland') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Maine') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Michigan') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Minnesota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Missouri') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Mississippi') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Montana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('North Carolina') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('North Dakota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Nebraska') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('New Hampshire') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('New Jersey') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('New Mexico') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Nevada') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('New York') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Ohio') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Oklahoma') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Oregon') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Pennsylvania') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Puerto Rico') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Rhode Island') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('South Carolina') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('South Dakota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Tennessee') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Texas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Utah') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Virginia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Vermont') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Washington') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Wisconsin') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('West Virginia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('Wyoming') ON CONFLICT DO NOTHING;
