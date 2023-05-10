
----------------------------------------------------------------------
-----------------------------TABLES-----------------------------------
----------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS "events" (
    "id" INTEGER,
    "name" TEXT,
    "date" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "location" TEXT NOT NULL,
    "passed" INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "users" (
    "id" INTEGER,
    "firstname" TEXT NOT NULL,
    "lastname" TEXT NOT NULL,
    "email" TEXT NOT NULL UNIQUE,
    "birthdate" INTEGER NOT NULL, 
    PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "enrolled" (
    "event_id" INTEGER,
    "user_id" INTEGER,
    FOREIGN KEY("event_id") REFERENCES "events"("id"),
    FOREIGN KEY("user_id") REFERENCES "users"("id")
);

----------------------------------------------------------------------
-----------------------------VIEWS------------------------------------
----------------------------------------------------------------------
-- Create a view upcoming events
CREATE VIEW IF NOT EXISTS "upcoming_events" AS 
SELECT "id", "name", "date", "location"
FROM "events"
WHERE "passed" = 0;

-- Create a view passed events
CREATE VIEW IF NOT EXISTS "passed_events" AS 
SELECT "id", "name", "date", "location"
FROM "events"
WHERE "passed" = 1;

-- Create a view for enrolled users
CREATE VIEW IF NOT EXISTS "enrolled_users" AS
SELECT "firstname","lastname", "name" AS "event" FROM "users"
JOIN "enrolled" ON "users"."id" = "enrolled"."user_id"
JOIN "events" ON "events"."id" = "enrolled"."event_id";

-- Create a view for how many are attending each event
CREATE VIEW IF NOT EXISTS "attending" AS
SELECT "name" AS "event", COUNT("users"."id") AS "attending" FROM "users"
JOIN "enrolled" ON "enrolled"."user_id" = "users"."id"
JOIN "events" ON "events"."id" = "enrolled"."event_id"
GROUP BY "name";

-- Create a view to display users current age
CREATE VIEW IF NOT EXISTS "user_ages" AS
SELECT "id", "firstname", "lastname", "email",
    strftime('%Y', 'now') - strftime('%Y', birthdate)
    - (strftime('%m-%d', 'now') < strftime('%m-%d', birthdate))
    AS "age"
FROM users
GROUP BY "id";
