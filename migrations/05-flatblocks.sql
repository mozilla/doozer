BEGIN;
CREATE TABLE `flatblocks_flatblock` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `slug` varchar(255) NOT NULL UNIQUE,
    `header` varchar(255),
    `content` longtext
)
;
COMMIT;
