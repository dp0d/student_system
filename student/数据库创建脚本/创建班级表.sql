-- 创建班级表
CREATE TABLE classes (
    class_id INT AUTO_INCREMENT COMMENT '班级ID，主键自增',
    class_name VARCHAR(50) NOT NULL COMMENT '班级名称',
    PRIMARY KEY (class_id),
    UNIQUE KEY uk_class_name (class_name) COMMENT '班级名称唯一索引'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='班级信息表';

-- 添加示例数据
INSERT INTO classes (class_name) VALUES 
    ('计算机科学与技术1班'),
    ('软件工程2班'),
    ('人工智能3班');