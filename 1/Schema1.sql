drop database if exists TRUONGHOC1;

-- tao csdl TRUONGHOC1
create database TRUONGHOC1;


--  dung csdl TRUONGHOC1
USE TRUONGHOC1;


-- tao bang TRUONG
drop table if exists truong;
CREATE TABLE TRUONG (
    MATR CHAR(3) PRIMARY KEY,

    TENTR VARCHAR(128) NOT NULL,
    DCHITR VARCHAR(256) default NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- tao bang HS
drop tables if exists hs;
CREATE TABLE HS (
    MAHS char(9) PRIMARY KEY,  
    HO VARCHAR(64) NOT NULL,
    TEN VARCHAR(128) NOT NULL,
    CCCD VARCHAR(12),
    NTNS varchar(12) NOT NULL,
    DCHI_HS VARCHAR(256) NOT NULL,
    CONSTRAINT UQ_HS_CCCD UNIQUE (CCCD)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




drop table if exists hoc;
-- tao bang hoc
CREATE TABLE HOC (
    MATR char(3),
    MAHS char(9),
    NAMHOC char(9),
    DIEMTB char(4) NOT NULL,
    XEPLOAI varchar(32) NOT NULL,
    KQUA varchar(32) NOT NULL,
    PRIMARY KEY (MATR, MAHS, NAMHOC),
    FOREIGN KEY (MATR) REFERENCES TRUONG (MATR),
    FOREIGN KEY (MAHS) REFERENCES HS (MAHS)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


