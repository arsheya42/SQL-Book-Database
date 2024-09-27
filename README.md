# Project Description: Donated Books Inventory and Sales Management System

## Overview

This project, titled Donated Books Inventory and Sales Management System, is developed by Arsheya Mathur as a high school project. It leverages Python and SQL to create an efficient platform for managing the donation and purchase of books, fostering community engagement in literacy initiatives.

## Features

+ **Menu-Driven Interface:** The program offers a straightforward menu that allows users to navigate through options for donating books, purchasing books, and searching the inventory.
+ **Book Donation:** Users can easily donate books. If the book already exists in the inventory, the system updates the quantity; otherwise, it adds a new book entry along with its details.
+ **Book Purchase:** Users can purchase books while the system checks the availability and updates the inventory accordingly.
Comprehensive Search Functionality: Users can search for books by various attributes, including book name, author, series, genre, and book type. Results are displayed in a well-formatted table for easy viewing.
+ **Transaction Logging:** Every donation and purchase is logged in the database, providing a complete transaction history.

## Technologies Used

+ **Python:** Used for implementing the core functionalities and user interface.
+ **MySQL:** Utilized for managing the backend database, ensuring reliable data storage and retrieval.

## Code Explanation

+ The program connects to a MySQL database named STOCK, where all book and transaction records are stored.
+ The donate_book function allows users to donate books, updating existing records or creating new ones as necessary.
+ The purchase_book function enables users to purchase books, verifying stock levels before proceeding with the transaction.
+ The search_menu function provides users with multiple search options, displaying results in a user-friendly table format using the PrettyTable library.

## Conclusion

This project not only showcases programming and database management skills but also emphasizes the importance of community contributions to literacy. It serves as a practical example of how technology can be harnessed to facilitate charitable initiatives and improve access to books.
