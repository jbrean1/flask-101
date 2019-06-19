# tests/test_views.py
from flask_testing import TestCase
from flask import json
from wsgi import app


class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_products_json_id_get(self):
        response = self.client.get("/api/v1/products/3")
        product = response.json
        self.assertIsInstance(product, dict)
        self.assertEqual(product['id'], 3)

    def test_products_json_id_delete(self):
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code, 204)

    def test_products_json_id_create(self):0
        response = self.client.post("/api/v1/products", data=dict(id= 4, name= "vindicator"))
        self.assertEqual(response.status_code, 201)
        """
        response = self.client.post("/api/v1/products/")
        self.assertEqual(response.status_code, 204)
        """
