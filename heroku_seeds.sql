DELETE FROM users;
DELETE FROM likes;
DELETE FROM posts;
DELETE FROM comments;

INSERT INTO users (name, username, email, profile_pic_url, bio, hashed_password,)
VALUES
    ('demo user', 'demouser', 'demouser@demouser.com', 'https://i.etsystatic.com/7745761/r/il/eb07f8/1384972180/il_570xN.1384972180_mly2.jpg', 'I am demo', 'pbkdf2:sha256:150000$JywjGg86$c0185e326734cfe06b5202753432121514673e62541029006de4bb1fb3db7704'),
    ('ceejay', 'ceejayduhh', 'ceejayduhh@ceejayduhh.com', 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_2837.JPG', 'It''s ceejay duhh', 'pbkdf2:sha256:150000$hqGtHVmM$1a7905391162a5eaebcf6b0a917c0b8f43826073a24d84d02651799b94813532');

INSERT INTO posts (user_id, post_imgurl, description)
VALUES
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_2210.JPG', 'Disneyland!')
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3468.JPG', 'LV Rug')
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3186.JPG', 'Halloween is around the corner!')
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3474.JPG', 'My team stays clean in SUPREME')


INSERT INTO follows (user_id, follow_user_id)
VALUES
    (1, 2)
    (2, 1)