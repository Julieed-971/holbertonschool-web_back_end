import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({
    host: '127.0.0.1',
    port: 6379
});

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

const listProducts = [
    { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5, }
];

const getItemById = (id) => {
    return listProducts.find(product => product.Id === id) || null;
}

const getAllAvailableProducts = () => {
    let listAllAvailableProducts = []
    listProducts.forEach(product => {
        listAllAvailableProducts.push({
            "itemId": product.Id,
            "itemName": product.name,
            "price" : product.price,
            "initialAvailableQuantity": product.stock,
        });
    });
    return listAllAvailableProducts;
}

const reserveStockById = (itemId, stock) => {
    client.set(`item.${itemId}`, stock, redis.print);
}

const getCurrentReservedStockById = async (itemId) => {
    try {
        const stock = await getAsync(`item.${itemId}`);
        return stock !== null ? Number(stock) : null;
    } catch (err) {
        console.log(err);
    }
}

const express = require('express');
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
    return res.json(getAllAvailableProducts());
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const currentProduct = getItemById(itemId);
    
    if (!currentProduct) {
        return res.json({"status":"Product not found"});
    }

    let currentProductAvailableStock = await getCurrentReservedStockById(itemId);
    if (currentProductAvailableStock === null) {
        currentProductAvailableStock = currentProduct.stock;
    }
    
    return res.json({
        "itemId": currentProduct.Id,
        "itemName": currentProduct.name,
        "price": currentProduct.price,
        "initialAvailableQuantity": currentProduct.stock,
        "currentQuantity": currentProductAvailableStock,
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = Number(req.params.itemId);
    const currentProduct = getItemById(itemId);
    
    if (!currentProduct) {
        return res.json({"status":"Product not found"});
    }

    let currentProductAvailableStock = await getCurrentReservedStockById(itemId);
    if (currentProductAvailableStock === null) {
        currentProductAvailableStock = currentProduct.stock;
        await reserveStockById(itemId, currentProductAvailableStock);
    }

    if (currentProductAvailableStock <= 0) {
        return res.json({"status":"Not enough stock available","itemId": itemId});
    }

    await reserveStockById(itemId, currentProductAvailableStock - 1);
    return res.json({"status":"Reservation confirmed","itemId":itemId});
})

app.listen(port, () => {
    console.log(`App listening on port ${port}`);
});
