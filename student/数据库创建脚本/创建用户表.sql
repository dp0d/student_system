-- 创建用户表
CREATE TABLE users (
    user_id INT AUTO_INCREMENT COMMENT '用户ID，主键自增',
    username VARCHAR(50) NOT NULL COMMENT '用户名（登录账号）',
    password VARCHAR(255) NOT NULL COMMENT '密码（建议存储加密后的值）',
    nickname VARCHAR(50) COMMENT '用户昵称（显示名称）',
    user_role TINYINT NOT NULL COMMENT '用户角色（1:管理员 2:教师）',
    class_id INT COMMENT '所属班级ID（仅教师角色需要）',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (user_id),
    UNIQUE KEY uk_username (username) COMMENT '用户名唯一约束',
    INDEX idx_user_role (user_role) COMMENT '角色索引',
    INDEX idx_class_id (class_id) COMMENT '班级ID索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户信息表';

-- 示例数据
INSERT INTO users (username, password, nickname, user_role, class_id) VALUES
    ('admin', '$2a$10$xJwL5vW5zW5zW5zW5zW5zO', '系统管理员', 1, NULL),
    ('teacher01', '$2a$10$xJwL5vW5zW5zW5zW5zW5zO', '张老师', 2, 1),
    ('teacher02', '$2a$10$xJwL5vW5zW5zW5zW5zW5zO', '李老师', 2, 2),
    ('teacher03', '$2a$10$xJwL5vW5zW5zW5zW5zW5zO', '王老师', 2, 3);