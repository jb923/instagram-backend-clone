DELETE FROM users;
DELETE FROM likes;
DELETE FROM posts;
DELETE FROM comments;

INSERT INTO users (name, username, email, profile_imgurl, bio, hashed_password)
VALUES
    ('demo user', 'demouser', 'demouser@demouser.com', 'https://i.etsystatic.com/7745761/r/il/eb07f8/1384972180/il_570xN.1384972180_mly2.jpg', 'Flexagram a place where you can enjoy moments with friends', 'pbkdf2:sha256:150000$JywjGg86$c0185e326734cfe06b5202753432121514673e62541029006de4bb1fb3db7704'),
    ('ceejay', 'ceejayduhh', 'ceejayduhh@ceejayduhh.com', 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/ktg.png', 'It''s ceejay duhh', 'pbkdf2:sha256:150000$hqGtHVmM$1a7905391162a5eaebcf6b0a917c0b8f43826073a24d84d02651799b94813532'),
    ('143', '143', '143@143.com', 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/143.jpeg', 'I love you', 'pbkdf2:sha256:150000$ehv1bynQ$abda7ed1e64b7d393fc366eac311b980504e0ff663d98cd06f6b293499e014bd'),
    ('Drake', 'Drake', 'drake@drake.com', 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/drake-laugh-now-cry-later.jpg', 'Laugh Now Cry Later', 'pbkdf2:sha256:150000$7V38UgLl$a2db106c0f93d5a67fece8ee4d22a2259d836d67cd7428e9c3a1d164eb9c2f8a'),
    ('johnny', 'johnny', 'johnny@johnny.com', 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/favicon.ico', 'Hi, it''s ya boy johnny', 'pbkdf2:sha256:150000$fYQkEBfV$88e6f34385035432aacd4093c85f7e2b0c01e01142c02708b86b14219be8834f');

INSERT INTO posts (user_id, post_imgurl, description)
VALUES
    (3, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3468.JPG', 'LV Rug'),
    (5, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/xupreme-app2.jpg', 'Checkout my Xupreme app on https://xupreme.herokuapp.com/!'),
    (2, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3474.JPG', 'My team stays clean in SUPREME'),
    (4, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/drake-nike2.jpg', 'When you trynna catch you''re girl on a lie'),
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3186.JPG', 'Halloween is around the corner!'),
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_2210.JPG', 'Disneyland!');


INSERT INTO follows (user_id, follow_user_id)
VALUES
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (5, 1),
    (4, 1),
    (3, 1),
    (2, 1),
    (1, 1),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (4, 4),
    (4, 5),
    (5, 5);

 
