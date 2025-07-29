# 🌐 Social Media Web Application – Setup & Environment Guide

This is a full-stack social media web application that includes user authentication, posts, likes, comments, profile management, image uploads via Cloudinary, and more.

---

## ⚙️ Environment Configuration (`.env`)

Create a `.env` file in your project root and paste the following:

 PORT=5000
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
CLOUDINARY_CLOUD_NAME=your_cloudinary_cloud_name
CLOUDINARY_API_KEY=your_cloudinary_api_key
CLOUDINARY_API_SECRET=your_cloudinary_api_secret


---

## 🚀 Tech Stack

- **Frontend**: React.js (optional)
- **Backend**: Node.js, Express.js
- **Database**: MongoDB with Mongoose
- **Authentication**: JWT (JSON Web Tokens)
- **Media Uploads**: Cloudinary

---

## 📁 Backend Folder Structure (Example)
---
- backend/
- ├── models/
- ├── routes/
- ├── controllers/
- ├── middleware/
- ├── utils/
- ├── .env
- ├── server.js (or app.js)
- ├── package.json

---


---

## 📦 Installation Instructions

Install all required dependencies:

```bash
npm install


# Development Mode
npm run dev


# Production Mode
npm start
