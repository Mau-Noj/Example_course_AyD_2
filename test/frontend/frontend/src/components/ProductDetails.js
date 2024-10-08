import React, { useState, useEffect } from 'react';
import { getProductById } from '../services/productService';

const ProductDetails = ({ productId }) => {
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const data = await getProductById(productId);
        setProduct(data);
      } catch (error) {
        console.error('Error fetching product details:', error);
      }
    };

    if (productId) {
      fetchProduct();
    }
  }, [productId]);

  if (!product) {
    return <p>Select a product to see details</p>;
  }

  return (
    <div>
      <h3>{product.title}</h3>
      <img src={product.image} alt={product.title} width="150" />
      <p>{product.description}</p>
      <p>Price: ${product.price}</p>
    </div>
  );
};

export default ProductDetails;
