from fastapi import FastAPI, HTTPException, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
#Product เรียกใช้โฟลเดอร์พร้อมไฟล์ข้างใน
from product import ProductModel,get_all_product,get_product_by_id,add_product,update_product,delete_product
from product import ProductModel2,get_all_product2,get_product_by_id2,add_product2,update_product2,delete_product2

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ##GET
@app.get("/get_all_product/", response_model=list[ProductModel])
def get_all_product_api():
    products = get_all_product()
    print(products)
    return JSONResponse(status_code=200, content=jsonable_encoder(products))

@app.get("/get_product/{pattern_id}", response_model=ProductModel)
def get_product_by_id_api(pattern_id:str):
    products = get_product_by_id(pattern_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(products))

#Post Create
@app.post('/create_product/', response_model=ProductModel)
def create_product_api(product: ProductModel):
    pattern_id = add_product(product)
    return JSONResponse(status_code=201, content={'status': 'success', 'product_id': pattern_id})

#Update
@app.put("/update_product/{pattern_id}", response_model=ProductModel)
def update_product_api(pattern_id: str, product: ProductModel):
    # Check if product exists
    existing_product = get_product_by_id(pattern_id)
    if len(existing_product) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    updated_product = update_product(pattern_id, product)
    if updated_product:
        return JSONResponse(status_code=200, content={'status': 'success', 'product_data': updated_product})
    else:
        raise HTTPException(status_code=500, detail="Failed to update data")
    
#Delete
@app.delete("/delete_product/{pattern_id}", response_model=ProductModel)
def delte_product_api(pattern_id: str):
    existing_product = get_product_by_id(pattern_id)
    if len(existing_product) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_product(pattern_id)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")

# ##GET
@app.get("/get_all_product2/", response_model=list[ProductModel2])
def get_all_product2_api():
    products = get_all_product2()
    print(products)
    return JSONResponse(status_code=200, content=jsonable_encoder(products))

@app.get("/get_product2/{spare_id}", response_model=ProductModel2)
def get_product_by_id2_api(spare_id:str):
    products = get_product_by_id2(spare_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(products))

#Post Create
@app.post('/create_product2/', response_model=ProductModel2)
def create_product2_api(product: ProductModel2):
    spare_id = add_product2(product)
    return JSONResponse(status_code=201, content={'status': 'success', 'product_id': spare_id})

#Update
@app.put("/update_product2/{spare_id}", response_model=ProductModel2)
def update_product2_api(spare_id: str, product: ProductModel2):
    # Check if product exists
    existing_product = get_product_by_id2(spare_id)
    if len(existing_product) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    updated_product = update_product2(spare_id, product)
    if updated_product:
        return JSONResponse(status_code=200, content={'status': 'success', 'product_data': updated_product})
    else:
        raise HTTPException(status_code=500, detail="Failed to update data")
    
#Delete
@app.delete("/delete_product2/{spare_id}", response_model=ProductModel2)
def delte_product2_api(spare_id: str):
    existing_product = get_product_by_id2(spare_id)
    if len(existing_product) == 0:
        raise HTTPException(status_code=404, detail="Data not found")
    is_deleted = delete_product2(spare_id)
    if is_deleted:
        return JSONResponse(status_code=200, content={'status': 'success', 'message':'Data deleted successfully'})
    else:
        raise HTTPException(status_code=500, detail="Failed to delete data")


