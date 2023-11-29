CREATE OR REPLACE FUNCTION beer.trigger_set_timestamp()
      RETURNS TRIGGER
      AS $$
BEGIN
      NEW.updated_at = now() at time zone 'utc';
      RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION beer.trigger_creation(
       schema_n VARCHAR (50),
       table_n VARCHAR (50),
       trigger_n VARCHAR (50)
       )
    RETURNS BOOLEAN
    AS $$
    DECLARE trigger_existence BOOLEAN;
BEGIN
    trigger_existence = (
        SELECT EXISTS(
        SELECT * FROM information_schema.triggers
        WHERE event_object_schema = schema_n
        AND event_object_table = table_n
        AND trigger_name = trigger_n)
        );

    IF trigger_existence
    THEN
	    RAISE NOTICE 'Trigger already exists, skipping';
    ELSE
	    EXECUTE ('CREATE TRIGGER' || ' ' || trigger_n || ' ' ||
        'BEFORE UPDATE ON' || ' ' || schema_n || '.' || table_n || ' '|| 'FOR EACH ROW EXECUTE FUNCTION beer.trigger_set_timestamp()');
    END IF;
    RETURN trigger_existence;
END $$
LANGUAGE plpgsql;
