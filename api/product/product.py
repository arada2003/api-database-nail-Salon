from fastapi import HTTPException,APIRouter
from database.query import query_get, query_create, query_update

from .models import ProductModel, ProductModel2

def get_all_product():
    products = query_get("""
        SELECT  
            *
        FROM Nail_Patterns
        """, ())
    return products

def get_product_by_id(pattern_id: str):
    product = query_get("""
        SELECT
        *
        FROM Nail_Patterns
        WHERE pattern_id = %s
        """, (pattern_id))
    return product

def add_product(product: ProductModel):
    last_row_id = query_create("""
                INSERT INTO Nail_Patterns (
                    pattern_id,
                    pattern_Name,
                    pattern_Price
                ) VALUES (%s, %s, %s)
                """,
                (
                    product.pattern_id,
                    product.pattern_Name,
                    product.pattern_Price
                )
                )
    return last_row_id

def update_product(pattern_id: str,product: ProductModel):
    is_update = query_update("""
            UPDATE Nail_Patterns
                SET pattern_Name = %s,
                pattern_Price = %s
                WHERE pattern_id = %s;
            """,
            (
                product.pattern_Name,
                product.pattern_Price,
                pattern_id
            )
            )
    if is_update:
        product_update_data = product.dict()
        product_update_data.update({"pattern_id": pattern_id})
        return product_update_data
    else:
        return None
    
def delete_product(pattern_id: str):
    is_deleted = query_update("""
        DELETE FROM Nail_Patterns
        WHERE pattern_id = %s;
        """,
        (pattern_id,)
        )
    return is_deleted


def get_all_product2():
    products = query_get("""
        SELECT  
            *
        FROM Materials
        """, ())
    return products

def get_product_by_id2(spare_id: str):
    product = query_get("""
        SELECT
        *
        FROM Materials
        WHERE spare_id = %s
        """, (spare_id))
    return product

def add_product2(product: ProductModel):
    last_row_id = query_create("""
                INSERT INTO Materials (
                    spare_id,
                    spare_name,
                    spare_Price
                ) VALUES (%s, %s, %s)
                """,
                (
                    product.spare_id,
                    product.spare_name,
                    product.spare_Price
                )
                )
    return last_row_id

def update_product2(spare_id: str,product: ProductModel):
    is_update = query_update("""
            UPDATE Materials
                SET spare_name = %s,
                spare_Price = %s
                WHERE spare_id = %s;
            """,
            (
                product.spare_name,
                product.spare_Price,
                spare_id
            )
            )
    if is_update:
        product_update_data = product.dict()
        product_update_data.update({"spare_id": spare_id})
        return product_update_data
    else:
        return None
    
def delete_product2(spare_id: str):
    is_deleted = query_update("""
        DELETE FROM Materials
        WHERE spare_id = %s;
        """,
        (spare_id,)
        )
    return is_deleted
