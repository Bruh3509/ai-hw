CREATE TABLE users (
                       id BIGSERIAL PRIMARY KEY,
                       name VARCHAR(255),
                       username VARCHAR(255) UNIQUE,
                       email VARCHAR(255) UNIQUE,
                       phone VARCHAR(255),
                       website VARCHAR(255),
                       address_street VARCHAR(255),
                       address_suite VARCHAR(255),
                       address_city VARCHAR(255),
                       address_zipcode VARCHAR(255),
                       address_geo_lat VARCHAR(255),
                       address_geo_lng VARCHAR(255),
                       company_name VARCHAR(255),
                       company_catch_phrase TEXT,
                       company_bs TEXT
);

CREATE TABLE auth_users (
                            id BIGSERIAL PRIMARY KEY,
                            name VARCHAR(255),
                            email VARCHAR(255) NOT NULL UNIQUE,
                            password_hash VARCHAR(255) NOT NULL
);
