drop database if exists TRUONGHOC1;

-- Tạo cơ sở dữ liệu TRUONGHOC1
create database TRUONGHOC1;


-- Sử dụng cơ sở dữ liệu TRUONGHOC1
USE TRUONGHOC1;


-- Tạo bảng TRUONG

CREATE TABLE TRUONG (
    MATR CHAR(6) PRIMARY KEY,
    TENTR VARCHAR(50) NOT NULL,
    DCHITR VARCHAR(256) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Tạo clustered index cho bảng TRUONG


-- Tạo bảng HS

CREATE TABLE HS (
    MAHS char(9) PRIMARY KEY,  // HS1000000
    HO VARCHAR(50) NOT NULL,
    TEN VARCHAR(50) NOT NULL,
    CCCD VARCHAR(12),
    NTNS char(2) NOT NULL,
    DCHI_HS VARCHAR(100) NOT NULL,
    CONSTRAINT UQ_HS_CCCD UNIQUE (CCCD)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Tạo clustered index cho bảng HS



-- Tạo bảng HOC
CREATE TABLE HOC (
    MATR char(9),
    MAHS char(9),
    NAMHOC char(9),
    DIEMTB char(2) NOT NULL,
    XEPLOAI varchar(20) NOT NULL,
    KQUA varchar(20) NOT NULL,
    PRIMARY KEY (MATR, MAHS, NAMHOC),
    FOREIGN KEY (MATR) REFERENCES TRUONG (MAmTR),
    FOREIGN KEY (MAHS) REFERENCES HS (MAHS),
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Tạo clustered index cho bảng HOC

