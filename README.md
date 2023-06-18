# Netflix 2.0 Web App

<p align="center">
<!--    ![Netflix Logo](./netflixprj/static/assets/netflix.png) -->
   <img src="./netflixprj/static/assets/netflix.png" />
</p>

The Netflix 2.0 web application is a streaming platform built entirely from scratch using Python Django, SQLite database, HTML, Bootstrap, and Vanilla JavaScript. It offers a wide range of features to enhance the streaming experience for users.

## Features

- **Signup/Login**: Users can easily create an account or log in using their email and username credentials.
- **Extensive Streaming Library**: The web app provides a plethora of movies and TV shows for users to enjoy.
- **User Profiles**: Multiple user profiles can be created within a single account, allowing personalised content streaming for each user.
- **Content Categories**: The platform offers two categories of content: universal and kids-only.
- **Age-Based Content Segregation**: The app segregates content based on the user's age preference. If a user selects the 'Kids' option, only kids-only content will be visible, while other content will remain hidden.

## Implementation Details

- **Models**: The app includes models for Profile, Movie, and Video, which have been created and migrated to the SQLite database.
- **ORMs**: Object-Relational Mapping (ORM) is used to interact with the SQLite database, providing an intuitive and efficient way to manage data.
- **User Authentication and Authorisation**: The app leverages Django's built-in authentication system to handle user authentication and authorisation securely.
- **CSRF Tokens**: CSRF tokens are implemented to ensure secure communication and protect against cross-site request forgery attacks.

## Tech Stack

The Netflix 2.0 web app is built using the following technologies:

- **Python**: The backend logic and server-side implementation are written in Python.
- **Django**: The web framework Django is used for rapid development and efficient handling of various components.
- **SQLite**: A lightweight and serverless database system, SQLite, is used for data storage and retrieval.
- **HTML5**: HTML5 provides the structure and semantics for the web pages of the app.
- **Bootstrap**: Bootstrap CSS framework is employed for responsive and visually appealing UI design.
- **Vanilla JavaScript**: Vanilla JavaScript is used for interactive features and dynamic content manipulation.

## Installation and Usage

To run the Netflix 2.0 web app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/mishrakushal/netflix-2.git
   ```

2. Navigate to the project directory:

   ```bash
   cd netflix-2/netflixprj
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open your web browser and visit `http://localhost:8000` to access the Netflix 2.0 web app.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).

---

Enjoy streaming your favorite movies and TV shows with Netflix 2.0! If you encounter any issues or have suggestions for improvement, please feel free to contribute or report them in the project repository. Thank you.
