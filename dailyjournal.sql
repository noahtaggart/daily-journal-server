CREATE TABLE `Entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `journalEntry` TEXT NOT NULL,
    `date` INTEGER NOT NULL,
    `userId` INTEGER NOT NULL,
    `moodId` INTEGER NOT NULL,
    FOREIGN KEY(`userId`) REFERENCES `Users`(`id`),
    FOREIGN KEY(`moodId`) REFERENCES `Moods`(`id`)

);

CREATE TABLE `Users` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `username` TEXT NOT NULL
);

CREATE TABLE `Moods` (
`id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
`name`  TEXT NOT NULL
);

INSERT INTO `Entries` VALUES (null, "Ate some ice cream today", 04112022, 1, 2);
INSERT INTO `Entries` VALUES (null, "Reorganized bed room. Bought new vacuum after last one exploded", 04102022, 2, 3);
INSERT INTO `Entries` VALUES (null, "Got headshots taken and got some dope bibimbap", 04092022, 3, 1);
INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Content");


SELECT *
FROM Entries e
WHERE e.journalEntry LIKE "%ate%" 

SELECT *
FROM Entries e
WHERE e.journalEntry CONTAINS "ate"

   SELECT
            e.id,
            e.journalEntry,
            e.date,
            e.userId,
            e.moodId,
            m.name mood
        FROM Entries e
        Join Moods m
            ON m.id = e.moodId