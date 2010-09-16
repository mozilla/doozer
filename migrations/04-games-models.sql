BEGIN;
CREATE TABLE `games_game` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `updated` datetime NOT NULL,
    `creator_id` integer NOT NULL,
    `name` varchar(255) NOT NULL,
    `slug` varchar(50) NOT NULL,
    `description` longtext NOT NULL,
    `url` varchar(200) NOT NULL,
    `source` varchar(200),
    `resources` longtext,
    `is_approved` bool,
    `reviewed_by_id` integer
)
;
ALTER TABLE `games_game` ADD CONSTRAINT `creator_id_refs_id_6e7b32a8` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `games_game` ADD CONSTRAINT `reviewed_by_id_refs_id_6e7b32a8` FOREIGN KEY (`reviewed_by_id`) REFERENCES `auth_user` (`id`);
CREATE TABLE `games_screenshot` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `created` datetime NOT NULL,
    `updated` datetime NOT NULL,
    `game_id` integer NOT NULL,
    `file` varchar(100) NOT NULL
)
;
ALTER TABLE `games_screenshot` ADD CONSTRAINT `game_id_refs_id_5e86c673` FOREIGN KEY (`game_id`) REFERENCES `games_game` (`id`);
CREATE INDEX `games_game_3216ff68` ON `games_game` (`created`);
CREATE INDEX `games_game_8aac229` ON `games_game` (`updated`);
CREATE INDEX `games_game_685aee7` ON `games_game` (`creator_id`);
CREATE INDEX `games_game_56ae2a2a` ON `games_game` (`slug`);
CREATE INDEX `games_game_3e1cf92e` ON `games_game` (`is_approved`);
CREATE INDEX `games_game_362d9b12` ON `games_game` (`reviewed_by_id`);
CREATE INDEX `games_screenshot_3216ff68` ON `games_screenshot` (`created`);
CREATE INDEX `games_screenshot_8aac229` ON `games_screenshot` (`updated`);
CREATE INDEX `games_screenshot_7b333d1e` ON `games_screenshot` (`game_id`);
COMMIT;
