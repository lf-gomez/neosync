-- Create schemas
CREATE SCHEMA IF NOT EXISTS app_data;

-- Set search path
SET search_path TO app_data, public;

-- Create user roles table
CREATE TABLE app_data.roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create users table
CREATE TABLE app_data.users (
    user_id SERIAL PRIMARY KEY,
    role_id INTEGER REFERENCES app_data.roles(role_id) ON DELETE SET NULL,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create products table
CREATE TABLE app_data.products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    stock_quantity INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    category VARCHAR(50),
    is_available BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create orders table
CREATE TABLE app_data.orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES app_data.users(user_id) ON DELETE CASCADE,
    order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(12, 2) NOT NULL DEFAULT 0.00,
    shipping_address TEXT,
    tracking_number VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create order_items table for order-product relationship
CREATE TABLE app_data.order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES app_data.orders(order_id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES app_data.products(product_id) ON DELETE RESTRICT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0),
    subtotal DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * unit_price) STORED,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(order_id, product_id)
);

-- Create product_reviews table
CREATE TABLE app_data.product_reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL REFERENCES app_data.products(product_id) ON DELETE CASCADE,
    user_id INTEGER NOT NULL REFERENCES app_data.users(user_id) ON DELETE CASCADE,
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(product_id, user_id)
);

-- Create function to update timestamp
CREATE OR REPLACE FUNCTION update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers for updated_at columns
CREATE TRIGGER update_roles_timestamp BEFORE UPDATE ON app_data.roles
    FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_users_timestamp BEFORE UPDATE ON app_data.users
    FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_products_timestamp BEFORE UPDATE ON app_data.products
    FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_orders_timestamp BEFORE UPDATE ON app_data.orders
    FOR EACH ROW EXECUTE FUNCTION update_timestamp();

CREATE TRIGGER update_product_reviews_timestamp BEFORE UPDATE ON app_data.product_reviews
    FOR EACH ROW EXECUTE FUNCTION update_timestamp();

-- Insert some initial roles
INSERT INTO app_data.roles (role_name, description) VALUES 
    ('admin', 'Administrator with full access'),
    ('customer', 'Standard customer account'),
    ('staff', 'Staff member with limited admin privileges');

-- Create indexes for performance
CREATE INDEX idx_users_role_id ON app_data.users(role_id);
CREATE INDEX idx_orders_user_id ON app_data.orders(user_id);
CREATE INDEX idx_order_items_order_id ON app_data.order_items(order_id);
CREATE INDEX idx_order_items_product_id ON app_data.order_items(product_id);
CREATE INDEX idx_product_reviews_product_id ON app_data.product_reviews(product_id);
CREATE INDEX idx_product_reviews_user_id ON app_data.product_reviews(user_id);

-- Create view for order summaries
CREATE VIEW app_data.order_summaries AS
SELECT 
    o.order_id,
    o.user_id,
    u.username,
    o.order_date,
    o.status,
    o.total_amount,
    COUNT(oi.order_item_id) AS total_items
FROM 
    app_data.orders o
    JOIN app_data.users u ON o.user_id = u.user_id
    JOIN app_data.order_items oi ON o.order_id = oi.order_id
GROUP BY 
    o.order_id, u.username;

-- Create view for product ratings
CREATE VIEW app_data.product_ratings AS
SELECT 
    p.product_id,
    p.name,
    AVG(pr.rating) AS average_rating,
    COUNT(pr.review_id) AS review_count
FROM 
    app_data.products p
    LEFT JOIN app_data.product_reviews pr ON p.product_id = pr.product_id
GROUP BY 
    p.product_id, p.name;
