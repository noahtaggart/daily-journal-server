CREATE TABLE `Entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `date` TEXT NOT NULL,
    `moodId` INTEGER NOT NULL,
    FOREIGN KEY(`moodId`) REFERENCES `Moods`(`id`)

);

CREATE TABLE `Moods` (
`id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
`label`  TEXT NOT NULL
);
CREATE TABLE `Tags` (
`id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
`name`  TEXT NOT NULL
);
CREATE TABLE `Entrytags` (
`id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
`entry_id`  INTEGER NOT NULL,
`tag_id`  INTEGER NOT NULL,
FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`)
FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

INSERT INTO `Entries` VALUES (null, "Javascript", "I learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.\nI learned about loops today. They can be a lot of fun.", "Wed Sep 15 2021 10:10:47 ", 1);
INSERT INTO `Entries` VALUES (null, "Python", "Python is named after the Monty Python comedy group from the UK. I'm sad because I thought it was named after the snake", "Wed Sep 15 2021 10:11:33 ", 4);
INSERT INTO `Entries` VALUES (null, "Python", "Why did it take so long for python to have a switch statement? It's much cleaner than if/elif blocks", "Wed Sep 15 2021 10:13:11 ", 3);
INSERT INTO `Entries` VALUES (null, "Javascript", "Dealing with Date is terrible. Why do you have to add an entire package just to format a date. It makes no sense.", "Wed Sep 15 2021 10:14:05 ", 4);

INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Angry");
INSERT INTO `Moods` VALUES (null, "Ok");
INSERT INTO `Tags` VALUES (null, "tag1");
INSERT INTO `Tags` VALUES (null, "tag2");
INSERT INTO `Tags` VALUES (null, "tag3");
INSERT INTO `Tags` VALUES (null, "tag4");


SELECT *
FROM Entries e
WHERE e.entry LIKE "%ate%" 

SELECT *
FROM Entries e
WHERE e.entry CONTAINS "ate"

SELECT
    e.id,
    e.concept,
    e.entry,
    e.date,
    m.label mood
FROM Entries e
Join Moods m
    ON m.id = e.moodId