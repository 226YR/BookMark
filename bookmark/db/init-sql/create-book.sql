-- テーブル作成
CREATE TABLE IF NOT EXISTS Book (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),--ID
    title VARCHAR(200) NOT NULL,--タイトル
    author VARCHAR(100) NOT NULL,--著者
    impression TEXT NOT NULL,--感想
    favorite_flag BOOLEAN DEFAULT FALSE,--お気に入りフラグ
    reading_time_minutes INT DEFAULT 0,--読書時間（分）
    reading_status VARCHAR(50) CHECK (reading_status IN ('未読', '読んでいる途中', '読了')) DEFAULT '未読',--読書状況
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,--作成日時
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP--更新日時
);

-- ダミーデータ挿入
INSERT INTO Book (id, title, author, impression, favorite_flag, reading_time_minutes, reading_status, created_at, updated_at) VALUES
    ('3b4b60c6-3a90-48c9-b8ed-4df5d1231231', 'コンビニ人間', '村田沙耶香', '社会の中で「普通」とされる生き方への鋭い洞察が魅力的な作品でした。', TRUE, 240, '読了', '2025-01-08 14:20:47.397887', '2025-01-08 14:20:47.397887'),
    ('4a2b8e87-2c34-490e-80f7-123b456c7890', '君たちはどう生きるか', '吉野源三郎', '道徳や哲学的なテーマに深く考えさせられる一冊でした。', FALSE, 180, '読了', '2025-01-08 15:41:24.679379', '2025-01-08 15:41:24.679379'),
    ('d5f3ac91-9f64-4b82-b27a-c7d1b3cd5678', '嫌われる勇気', '岸見一郎・古賀史健', 'アドラー心理学の入門書として非常に分かりやすかったです。', TRUE, 200, '読んでいる途中', '2025-01-08 16:41:34.872312', '2025-01-08 16:41:34.872312'),
    ('6f894bd3-c987-485c-933a-a45b9c123456', 'ノルウェイの森', '村上春樹', '恋愛と喪失がテーマの作品で心に残るストーリーでした。', FALSE, 300, '未読', '2025-01-08 17:41:57.507', '2025-01-08 17:41:57.507');
