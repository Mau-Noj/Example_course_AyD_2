const express = require('express');
const productRoutes = require('./src/routes/productRoutes');

const app = express();
const port = 3000;

app.use(express.json());

app.use('/api', productRoutes);

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
