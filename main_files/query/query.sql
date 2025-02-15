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

-- Restaurants tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS restaurants
(
    ID           BIGSERIAL PRIMARY KEY,
    NAME         VARCHAR(255) NOT NULL,
    USERNAME     VARCHAR(255) NOT NULL UNIQUE,
    PASSWORD     VARCHAR(255) NOT NULL,
    ROLE         VARCHAR(255) NOT NULL,
    PHONE_NUMBER BIGINT       NOT NULL UNIQUE,
    COMPANY_FEE  BIGINT       NOT NULL,
    OWNER_ID     VARCHAR(255) NOT NULL REFERENCES users (ID) ON DELETE CASCADE,
    CREATED_AT   TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP,
    IS_LOGIN     BOOLEAN      NULL DEFAULT FALSE
);

-- branch tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS branch
(
    ID            BIGSERIAL PRIMARY KEY,
    NAME          VARCHAR(255) NOT NULL,
    LOCATION      VARCHAR(255) NOT NULL,
    RESTAURANT_ID BIGINT       NOT NULL REFERENCES restaurants (ID) ON DELETE CASCADE,
    PASSWORD      VARCHAR(255) NOT NULL,
    USERNAME      VARCHAR(255) NOT NULL UNIQUE,
    PHONE_NUMBER  BIGINT       NOT NULL UNIQUE,
    ROLE          VARCHAR(255) NOT NULL,
    CREATED_AT    TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP,
    IS_LOGIN      BOOLEAN      NULL DEFAULT FALSE
);

-- product tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS products
(
    ID            BIGSERIAL PRIMARY KEY,
    NAME          VARCHAR(255) NOT NULL,
    PRICE         BIGINT       NOT NULL,
    RESTAURANT_ID BIGINT       NOT NULL REFERENCES restaurants (ID) ON DELETE CASCADE,
    STATUS        BOOLEAN      NOT NULL DEFAULT TRUE,
    CREATED_AT    TIMESTAMP    NULL     DEFAULT CURRENT_TIMESTAMP
);

-- baskets tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS baskets
(
    ID         BIGSERIAL PRIMARY KEY,
    USER_ID    BIGINT       NOT NULL REFERENCES users (ID) ON DELETE CASCADE,
    STATUS     VARCHAR(255) NOT NULL,
    CREATED_AT TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP
);

-- basket_items tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS basket_items
(
    ID         BIGSERIAL PRIMARY KEY,
    BASKET_ID  BIGINT NOT NULL REFERENCES baskets (ID) ON DELETE CASCADE,
    PRODUCT_ID BIGINT NOT NULL REFERENCES products (ID) ON DELETE CASCADE,
    QUANTITY   BIGINT NOT NULL
);

-- orders tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS orders
(
    ID         BIGSERIAL PRIMARY KEY,
    USER_ID    BIGINT       NOT NULL REFERENCES users (ID) ON DELETE CASCADE,
    STATUS     VARCHAR(255) NOT NULL,
    CREATED_AT TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP
);

-- order_items tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS order_items
(
    ID        BIGSERIAL PRIMARY KEY,
    ORDER_ID  BIGINT       NOT NULL REFERENCES orders (ID) ON DELETE CASCADE,
    PRICE     BIGINT       NOT NULL,
    NAME      VARCHAR(255) NOT NULL,
    QUANTITY  BIGINT       NOT NULL,
    BRANCH_ID BIGINT       NOT NULL REFERENCES branch (ID) ON DELETE CASCADE
);

-- requests tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS requests
(
    ID         BIGSERIAL PRIMARY KEY,
    ORDER_ID   BIGINT       NOT NULL REFERENCES orders (ID) ON DELETE CASCADE,
    COURIER_ID BIGINT       NULL REFERENCES USERS (ID) ON DELETE CASCADE DEFAULT NULL,
    STATUS     VARCHAR(255) NOT NULL,
    CREATED_AT TIMESTAMP    NULL                                         DEFAULT CURRENT_TIMESTAMP
);

-- Register bo'lgan userni databasega yozish uchun query
INSERT INTO users(FIRST_NAME, LAST_NAME, username, password, phone_number, ROLE)
VALUES ('', '', '', '', '', '');

-- Admin userlarni parollarini almashtirish uchun query
UPDATE users
SET password='%s'
WHERE id = '%s';

-- Admin tomonidan userlarni uchirish uchun query
DELETE
FROM users
WHERE id = '% s';

-- Yangi restaurant qo'shish uchun query
INSERT INTO restaurants (NAME, USERNAME, PASSWORD, ROLE, PHONE_NUMBER, COMPANY_FEE, OWNER_ID)
VALUES ('%s', ' %s', '%s', '%s', '%s', '%s', '%s');

-- Restaurantni update qilish uchun query
UPDATE restaurants
SET NAME         = '%s',
    USERNAME     = '%s',
    PASSWORD     = '%s',
    ROLE         = '%s',
    PHONE_NUMBER = '%s',
    COMPANY_FEE  = '%s'
WHERE ID = '%s';

-- Qaysidir userni barcha branchlarini topish uchun query
select *
from branch
         inner join restaurants r on branch.RESTAURANT_ID = r.ID
WHERE r.OWNER_ID = '%s';

-- Restaran egasini barcha restaralarini ko'rish uchun query
SELECT *
FROM restaurants
WHERE OWNER_ID = '%s';

-- userni restarlarini tanlash uchun query
SELECT *
FROM restaurants
WHERE OWNER_ID = '% s'
  and ID = '% s';

-- Restaran egasi uzini branchini o'chirish uchun
SELECT *
FROM branch b
         INNER JOIN restaurants r on branch.RESTAURANT_ID = r.ID
WHERE r.owner_id = '% s'
  AND b.id = '% s'