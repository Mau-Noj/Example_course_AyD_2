const request = require('supertest');
const express = require('express');
const productRoutes = require('../../src/routes/productRoutes');

const app = express();
app.use(express.json());
app.use('/api', productRoutes);

describe('Product Routes - Integration Tests', () => {
  test('GET /api/products - should return all products', async () => {
    const response = await request(app).get('/api/products');
    
    /********** Verifica que el estado HTTP sea 200  ************/
    expect(response.status).toBe(200); 
    expect(Array.isArray(response.body)).toBe(true); 
  });

  test('GET /api/products/:id - should return a product by ID', async () => {
    const response = await request(app).get('/api/products/1');
    
    /********** Verifica que el estado HTTP sea 200  ************/
    expect(response.status).toBe(200); 

    /**********  Verifica que el producto tenga el ID correcto  ***********/
    expect(response.body).toHaveProperty('id', 1); 
  });
});
