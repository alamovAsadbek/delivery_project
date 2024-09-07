-- users tableni yasab olish uchun query
CREATE TABLE IF NOT EXISTS users
(
    ID
                 BIGSERIAL
        PRIMARY
            KEY,
    FIRST_NAME
                 VARCHAR(255)        NOT NULL,
    LAST_NAME    VARCHAR(255)        NOT NULL,
    username     VARCHAR(255) UNIQUE NOT NULL,
    password     VARCHAR(255)        NOT NULL,
    phone_number BIGINT UNIQUE       NOT NULL,
    ROLE         VARCHAR(255)        NOT NULL,
    IS_LOGIN     BOOLEAN             NOT NULL DEFAULT FALSE,
    CREATED_AT   TIMESTAMP           NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Dastur birinchi marta ishlagan payt hamma userlarni is_loginni false qilish uchun yani logoout
UPDATE users
SET IS_LOGIN= FALSE;
