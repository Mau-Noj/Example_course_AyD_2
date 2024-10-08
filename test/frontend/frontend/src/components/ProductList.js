import React, { useState, useEffect } from 'react';
import { getAllProducts } from '../services/productService';

const ProductList = ({ onSelectProduct }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const data = await getAllProducts();
        setProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };
    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {products.map(product => (
          <li key={product.id} onClick={() => onSelectProduct(product.id)}>
            {product.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
