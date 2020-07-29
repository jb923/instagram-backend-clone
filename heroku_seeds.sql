DELETE FROM users;
DELETE FROM likes;
DELETE FROM posts;
DELETE FROM comments;

INSERT INTO users (full_name, username, email, hashed_password, profileimgurl, bio)
VALUES
    ('demo user', 'demouser', 'demouser@demouser.com', 'pbkdf2:sha256:150000$Kae4NpQC$0f5d41ceda81c71f16e5c4f7c5651b12e3bb9aa631ff9c2c9a979a6781b7fe7f', 'https://i.etsystatic.com/7745761/r/il/eb07f8/1384972180/il_570xN.1384972180_mly2.jpg', 'I am demo');


INSERT INTO posts (user_id, imgurl, description)
VALUES
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_2210.JPG', 'Disneyland!')
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3468.JPG', 'LV Rug')
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3186.JPG', 'Halloween is around the corner!')
    (1, 'https://appacademy-instagram-clone.s3-us-west-1.amazonaws.com/IMG_3474.JPG', 'My team stays clean in SUPREME')


INSERT INTO comments (user_id, post_id, content)
VALUES 
    (1, 1, 'Amazing!')
    (1, 2, 'I need this!')
    (1, 3, 'Pumpkins!')
    (1, 4, 'Drippppp')

INSERT INTO likes (user_id, liked)
VALUES
    (1, True)