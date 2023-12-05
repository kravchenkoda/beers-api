CREATE TABLE IF NOT EXISTS beer.states(
   id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   created_at TIMESTAMP without TIME ZONE DEFAULT (now() at time zone 'utc'),
   updated_at TIMESTAMP without TIME ZONE DEFAULT (now() at time zone 'utc')
);

SELECT beer.trigger_creation('beer','states','tr_b_states');

INSERT INTO beer.states(name) VALUES ('alaska') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('alabama') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('arkansas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('arizona') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('california') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('colorado') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('connecticut') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('district of columbia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('delaware') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('florida') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('georgia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('hawaii') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('iowa') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('idaho') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('illinois') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('indiana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('kansas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('kentucky') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('louisiana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('massachusetts') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('maryland') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('maine') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('michigan') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('minnesota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('missouri') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('mississippi') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('montana') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('north carolina') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('north dakota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('nebraska') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('new hampshire') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('new jersey') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('new mexico') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('nevada') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('new york') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('ohio') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('oklahoma') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('oregon') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('pennsylvania') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('puerto rico') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('rhode island') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('south carolina') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('south dakota') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('tennessee') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('texas') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('utah') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('virginia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('vermont') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('washington') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('wisconsin') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('west virginia') ON CONFLICT DO NOTHING;
INSERT INTO beer.states(name) VALUES ('wyoming') ON CONFLICT DO NOTHING;
