function searchBooks() {
    const searchBy = document.getElementById("searchBy").value;
    const searchQuery = document.getElementById("searchInput").value.toLowerCase();
    const books = JSON.parse(localStorage.getItem('books')) || [];
    const searchResults = books.filter(book =>
        book[searchBy].toLowerCase().includes(searchQuery)
    );
    displaySearchResults(searchResults);
}


function displaySearchResults(results) {
    const searchResultsContainer = document.getElementById("searchResults");
    searchResultsContainer.innerHTML = ""; // Clear previous search results
    if (results.length === 0) {
        searchResultsContainer.innerHTML = "<p>No matching books found.</p>";
    } else {
        results.forEach(book => {
            const bookItem = document.createElement("div");
            bookItem.classList.add("book-item");
            bookItem.innerHTML = `
                <img src="${book.imageUrl}" alt="${book.title}">
                <div class="book-info">
                    <h3>${book.title}</h3>
                    <p><strong>Author:</strong> ${book.author}</p>
                    <p><strong>Category:</strong> ${book.category}</p>
                    <p>${book.description}</p>
                    <button onclick="borrowBook('${book.id}')">Borrow</button>
                </div>
            `;
            searchResultsContainer.appendChild(bookItem);
        });
    }
}

function borrowBook(bookId) {
    let borrowedBooks = JSON.parse(localStorage.getItem('borrowedBooks')) || [];
    let books = JSON.parse(localStorage.getItem('books')) || [];
    const bookIndex = books.findIndex(book => book.id === bookId);
    if (bookIndex !== -1) {
        const book = books[bookIndex];
        if (!book.available) {
            alert("This book is not available for borrowing.");
            return;
        }
        book.available = false;
        borrowedBooks.push(book);
        books.splice(bookIndex, 1); // Remove the borrowed book from available books
        localStorage.setItem('borrowedBooks', JSON.stringify(borrowedBooks));
        localStorage.setItem('books', JSON.stringify(books));
        displaySearchResults(books); // Update search results
        displayBorrowedBooks(borrowedBooks); // Update borrowed books list
    } else {
        console.log('Book not found.');
    }
}

function displayBorrowedBooks(borrowedBooks) {
    const borrowedList = document.getElementById("borrowedList");
    borrowedList.innerHTML = ""; 
    borrowedBooks.forEach(book => {
        const listItem = document.createElement("li");
        listItem.textContent = `${book.title} by ${book.author}`;
        borrowedList.appendChild(listItem);
    });
}

window.onload = function() {
    displayBorrowedBooks(JSON.parse(localStorage.getItem('borrowedBooks')) || []);
};
