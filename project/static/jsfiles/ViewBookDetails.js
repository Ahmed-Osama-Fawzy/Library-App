function displaySelectedBookDetails() {
    const selectElement = document.getElementById("selectBook");
    const bookId = selectElement.value;
    const books = JSON.parse(localStorage.getItem('books')) || [];
    const selectedBook = books.find(book => book.id === bookId);

    const bookDetailsContainer = document.getElementById("bookDetails");
    bookDetailsContainer.innerHTML = "";

    if (selectedBook) {
        const bookDetails = `
            <h2>${selectedBook.title}</h2>
            <p><strong>ID:</strong> ${selectedBook.id}</p>
            <p><strong>Author:</strong> ${selectedBook.author}</p>
            <p><strong>Category:</strong> ${selectedBook.category}</p>
            <p><strong>Description:</strong> ${selectedBook.description}</p>
            <p><strong>Available:</strong> ${selectedBook.available ? "Yes" : "No"}</p>
            <img src="${selectedBook.imageUrl}" alt="${selectedBook.title}" style="width: 200px; height: auto;">
        `;
        bookDetailsContainer.innerHTML = bookDetails;
    } else {
        bookDetailsContainer.innerHTML = "<p>No book selected.</p>";
    }
}

window.onload = function () {
    const selectElement = document.getElementById("selectBook");
    const books = JSON.parse(localStorage.getItem('books')) || [];
    books.forEach(book => {
        const option = document.createElement("option");
        option.value = book.id;
        option.text = book.title;
        selectElement.appendChild(option);
    });
};