# MyAMTS 🚌

> A comprehensive web application for Ahmedabad's public transport system with real-time tracking and smart route planning

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-v4.0+-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/bootstrap-v5.0+-purple.svg)](https://getbootstrap.com/)
[![GitHub stars](https://img.shields.io/github/stars/Manthan0207/My-Amts.svg)](https://github.com/Manthan0207/My-Amts/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Manthan0207/My-Amts.svg)](https://github.com/Manthan0207/My-Amts/network)

## 🌟 Overview

MyAMTS Web is a user-friendly platform designed to provide real-time information about Ahmedabad's AMTS bus services. Built with Django framework and modern web technologies, it helps commuters plan their routes efficiently with an intuitive UI and seamless navigation. The application offers comprehensive features including real-time bus tracking, route planning, digital ticket booking with QR codes, and journey history management.

## ✨ Key Features

### 🏠 Main Dashboard
- **Clean Interface** - User-friendly platform with intuitive navigation
- **Quick Access** - Key features and navigation options readily available
- **Recent Searches** - View previously searched routes for quick access
- **Nearby Bus Stops** - Find bus stops in your vicinity
- **Route Finder** - Search for routes by bus number

### 🔍 Smart Route Planning
- **Source & Destination Search** - Find buses based on your travel points
- **Multiple Route Options** - Shows all available buses for your journey
- **Interchange Support** - Provides interchange options when direct routes aren't available
- **Optimal Route Suggestions** - Intelligent routing for efficient travel

### 🗺️ Interactive Map Integration
- **Route Visualization** - Displays selected bus route directly on the map
- **Real-time Bus Locations** - Live tracking of bus positions
- **Stop Markers** - Visual representation of all bus stops along the route
- **Interactive Navigation** - Click and explore different routes and stops

### ⏰ Real-time Bus Status
- **Live Tracking** - Real-time bus location updates
- **Schedule Status** - Indicates whether a bus is on time or delayed
- **Arrival Predictions** - Estimated arrival times at stops
- **Service Alerts** - Real-time notifications about service disruptions

### 🎫 Digital Ticketing System
- **Online Booking** - Book tickets directly through the platform
- **QR Code Generation** - Digital tickets with QR codes containing trip details
- **Booking History** - View previous ticket bookings and journey records
- **Trip Management** - Manage current and upcoming journeys

### 📱 User Experience Features
- **Responsive Design** - Seamless experience across all devices
- **Fast Performance** - Optimized for quick loading and smooth navigation
- **Intuitive UI** - Clean and modern interface design
- **Search History** - Quick access to frequently used routes

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Core programming language
- **Django 4.0+** - Web framework for robust backend
- **SQLite/PostgreSQL** - Database for storing routes, schedules, and user data
- **Django REST Framework** - API development for real-time features
- **WebSocket Support** - Real-time bus tracking updates

### Frontend
- **HTML5** - Semantic markup structure
- **CSS3** - Modern styling with responsive design
- **JavaScript (ES6+)** - Interactive functionality and real-time updates
- **Bootstrap 5** - CSS framework for responsive design
- **Interactive Maps** - Real-time route and bus location visualization
- **QR Code Library** - Digital ticket generation
- **AJAX** - Seamless data updates without page reload

### Key Integrations
- **Geolocation API** - Location-based services
- **Map Services** - Interactive route visualization
- **Real-time Data** - Live bus tracking and schedule updates
- **QR Code Generation** - Digital ticketing system

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Manthan0207/My-Amts.git
   cd My-Amts
   ```

2. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Load AMTS Data**
   ```bash
   python manage.py loaddata fixtures/bus_routes.json
   python manage.py loaddata fixtures/bus_stops.json
   python manage.py loaddata fixtures/schedules.json
   ```

4. **Run the application**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   
   Open `http://127.0.0.1:8000` in your browser


## 🎯 Core Functionality

### Route Search & Planning
- **Smart Search Algorithm** - Find optimal routes between any two points
- **Multiple Options** - Display various route combinations
- **Interchange Detection** - Automatically suggest transfer points
- **Route Comparison** - Compare time, distance, and convenience

### Real-time Tracking
- **Live Bus Locations** - GPS-based real-time bus positions
- **Schedule Adherence** - On-time/delayed status indicators  
- **Arrival Predictions** - Estimated arrival times using real-time data
- **Service Disruptions** - Immediate alerts about route changes

### Digital Ticketing
- **Seamless Booking** - Quick and easy ticket purchase
- **QR Code Tickets** - Digital tickets with embedded trip information
- **Booking Management** - View and manage current and past bookings

### User Experience
- **Personalized Dashboard** - Customized experience based on usage patterns
- **Search History** - Quick access to frequently used routes
- **Favorites System** - Save commonly used routes and stops
- **Responsive Design** - Optimal experience across all devices



### Map Integration
```javascript
// Map configuration for route visualization
const mapConfig = {
    center: [23.0225, 72.5714], // Ahmedabad coordinates
    zoom: 12,
    tileLayer: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
};
```

## 📱 User Journey

1. **Dashboard Access** - Land on the main dashboard with navigation options
2. **Route Search** - Enter source and destination for journey planning
3. **Route Selection** - Choose from available route options with details
4. **Map Visualization** - View selected route on interactive map
5. **Real-time Tracking** - Monitor bus location and arrival status
6. **Ticket Booking** - Book tickets and receive QR code confirmation
7. **Journey Management** - Track bookings and view travel history

### Environment Variables
```env
# Production settings
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
SECRET_KEY=your_production_secret_key
DATABASE_URL=postgresql://user:pass@host:port/db
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📋 Future Enhancements

- [ ] **Mobile Application** - Native iOS/Android app
- [ ] **Payment Gateway** - Multiple payment options
- [ ] **Multi-language** - Support for Gujarati and Hindi
- [ ] **Bus Crowding** - Real-time occupancy information
- [ ] **Smart Notifications** - Personalized journey alerts
- [ ] **Analytics Dashboard** - Usage statistics and insights



## 👨‍💻 Author

**Manthan Patel**
- GitHub: [@Manthan0207](https://github.com/Manthan0207)
- Portfolio: [https://portfolio-11lq.onrender.com](https://portfolio-11lq.onrender.com)
- Email: manthanpanseriya0205@gmail.com





⭐ **If this project helped you, please give it a star!** ⭐

