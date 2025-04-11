# 🌟 Part 4 - HBnB Simple Web Client

In this phase, you’ll be focusing on the **front-end development** of your application using **HTML5**, **CSS3**, and **JavaScript ES6**. Your task is to design and implement an interactive user interface that connects with the back-end services you have developed in previous parts of the project.

---

## 📋 Objectives

- 🖥️ Develop a user-friendly interface following provided design specifications.
- 🔗 Implement client-side functionality to interact with the back-end API.
- 🔒 Ensure secure and efficient data handling using JavaScript.
- 🚀 Apply modern web development practices to create a dynamic web application.

---

## 🎯 Learning Goals

- 📜 Understand and apply **HTML5**, **CSS3**, and **JavaScript ES6** in a real-world project.
- 🌐 Learn to interact with back-end services using **AJAX/Fetch API**.
- 🔑 Implement authentication mechanisms and manage user sessions.
- ⚡ Use client-side scripting to enhance user experience without page reloads.

---

## 🛠️ Tasks Breakdown

### 1️⃣ Design (Task 1)
#### Objectives:
- Complete provided HTML and CSS files to match the given design specifications.
- Create pages for:
  - Login
  - List of Places
  - Place Details
  - Add Review

#### Requirements:
- Use semantic HTML5 elements to structure content.
- Apply CSS styles to match design specifications.

#### Pages:
1. **Login Form**: Fields for email and password.
2. **List of Places**: Display basic information about places.
3. **Place Details**: Detailed view for a specific place.
4. **Add Review Form**: Accessible only to authenticated users.

---

### 2️⃣ Login (Task 2)
#### Objectives:
- Implement login functionality using the back-end API.
- Store JWT token returned by the API in a cookie for session management.

#### Instructions:
1. Add an event listener to handle form submission (`scripts.js`).
2. Use Fetch API to send a POST request with user credentials.
3. Store JWT token in cookies upon successful login.
4. Redirect authenticated users to `index.html`.

---

### 3️⃣ List of Places (Task 3)
#### Objectives:
- Display a list of places dynamically fetched from the API.
- Implement client-side filtering based on price or country.

#### Instructions:
1. Verify user authentication via cookies.
2. Fetch places data using Fetch API and populate dynamically into `index.html`.
3. Add filtering functionality without page reloads.

---

### 4️⃣ Place Details (Task 4)
#### Objectives:
- Fetch detailed information about a place using its ID from the URL query parameters.
- Display extended information such as host, price, description, amenities, and reviews.

#### Instructions:
1. Extract place ID from URL query parameters.
2. Verify user authentication via cookies.
3. Fetch place details using Fetch API and populate dynamically into `place.html`.

---

### 5️⃣ Add Review (Task 5)
#### Objectives:
- Implement a form for adding reviews accessible only to authenticated users.

#### Instructions:
1. Display the form only if the user is authenticated.
2. Redirect unauthenticated users to `index.html`.
3. Send review data to the API via Fetch API.

---

## 🌟 Design Guidelines

### Fixed Parameters:
- **Margin:** Use a margin of `20px` for place and review cards.
- **Padding:** Use a padding of `10px` within place and review cards.
- **Border:** Use a border of `1px solid #ddd` for place and review cards.
- **Border Radius:** Use a border radius of `10px` for place and review cards.

### Flexible Parameters:
Feel free to customize:
- 🎨 Color palette
- ✍️ Fonts
- 🖼️ Images (sample images provided)
- 📌 FavIcon: Add custom favicon or use provided icon.png.

---

## 🚀 Resources

Here are some helpful links:

1. [HTML5 Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML)
2. [CSS3 Documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
3. [JavaScript ES6 Features](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
4. [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
5. [Responsive Web Design Basics](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)
6. [Handling Cookies in JavaScript](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)

---

## 🧪 Tests

Here are examples of tests you can perform for each feature:

### ✅ Login Page
1. Open `login.html` in your browser.
2. Enter valid credentials (e.g., `email: test@example.com`, `password: password123`) and submit the form.
   - Expected Result: You should be redirected to `index.html`, and a JWT token should be stored in your browser's cookies.
3. Enter invalid credentials (e.g., incorrect email or password) and submit the form.
   - Expected Result: An error message should appear, indicating invalid login credentials.

### ✅ List of Places
1. Open `index.html` after logging in successfully.
2. Check if all places are dynamically loaded from the back-end API into the page as cards or list items.
   - Expected Result: The list should display accurate details such as name, location, price, etc., fetched from the API.
3. Test filtering by entering a price range or country name in the filter fields, then submit or apply filters dynamically without reloading the page.
   - Expected Result: The displayed places should update based on your filter criteria.

### ✅ Place Details Page
1. Click on any place card from the list on `index.html` to navigate to its details page (`place.html?place_id=<id>`).
   - Expected Result: The page should display detailed information about the selected place, including host details, amenities, reviews, etc., fetched from the back-end API using its ID.

### ✅ Add Review Form
1. Navigate to `add_review.html` while logged in as an authenticated user.
   - Expected Result: A form should be visible for adding reviews (e.g., rating, comment).
2. Submit a valid review (e.g., rating: 5 stars, comment: "Amazing experience!").
   - Expected Result: The review should be sent successfully to the back-end API, and you may see it added immediately or after refreshing the page on `place.html`.
3. Try accessing `add_review.html` without logging in (clear cookies or open in incognito mode).
   - Expected Result: You should be redirected automatically to `index.html`.

---

## AUTHORS 📌

- [Saynez667](https://github.com/Saynez667)

✨ Happy coding! 😊
