#!/bin/bash

echo "================================="
echo "Building ShopNow Docker Images"
echo "================================="

echo ""
echo "Building Backend..."
docker build -t shopnow-backend:v1 ./backend

echo ""
echo "Building Frontend..."
docker build -t shopnow-frontend:v1 ./frontend

echo ""
echo "Building Admin..."
docker build -t shopnow-admin:v1 ./admin

echo ""
echo "================================="
echo "Build completed successfully!"
echo "================================="