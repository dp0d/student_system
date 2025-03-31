-- 创建学生表
CREATE TABLE students (
    student_id INT AUTO_INCREMENT COMMENT '学生ID，主键自增',
    student_number VARCHAR(20) NOT NULL COMMENT '学号（业务唯一标识）',
    student_name VARCHAR(50) NOT NULL COMMENT '学生姓名',
    gender TINYINT NOT NULL COMMENT '性别（1:男 2:女）',
    class_id INT NOT NULL COMMENT '所属班级ID',
    math_score DECIMAL(5,2) UNSIGNED DEFAULT 0 COMMENT '数学成绩(0-100)',
    english_score DECIMAL(5,2) UNSIGNED DEFAULT 0 COMMENT '英语成绩(0-100)',
    chinese_score DECIMAL(5,2) UNSIGNED DEFAULT 0 COMMENT '语文成绩(0-100)',
    PRIMARY KEY (student_id),
    UNIQUE KEY uk_student_number (student_number) COMMENT '学号唯一约束',
    INDEX idx_class_id (class_id) COMMENT '班级ID索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='学生信息表';

-- 更新示例数据（不带出生日期）
INSERT INTO students (student_number, student_name, gender, class_id, math_score, english_score, chinese_score) VALUES
    ('20230001', '张三', 1, 1, 85.5, 92.0, 88.0),
    ('20230002', '李四', 2, 1, 90.0, 88.5, 92.5),
    ('20230003', '王五', 1, 2, 76.0, 82.5, 85.0),
    ('20230004', '赵六', 2, 3, 95.5, 89.0, 91.0);