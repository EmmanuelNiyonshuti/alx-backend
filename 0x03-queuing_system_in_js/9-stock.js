#!/usr/bin/node
import express from 'express';
import redis from 'redis';
import util from 'util';

const port = 1245;
const app = express();

const client = redis.createClient();

const clientGet = util.promisify(client.get).bind(client);

const arr = [
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]

const getItemById = (id) => { 
    for (const item of arr){
        if (item.id === id){
            return item
        }
    }
}

app.get('/list_products', (req, res) => {
    const items = arr.map((item) => {
        return {
            itemId: item.id,
            itemName: item.name,
            price: item.price,
            initialAvailableQuantity: item.stock
        }
    });
    res.send(items);
})

const reserveStockById = (itemId, stock) => {
    client.set(itemId, stock);
}

const getCurrentReservedStockById = async (itemId) => {
    const reserved_stock = await clientGet(itemId);
    return reserved_stock ? parseInt(reserved_stock): null;
}

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    if (!itemId){
        res.json({"status": "Product not found"});
        return;
    }
    const product = getItemById(itemId);

    if (!product){
        res.json({"status": "Product not found"});
        return;
    }
    const currQuantity = await getCurrentReservedStockById(itemId) || product.stock;
    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currQuantity   
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    if (!product){
        res.json({ "status": "Product not found" });
        return;
    }
    const currentQuantity = await getCurrentReservedStockById(itemId) || product.stock;

    if (currentQuantity <= 0) {
        res.json({ "status": "Not enough stock available", "itemId": itemId });
        return;
    }

    await reserveStockById(itemId, currentQuantity - 1);
    res.json({ "status": "Reservation confirmed", "itemId": itemId });
});

app.listen(port, () => {
    console.log(`server listening on ${port} port`);
})

