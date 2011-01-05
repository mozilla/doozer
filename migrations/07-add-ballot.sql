BEGIN;CREATE TABLE `vote_ballot` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `creator_id` integer NOT NULL,
    `games` longtext NOT NULL
)
;
ALTER TABLE `vote_ballot` ADD CONSTRAINT `creator_id_refs_id_23f756ca` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`);
CREATE TABLE `vote_vote` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `creator_id` integer NOT NULL,
    `game_id` integer NOT NULL,
    `score` smallint NOT NULL
)
;
ALTER TABLE `vote_vote` ADD CONSTRAINT `game_id_refs_id_9fe09d1` FOREIGN KEY (`game_id`) REFERENCES `games_game` (`id`);
ALTER TABLE `vote_vote` ADD CONSTRAINT `creator_id_refs_id_4175b566` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`);
CREATE INDEX `vote_ballot_685aee7` ON `vote_ballot` (`creator_id`);
CREATE INDEX `vote_vote_685aee7` ON `vote_vote` (`creator_id`);
CREATE INDEX `vote_vote_7b333d1e` ON `vote_vote` (`game_id`);COMMIT;
