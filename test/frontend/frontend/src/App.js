import React, { useState } from 'react';
import ProductList from '../src/components/ProductList';
import ProductDetails from '../src/components/ProductDetails';

function App() {
  const [selectedProductId, setSelectedProductId] = useState(null);

  const handleSelectProduct = (id) => {
    setSelectedProductId(id);
  };

  return (
    <div className="App">
      <h1>Fake Store</h1>
      <div style={{ display: 'flex', gap: '20px' }}>
        <ProductList onSelectProduct={handleSelectProduct} />
        <ProductDetails productId={selectedProductId} />
      </div>
    </div>
  );
}

export default App;
